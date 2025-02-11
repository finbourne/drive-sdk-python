# lusid_drive.FoldersApi

All URIs are relative to *https://fbn-prd.lusid.com/drive*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_folder**](FoldersApi.md#create_folder) | **POST** /api/folders | [EARLY ACCESS] CreateFolder: Create a new folder in LUSID Drive
[**delete_folder**](FoldersApi.md#delete_folder) | **DELETE** /api/folders/{id} | [EARLY ACCESS] DeleteFolder: Delete a specified folder and all subfolders
[**get_folder**](FoldersApi.md#get_folder) | **GET** /api/folders/{id} | [EARLY ACCESS] GetFolder: Get metadata of folder
[**get_folder_contents**](FoldersApi.md#get_folder_contents) | **GET** /api/folders/{id}/contents | GetFolderContents: List contents of a folder
[**get_root_folder**](FoldersApi.md#get_root_folder) | **GET** /api/folders | GetRootFolder: List contents of root folder
[**move_folder**](FoldersApi.md#move_folder) | **POST** /api/folders/{id} | [EARLY ACCESS] MoveFolder: Move files to specified folder
[**update_folder**](FoldersApi.md#update_folder) | **PUT** /api/folders/{id} | [EARLY ACCESS] UpdateFolder: Update an existing folder&#39;s name, path


# **create_folder**
> StorageObject create_folder(create_folder)

[EARLY ACCESS] CreateFolder: Create a new folder in LUSID Drive

### Example

```python
from lusid_drive.exceptions import ApiException
from lusid_drive.extensions.configuration_options import ConfigurationOptions
from lusid_drive.models import *
from pprint import pprint
from lusid_drive import (
    SyncApiClientFactory,
    FoldersApi
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
    api_instance = api_client_factory.build(FoldersApi)

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # create_folder = CreateFolder.from_json("")
    # create_folder = CreateFolder.from_dict({})
    create_folder = CreateFolder()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.create_folder(create_folder, opts=opts)

        # [EARLY ACCESS] CreateFolder: Create a new folder in LUSID Drive
        api_response = api_instance.create_folder(create_folder)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling FoldersApi->create_folder: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_folder** | [**CreateFolder**](CreateFolder.md)| A CreateFolder object that defines the name and path of the new folder | 

### Return type

[**StorageObject**](StorageObject.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **delete_folder**
> delete_folder(id)

[EARLY ACCESS] DeleteFolder: Delete a specified folder and all subfolders

### Example

```python
from lusid_drive.exceptions import ApiException
from lusid_drive.extensions.configuration_options import ConfigurationOptions
from lusid_drive.models import *
from pprint import pprint
from lusid_drive import (
    SyncApiClientFactory,
    FoldersApi
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
    api_instance = api_client_factory.build(FoldersApi)
    id = 'id_example' # str | Unique ID of the folder

    try:
        # uncomment the below to set overrides at the request level
        #  api_instance.delete_folder(id, opts=opts)

        # [EARLY ACCESS] DeleteFolder: Delete a specified folder and all subfolders
        api_instance.delete_folder(id)
    except ApiException as e:
        print("Exception when calling FoldersApi->delete_folder: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique ID of the folder | 

### Return type

void (empty response body)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | The details of the input related failure |  -  |
**404** | No folder with this Id exists |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_folder**
> StorageObject get_folder(id)

[EARLY ACCESS] GetFolder: Get metadata of folder

### Example

```python
from lusid_drive.exceptions import ApiException
from lusid_drive.extensions.configuration_options import ConfigurationOptions
from lusid_drive.models import *
from pprint import pprint
from lusid_drive import (
    SyncApiClientFactory,
    FoldersApi
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
    api_instance = api_client_factory.build(FoldersApi)
    id = 'id_example' # str | Unique ID of the folder

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_folder(id, opts=opts)

        # [EARLY ACCESS] GetFolder: Get metadata of folder
        api_response = api_instance.get_folder(id)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling FoldersApi->get_folder: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique ID of the folder | 

### Return type

[**StorageObject**](StorageObject.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**404** | No folder with this Id exists |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_folder_contents**
> PagedResourceListOfStorageObject get_folder_contents(id, page=page, sort_by=sort_by, start=start, limit=limit, filter=filter)

GetFolderContents: List contents of a folder

### Example

```python
from lusid_drive.exceptions import ApiException
from lusid_drive.extensions.configuration_options import ConfigurationOptions
from lusid_drive.models import *
from pprint import pprint
from lusid_drive import (
    SyncApiClientFactory,
    FoldersApi
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
    api_instance = api_client_factory.build(FoldersApi)
    id = 'id_example' # str | Unique ID of the folder
    page = 'page_example' # str | The pagination token to use to continue listing contents from a previous call to list contents.              This value is returned from the previous call. If a pagination token is provided the sortBy and filter fields              must not have changed since the original request. Also, if set, a start value cannot be provided. (optional)
    sort_by = ['sort_by_example'] # List[str] | Order the results by these fields. Use use the '-' sign to denote descending order. (optional)
    start = 56 # int | When paginating, skip this number of results. (optional)
    limit = 56 # int | When paginating, limit the number of returned results to this many. (optional)
    filter = '' # str | Expression to filter the result set. (optional) (default to '')

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_folder_contents(id, page=page, sort_by=sort_by, start=start, limit=limit, filter=filter, opts=opts)

        # GetFolderContents: List contents of a folder
        api_response = api_instance.get_folder_contents(id, page=page, sort_by=sort_by, start=start, limit=limit, filter=filter)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling FoldersApi->get_folder_contents: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique ID of the folder | 
 **page** | **str**| The pagination token to use to continue listing contents from a previous call to list contents.              This value is returned from the previous call. If a pagination token is provided the sortBy and filter fields              must not have changed since the original request. Also, if set, a start value cannot be provided. | [optional] 
 **sort_by** | [**List[str]**](str.md)| Order the results by these fields. Use use the &#39;-&#39; sign to denote descending order. | [optional] 
 **start** | **int**| When paginating, skip this number of results. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. | [optional] 
 **filter** | **str**| Expression to filter the result set. | [optional] [default to &#39;&#39;]

### Return type

[**PagedResourceListOfStorageObject**](PagedResourceListOfStorageObject.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**404** | No folder with this Id exists |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_root_folder**
> PagedResourceListOfStorageObject get_root_folder(page=page, sort_by=sort_by, start=start, limit=limit, filter=filter)

GetRootFolder: List contents of root folder

### Example

```python
from lusid_drive.exceptions import ApiException
from lusid_drive.extensions.configuration_options import ConfigurationOptions
from lusid_drive.models import *
from pprint import pprint
from lusid_drive import (
    SyncApiClientFactory,
    FoldersApi
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
    api_instance = api_client_factory.build(FoldersApi)
    page = 'page_example' # str | The pagination token to use to continue listing contents from a previous call to list contents.              This value is returned from the previous call. If a pagination token is provided the sortBy and filter fields              must not have changed since the original request. Also, if set, a start value cannot be provided. (optional)
    sort_by = ['sort_by_example'] # List[str] | Order the results by these fields. Use use the '-' sign to denote descending order. (optional)
    start = 56 # int | When paginating, skip this number of results. (optional)
    limit = 56 # int | When paginating, limit the number of returned results to this many. (optional)
    filter = 'true' # str | Expression to filter the result set. (optional) (default to 'true')

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_root_folder(page=page, sort_by=sort_by, start=start, limit=limit, filter=filter, opts=opts)

        # GetRootFolder: List contents of root folder
        api_response = api_instance.get_root_folder(page=page, sort_by=sort_by, start=start, limit=limit, filter=filter)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling FoldersApi->get_root_folder: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **str**| The pagination token to use to continue listing contents from a previous call to list contents.              This value is returned from the previous call. If a pagination token is provided the sortBy and filter fields              must not have changed since the original request. Also, if set, a start value cannot be provided. | [optional] 
 **sort_by** | [**List[str]**](str.md)| Order the results by these fields. Use use the &#39;-&#39; sign to denote descending order. | [optional] 
 **start** | **int**| When paginating, skip this number of results. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. | [optional] 
 **filter** | **str**| Expression to filter the result set. | [optional] [default to &#39;true&#39;]

### Return type

[**PagedResourceListOfStorageObject**](PagedResourceListOfStorageObject.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **move_folder**
> PagedResourceListOfStorageObject move_folder(id, request_body, overwrite=overwrite, delete_source=delete_source)

[EARLY ACCESS] MoveFolder: Move files to specified folder

### Example

```python
from lusid_drive.exceptions import ApiException
from lusid_drive.extensions.configuration_options import ConfigurationOptions
from lusid_drive.models import *
from pprint import pprint
from lusid_drive import (
    SyncApiClientFactory,
    FoldersApi
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
    api_instance = api_client_factory.build(FoldersApi)
    id = 'id_example' # str | Unique ID of the folder where the files should be moved
    request_body = ["FolderID1","FolderID2","FolderID3"] # List[str] | Enumerable of unique IDs of files that should be moved
    overwrite = False # bool | True if the destination has file with same name if should be overwritten (optional) (default to False)
    delete_source = False # bool | If true after moving the original file is deleted (optional) (default to False)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.move_folder(id, request_body, overwrite=overwrite, delete_source=delete_source, opts=opts)

        # [EARLY ACCESS] MoveFolder: Move files to specified folder
        api_response = api_instance.move_folder(id, request_body, overwrite=overwrite, delete_source=delete_source)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling FoldersApi->move_folder: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique ID of the folder where the files should be moved | 
 **request_body** | [**List[str]**](str.md)| Enumerable of unique IDs of files that should be moved | 
 **overwrite** | **bool**| True if the destination has file with same name if should be overwritten | [optional] [default to False]
 **delete_source** | **bool**| If true after moving the original file is deleted | [optional] [default to False]

### Return type

[**PagedResourceListOfStorageObject**](PagedResourceListOfStorageObject.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**404** | No folder or file with the supplied Id exists |  -  |
**409** | There is already a file with the same name at this location |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **update_folder**
> StorageObject update_folder(id, update_folder)

[EARLY ACCESS] UpdateFolder: Update an existing folder's name, path

### Example

```python
from lusid_drive.exceptions import ApiException
from lusid_drive.extensions.configuration_options import ConfigurationOptions
from lusid_drive.models import *
from pprint import pprint
from lusid_drive import (
    SyncApiClientFactory,
    FoldersApi
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
    api_instance = api_client_factory.build(FoldersApi)
    id = 'id_example' # str | Unique ID of the folder

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # update_folder = UpdateFolder.from_json("")
    # update_folder = UpdateFolder.from_dict({})
    update_folder = UpdateFolder()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.update_folder(id, update_folder, opts=opts)

        # [EARLY ACCESS] UpdateFolder: Update an existing folder's name, path
        api_response = api_instance.update_folder(id, update_folder)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling FoldersApi->update_folder: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique ID of the folder | 
 **update_folder** | [**UpdateFolder**](UpdateFolder.md)| An UpdateFolder object that defines the new name or path of the folder | 

### Return type

[**StorageObject**](StorageObject.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**404** | No folder with this Id exists |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

