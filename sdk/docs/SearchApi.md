# lusid_drive.SearchApi

All URIs are relative to *https://fbn-prd.lusid.com/drive*

Method | HTTP request | Description
------------- | ------------- | -------------
[**search**](SearchApi.md#search) | **POST** /api/search | [EARLY ACCESS] Search: Search for a file or folder with a given name and path


# **search**
> PagedResourceListOfStorageObject search(search_body, page=page, sort_by=sort_by, limit=limit, filter=filter)

[EARLY ACCESS] Search: Search for a file or folder with a given name and path

### Example

```python
from lusid_drive.exceptions import ApiException
from lusid_drive.extensions.configuration_options import ConfigurationOptions
from lusid_drive.models import *
from pprint import pprint
from lusid_drive import (
    SyncApiClientFactory,
    SearchApi
)

def main():

    with open("secrets.json", "w") as file:
        file.write('''
    {
        "api":
        {
            "tokenUrl":"<your-token-url>",
            "driveUrl":"https://<your-domain>.lusid.com/drive",
            "username":"<your-username>",
            "password":"<your-password>",
            "clientId":"<your-client-id>",
            "clientSecret":"<your-client-secret>"
        }
    }''')

    # Use the lusid_drive SyncApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = SyncApiClientFactory(opts=opts)

    api_client_factory = SyncApiClientFactory()

    # Enter a context with an instance of the SyncApiClientFactory to ensure the connection pool is closed after use
    
    # Create an instance of the API class
    api_instance = api_client_factory.build(SearchApi)

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # search_body = SearchBody.from_json("")
    # search_body = SearchBody.from_dict({})
    search_body = SearchBody()
    page = 'page_example' # str |  (optional)
    sort_by = ['sort_by_example'] # List[str] |  (optional)
    limit = 56 # int |  (optional)
    filter = '' # str |  (optional) (default to '')

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.search(search_body, page=page, sort_by=sort_by, limit=limit, filter=filter, opts=opts)

        # [EARLY ACCESS] Search: Search for a file or folder with a given name and path
        api_response = api_instance.search(search_body, page=page, sort_by=sort_by, limit=limit, filter=filter)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling SearchApi->search: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_body** | [**SearchBody**](SearchBody.md)| Search parameters | 
 **page** | **str**|  | [optional] 
 **sort_by** | [**List[str]**](str.md)|  | [optional] 
 **limit** | **int**|  | [optional] 
 **filter** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

[**PagedResourceListOfStorageObject**](PagedResourceListOfStorageObject.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

