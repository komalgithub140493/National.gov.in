from diagrams import Cluster, Diagram, Node, Edge
from diagrams.gcp.network import LoadBalancing
from diagrams.k8s.infra import Node
from diagrams.aws.general import TraditionalServer
from diagrams.aws.management import OpsworksApps
from diagrams.onprem.network import Haproxy
from diagrams.custom import Custom
 
 
 
 
graph_attr = {
    "fontsize": "55",
    "bgcolor": "transparent"
}
  
with Diagram("Cluster nesting", show=False):
    Service = LoadBalancing("service")

    with Cluster("Kubernetes"):
        
        with Cluster("HAproxy"):
             haproxy = Haproxy("HAProxy")
             haproxy2 = Haproxy("HAProxy")
  
            
        # Connect HAProxy 1 to HAProxy 2 with a simple line
        haproxy - Edge(style="dotted" , color ="gray") - haproxy2
             
        with Cluster(""):       
             with Cluster("Node"):
                  node1 = Node("Worker Node1")
                  node2 = Node("Worker Node2")
             
             with Cluster("Nodes"):
                  nodes3 = Node("Worker Node3")
                  nodes4 = Node("Worker Node4")
                  nodes5 = Node("Worker Node5")
            
    with Cluster("Services"):
        with Cluster("Apps"):
            opsworks_apps1 = OpsworksApps("Apps 1")
            opsworks_apps2 = OpsworksApps("Apps 2")
            opsworks_apps3 = OpsworksApps("Apps 3")

        with Cluster("Server"):
            traditional_server1 = TraditionalServer("API Server 1")
            traditional_server2 = TraditionalServer("API Server 2")
            traditional_server3 = TraditionalServer("API Server 3")

    # Connect OpsworksApps to Apps cluster
    opsworks_apps1 -  Edge(style= "dotted" , color ="gray") - opsworks_apps2
    opsworks_apps2 -  Edge(style= "dotted" , color ="gray") - opsworks_apps3

    # # Connect HAProxy cluster to Nodes cluster
    # haproxy2 >> Edge(label="") >> nodes3
    
    node2 >> traditional_server2
    
    
    # Add a connection for "Service" to "NPCI" and "Aadhar" boxes
    with Cluster("Aadhar"):
        # Add an Aadhar Box
        aadhar_box = Custom("", "./aadhar_box.png")  # Replace with your Aadhar Box image path

    with Cluster("NPCI"):
        # Add an NPCI Box
        npci_box = Custom("", "./npci_box.png")  # Replace with your NPCI Box image path


    # aadhar_box - Edge(style="dotted", color="gray") - npci_box
    
    
    Service >> Edge(style="", direction="TB", color="darkgreen") >> npci_box
    Service >> Edge(style="", direction="TB", color="darkgreen") >> aadhar_box

   # Connect HAProxy cluster to Nodes cluster (outside of clusters)
    haproxy >> Edge(style= "bold dotted" , color ="red" ,label="") >> nodes3

     # Connect "API Server 2" to the Load Balancer (Service)
    traditional_server2 - Edge(headport="c", tailport="c", minlen="1", color ="darkgreen",) - Service
 
    # Add a connection from "Apps" cluster to "Kubernetes" cluster
    opsworks_apps3 >> Edge(style="bold", color="red" , label="connect to haproxy") >> haproxy
    
    # Connect TraditionalServer instances to clusters
    traditional_server1 -  Edge(style= "dotted" , color ="gray") - traditional_server2
    traditional_server2 -  Edge(style= "dotted" , color ="gray") - traditional_server3

    # Connect MyApp Ingress to Node in Kubernetes cluster
    node1 << Edge(headport="c", tailport="c", minlen="1", color ="red", lhead='cluster_Node') << nodes3
    node2 << Edge(headport="c", tailport="c", minlen="1", color ="darkgreen", lhead='cluster_Nodes') << nodes4
    
    # Services >> Edge(headport="c", tailport="c", minlen="1", lhead='cluster_Kubernetes') >> Kubernetes
       
# Save the diagram as an image
diagram.save("cluster_nesting1.png")
