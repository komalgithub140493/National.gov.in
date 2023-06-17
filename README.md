# National Portal Of India 2.0
<img src="https://upload.wikimedia.org/wikipedia/commons/5/55/Emblem_of_India.svg" width="50" height="100">

# OBJECTIVES 

> **S3WaaS providing data through API of components** 

+ Knowindia - tourist places
+ Knowindia - accommodation
+ Knowindia - photo gallery
+ Knowindia - culinary delights
+ Knowindia - helpline
+ Knowindia - produce
+ Knowindia - public utilities (School)
+ District- Who is Who

❏ **Analysis of  above mentioned API responses**
 
- **Mapping** the API response into common & specific fields as per the guidelines document shared by the NIC NPI team (NPI_2.0_datasources_and_metadata)
- Proposed some **new attributes in common and specific portions** as and when required

❏ **Suggesting faceted “Search” fields** from the response received
  
❏ Suggesting **Business use case** 

# OBJECTIVE : 1 

# Analysis API Responses
  - 1.1 Content Type : Know India - Tourist Place

#### REQUEST URL = https://api.s3waas.gov.in/api/v1/get_touristplaces

```json
Request PayLoad

{	
	"deviceID": "ffffffff-c0f8-4e30-ffff-ffffef05ac4a",
	"categoryId": "",
	"searchText":"",
	"stateId": "",
	"districtId": "",
	"placeTypeId":"",
	"pageIndex": "1",
	"recordPerpage": "10",
	"most_liked": "0",
	"most_viewed": "0",
	"popular":"0",
	"language": "en",
	"ignore_id":"kNiZvYQBvAOITNx44CEb"
}
```
### 

```json
Response

{
  "resultFlag": 1,
  "message": "Detail Found",
  "cache": 0,
  "data": {
    "totalRecords": 3159,
    "pages": 316,
    "PlaceList": [
      {
        "_index": "touristplace",
        "_type": "_doc",
        "_id": "h96gdYgBvAOITNx4Pm_8",
        "image": "https://cdn.s3waas.gov.in/s36bc24fc1ab650b25b4114e93a98f1eba/uploads/2018/08/2018081222.png",
        "title": "MANDARTHI SHREE DURGAPARAMESHWARI TEMPLE",
        "url": "https://udupi.nic.in/en/tourist-place/mandarthi-shree-durgaparameshwari-temple/",
        "latitude": 13.4979,
        "longitude": 74.8104,
        "totalViews": 0,
        "totalLikes": 0,
        "isLiked": 0,
        "cityName": "Udupi",
        "cityID": 829,
        "stateName": "Karnataka",
        "statecode": "KA",
        "stateID": 15,
        "placeCategoryName": ["Religious"],
        "placeCategoryID": [321],
        "stayDetails": [],
        "video_url": "",
        "id": 3334,
        "imageList": {
          "title": "god_temple",
          "alt": "mandharthi",
          "image": "https://cdn.s3waas.gov.in/s36bc24fc1ab650b25b4114e93a98f1eba/uploads/2018/08/2018081222.png",
          "thumb_img_url": "https://cdn.s3waas.gov.in/s36bc24fc1ab650b25b4114e93a98f1eba/uploads/2018/08/2018081222-150x150.png",
          "full_img_url": "https://cdn.s3waas.gov.in/s36bc24fc1ab650b25b4114e93a98f1eba/uploads/2018/08/2018081222.png"
        },
        "gallery_images": [
          {
            "title": "god_temple",
            "alt": "mandharthi",
            "image": "https://cdn.s3waas.gov.in/s36bc24fc1ab650b25b4114e93a98f1eba/uploads/2018/08/2018081222.png",
            "thumb_img_url": "https://cdn.s3waas.gov.in/s36bc24fc1ab650b25b4114e93a98f1eba/uploads/2018/08/2018081222-150x150.png",
            "full_img_url": "https://cdn.s3waas.gov.in/s36bc24fc1ab650b25b4114e93a98f1eba/uploads/2018/08/2018081222.png"
          }
        ],
        "languages": ["en", "kn"]
      }
    ]
  }
}

```
```
Total Records : 3149
```
## API Response Know India - Tourist Places : Common Fields..Mapping..1/2
---------------------------


 
|  Common Attribute
'(Shared by NIC Team)' | 'Closest Field from API response'  | Remarks | Query |
|---|---|---|---|
| `Id`| |Unmapped(To be filled by pipeline) | |
| `Title/Name` |title": "MANDARTHI SHREE DURGAPARAMESHWARI TEMPLE", |Mapped|This will be taken into account for free text serach|
| `Description`|                                                    |Unmapped|
| `Url` |"url": "https://udupi.nic.in/en/tourist-place/mandarthi-shree-durgaparameshwari-temple/",|Mapped|we shall fill based on API url??|
| `Lineage`||Unmapped|Kindly share mapping tables for lineage|
| `Sector`||Unmapped|
| `Keywords`|   |Unmapped (To be filled by pipeline) |To be added by Pipeline . What is difference between tags and keywords|
| `Tags`| |Unmapped (To be filled by pipeline)|To be added by Pipeline . keywords need to be discussed|
| `People Group`| |Umapped|What is to be filled ?|
| `Language`|"languages": [ "en", "kn" ]|Mapped|default is english|        
| `Source`| |Unmapped (To be filled by pipeline)|What is to be filled ?|
| `Source record Id`  |"_id": "h96gdYgBvAOITNx4Pm_8",|Mapped|Assume this is given in API response|
| `Source language`   |"languages": [ "en", "kn" ]|Mapped|default is english (this is duplicate of language) perhaps can be removed|

## API Response Know India - Tourist Places : Common Fields..Mapping..1/2

### (Shared by NIC Team)

| Common Attribute       | Closest Field from API Response | Remarks| Query/Remarks
|--------| --------- | ----------|-----------|
| `source published date`  | created_at| Mapped                                                    |
| `workflow state`         || Unmapped (To be filled by pipeline)|This will tell the pipeline processing status like ACQUIRED, TRANSFORMED, TAGGED 
| `updated by`             || Unmapped (To be filled by pipeline)|This will be the user ID of the pipeline |                                 
| `created at`             || Unmapped (To be filled by pipeline)|This will be the date when the data is fetched in NIP|
| `updated at`             || Unmapped (To be filled by pipeline)|This will be the date when the data is updated in NIP|
| `archival date`          || Unmapped (To be filled by pipeline)|This will be the date when the data is archived in NIP|                          
| `size`                   || Unmapped (To be filled by pipeline)|This will be the size of the data received of one record|                       
|`lastHitStatusCode`||Unmapped(To be filled by pipeline)|This will be the HTTP status code when the pipeline hits the source URL(e.g., 200, 404) | 
| `md5 hash`               || Unmapped (To be filled by pipeline)| This will be the MD5 hash of the data received of one record|                   
| `itemBody`               || Unmapped (To be filled by pipeline)|This will be the API response body|
| `Facet Search Map`       || Unmapped| To be added by pipeline based on the faceted search options for the data Ps: this did not exist earlier Eg: stateName: Haryana, category: Historic|  


## API Response Know India - Tourist Places : Specific Fields..Mapping
| Common Attribute       | Closest Field from API Response | Remarks| Query/Remarks
|--------| --------- | ----------|-----------|
|`category`| Closest field from API respons"placeCategoryName": ["Historic"]|Mapped| |
|`Featured image url`|"image": "https://cdn.s3waas.gov.in/s3c9e1074f5b3f9fc8ea15d152add07294/uploads/2018/05/2018051460.jpg",|Mapped|There will no images stored in NIP|
|`photos`| |Unmapped|Is it same as ‘Featured image url’. If yes, it can be removed|
|`Video url`|"video_url": "https://www.youtube.com/watch?v=ourYdg5UUhE"|Mapped| |
|`How to reach`||Unmapped|What is to be filled  here ?|
|`Custom category`| |Unmapped|Is it same as ‘ategory’. If yes, it can be removed|
|`Popularity`|Popularity(totalViews,totalLikes,isLiked)|Mapeed|his was not existing earlier. Do we add this ? should this be used in faceted search|
|`geolocation`|"latitude": 8.3914769,"longitude": 77.2594318|Mapped|lat/long is blank in some data points|


## Objective : 2
> **Suggested Search Facets**
#### Improving Search Capabilities for Know India Tourist Places API
##

*“Based on a review of the District Who is Who API response received, the following search types are suggested to improve search capabilities:”
![](Aspose.Words.3f5c9bf0-cda6-4d39-a536-2905a5a4ecf9.009.png)*
## Simple Text Search

This search type is similar to 'Google search' and allows users to perform a text-based search. To enhance this search capability, the following surface areas can be defined:

- Title
- State
- and more...

## Faceted Search

Faceted search offers options to make the search more comprehensive. It allows users to refine their search results based on specific facets. The following facets can be considered:

- GeoLocation
  - Longitude
  - Latitude
  - Distance (How to find range)

- Popularity
  - Total Views
  - Total Likes
  - Is Liked
  - Star Rating (based on 3 attributes)

- State Name

- Place Category Name
  - e.g., Historic (if PlaceCategoryName is empty, handle accordingly)

These search types and facets can be implemented to enhance the search capabilities of the Know India Tourist Places API.

## Objective :3 
> **Suggesting Business Use Cases**

|Usecase|Search Attributes|
| --- | ---|
|<p>Show **historic** places in **UK** |Image,video,title,state,city_name,geoLocation|
|Show **popular historic** places in **UK**|Image,video,title,state,city_name,geoLocation|
|Show **popular historic** places in UK **near me**|Image,video,title,state,city_name,geoLocation|


## Objective : 1
#### Analysis API Responses
- 1.2 Content Type : Knowindia - Accommodation

#### REQUEST URL = https://api.s3waas.gov.in/api/v1/getAccommodationList
```json
Request PayLoad
{
	"deviceID": "10E6B617-914F-4380-9C42-7393D0EB058D",
	"categoryId": "",
	"searchText":"",
	"stateId": "",
	"districtId": "",
	"pageIndex": "1",
	"recordPerpage": "10",
	"most_liked": "0",
	"most_viewed": "0",
	"language": "en",3149
	"ignore_id":"xtgePYUBvAOITNx4tmSY"
}
```
###

```json
Response 
{
  "resultFlag": 1,
  "message": "Detail Found",
  "totalRecords": 451,
  "pages": 46,
  "cache": 0,
  "data": [
    {
      "_index": "wheretostay",
      "_type": "_doc",
      "_id": "dtsMmYcBvAOITNx4Sroq",
      "_source": {
        "image": "https://cdn.s3waas.gov.in/s33416a75f4cea9109507cacd8e2f2aefc/uploads/2019/07/2019071823.jpg",
        "title": "The Urmi",
        "totalViews": 0,
        "totalLikes": 0,
        "isLiked": 0,
        "cityName": "Haridwar",
        "cityID": 491,
        "stateName": "Uttarakhand",
        "statecode": "UK",
        "stateID": 35,
        "placeCategoryName": [
          "Commercial",
          "Hotel"
        ],
        "placeCategoryID": [
          465,
          466
        ],
        "category": [
          {
            "id": 465,
            "category": "Commercial"
          }
        ],
        "subCategory": [
          {
            "id": 466,
            "category": "Hotel"
          }
        ],
        "content": "",
        "id": 27128,
        "imageList": {
          "title": "hotel-the-urmi-haridwar",
          "alt": "the-urmi-haridwar",
          "image": "https://cdn.s3waas.gov.in/s33416a75f4cea9109507cacd8e2f2aefc/uploads/2019/07/2019071823.jpg",
          "thumb_img_url": "https://cdn.s3waas.gov.in/s33416a75f4cea9109507cacd8e2f2aefc/uploads/2019/07/2019071823-150x150.jpg",
          "full_img_url": "https://cdn.s3waas.gov.in/s33416a75f4cea9109507cacd8e2f2aefc/uploads/2019/07/2019071823.jpg"
        },
        "siteurl": "https://haridwar.nic.in",
        "url": "https://haridwar.nic.in/accommodation/the-urmi/",
        "created_at": "2019-07-18T12:22:06",
        "updated_at": "2019-07-19T08:27:18",
        "email": "reservation@theurmi.com",
        "address": "Ganga Vihar Colony, Near Shantikunj, Bhupatwala, Haridwar",
        "phone": "8006005665",
        "website_link": "http://www.theurmi.com/",
        "pincode": "",
        "latitude": 0,
        "longitude": 0,
        "languages": [
          "en",
          "hi"
        ]
      }
    }
  ]
}
```
```
Total Records : 451
```






