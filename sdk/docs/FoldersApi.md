# lusid_drive.FoldersApi

All URIs are relative to *https://fbn-prd.lusid.com/drive*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_folder**](FoldersApi.md#create_folder) | **POST** /api/folders | [EARLY ACCESS] CreateFolder: Create a new folder in LUSID Drive
[**delete_folder**](FoldersApi.md#delete_folder) | **DELETE** /api/folders/{id} | [EARLY ACCESS] DeleteFolder: Delete a specified folder and all subfolders
[**get_folder**](FoldersApi.md#get_folder) | **GET** /api/folders/{id} | [EARLY ACCESS] GetFolder: Get metadata of folder
[**get_folder_contents**](FoldersApi.md#get_folder_contents) | **GET** /api/folders/{id}/contents | [EARLY ACCESS] GetFolderContents: List contents of a folder
[**get_root_folder**](FoldersApi.md#get_root_folder) | **GET** /api/folders | [EARLY ACCESS] GetRootFolder: List contents of root folder
[**move_folder**](FoldersApi.md#move_folder) | **POST** /api/folders/{id} | [EARLY ACCESS] MoveFolder: Move files to specified folder
[**update_folder**](FoldersApi.md#update_folder) | **PUT** /api/folders/{id} | [EARLY ACCESS] UpdateFolder: Update an existing folder&#39;s name, path


# **create_folder**
> StorageObject create_folder(create_folder)

[EARLY ACCESS] CreateFolder: Create a new folder in LUSID Drive

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid_drive
from lusid_drive.rest import ApiException
from lusid_drive.models.create_folder import CreateFolder
from lusid_drive.models.storage_object import StorageObject
from pprint import pprint

import os
from lusid_drive import (
    ApiClientFactory,
    FoldersApi,
    EnvironmentVariablesConfigurationLoader,
    SecretsFileConfigurationLoader,
    ArgsConfigurationLoader
)

# Use the lusid_drive ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://fbn-prd.lusid.com/drive"
# Path to a secrets.json file containing authentication credentials
# See https://support.lusid.com/knowledgebase/article/KA-01667/en-us
# for a detailed guide to setting up the SDK make authenticated calls to LUSID APIs
secrets_path = os.getenv("FBN_SECRETS_PATH")
app_name="LusidJupyterNotebook"

config_loaders = [
	EnvironmentVariablesConfigurationLoader(),
	SecretsFileConfigurationLoader(api_secrets_file=secrets_path),
	ArgsConfigurationLoader(api_url=api_url, app_name=app_name)
]
api_client_factory = ApiClientFactory(config_loaders=config_loaders)


# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.



# Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
async with api_client_factory:
    # Create an instance of the API class
    api_instance = api_client_factory.build(lusid_drive.FoldersApi)
    create_folder = {"path":"/path/to/saveTo/","name":"folderName"} # CreateFolder | A CreateFolder object that defines the name and path of the new folder

    try:
        # [EARLY ACCESS] CreateFolder: Create a new folder in LUSID Drive
        api_response = await api_instance.create_folder(create_folder)
        print("The response of FoldersApi->create_folder:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FoldersApi->create_folder: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_folder** | [**CreateFolder**](CreateFolder.md)| A CreateFolder object that defines the name and path of the new folder | 

### Return type

[**StorageObject**](StorageObject.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_folder**
> delete_folder(id)

[EARLY ACCESS] DeleteFolder: Delete a specified folder and all subfolders

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid_drive
from lusid_drive.rest import ApiException
from pprint import pprint

import os
from lusid_drive import (
    ApiClientFactory,
    FoldersApi,
    EnvironmentVariablesConfigurationLoader,
    SecretsFileConfigurationLoader,
    ArgsConfigurationLoader
)

# Use the lusid_drive ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://fbn-prd.lusid.com/drive"
# Path to a secrets.json file containing authentication credentials
# See https://support.lusid.com/knowledgebase/article/KA-01667/en-us
# for a detailed guide to setting up the SDK make authenticated calls to LUSID APIs
secrets_path = os.getenv("FBN_SECRETS_PATH")
app_name="LusidJupyterNotebook"

config_loaders = [
	EnvironmentVariablesConfigurationLoader(),
	SecretsFileConfigurationLoader(api_secrets_file=secrets_path),
	ArgsConfigurationLoader(api_url=api_url, app_name=app_name)
]
api_client_factory = ApiClientFactory(config_loaders=config_loaders)


# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.



# Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
async with api_client_factory:
    # Create an instance of the API class
    api_instance = api_client_factory.build(lusid_drive.FoldersApi)
    id = 'id_example' # str | Unique ID of the folder

    try:
        # [EARLY ACCESS] DeleteFolder: Delete a specified folder and all subfolders
        await api_instance.delete_folder(id)
    except Exception as e:
        print("Exception when calling FoldersApi->delete_folder: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique ID of the folder | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_folder**
> StorageObject get_folder(id)

[EARLY ACCESS] GetFolder: Get metadata of folder

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid_drive
from lusid_drive.rest import ApiException
from lusid_drive.models.storage_object import StorageObject
from pprint import pprint

import os
from lusid_drive import (
    ApiClientFactory,
    FoldersApi,
    EnvironmentVariablesConfigurationLoader,
    SecretsFileConfigurationLoader,
    ArgsConfigurationLoader
)

# Use the lusid_drive ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://fbn-prd.lusid.com/drive"
# Path to a secrets.json file containing authentication credentials
# See https://support.lusid.com/knowledgebase/article/KA-01667/en-us
# for a detailed guide to setting up the SDK make authenticated calls to LUSID APIs
secrets_path = os.getenv("FBN_SECRETS_PATH")
app_name="LusidJupyterNotebook"

config_loaders = [
	EnvironmentVariablesConfigurationLoader(),
	SecretsFileConfigurationLoader(api_secrets_file=secrets_path),
	ArgsConfigurationLoader(api_url=api_url, app_name=app_name)
]
api_client_factory = ApiClientFactory(config_loaders=config_loaders)


# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.



# Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
async with api_client_factory:
    # Create an instance of the API class
    api_instance = api_client_factory.build(lusid_drive.FoldersApi)
    id = 'id_example' # str | Unique ID of the folder

    try:
        # [EARLY ACCESS] GetFolder: Get metadata of folder
        api_response = await api_instance.get_folder(id)
        print("The response of FoldersApi->get_folder:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FoldersApi->get_folder: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique ID of the folder | 

### Return type

[**StorageObject**](StorageObject.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**404** | No folder with this Id exists |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_folder_contents**
> PagedResourceListOfStorageObject get_folder_contents(id, page=page, sort_by=sort_by, start=start, limit=limit, filter=filter)

[EARLY ACCESS] GetFolderContents: List contents of a folder

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid_drive
from lusid_drive.rest import ApiException
from lusid_drive.models.paged_resource_list_of_storage_object import PagedResourceListOfStorageObject
from pprint import pprint

import os
from lusid_drive import (
    ApiClientFactory,
    FoldersApi,
    EnvironmentVariablesConfigurationLoader,
    SecretsFileConfigurationLoader,
    ArgsConfigurationLoader
)

# Use the lusid_drive ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://fbn-prd.lusid.com/drive"
# Path to a secrets.json file containing authentication credentials
# See https://support.lusid.com/knowledgebase/article/KA-01667/en-us
# for a detailed guide to setting up the SDK make authenticated calls to LUSID APIs
secrets_path = os.getenv("FBN_SECRETS_PATH")
app_name="LusidJupyterNotebook"

config_loaders = [
	EnvironmentVariablesConfigurationLoader(),
	SecretsFileConfigurationLoader(api_secrets_file=secrets_path),
	ArgsConfigurationLoader(api_url=api_url, app_name=app_name)
]
api_client_factory = ApiClientFactory(config_loaders=config_loaders)


# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.



# Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
async with api_client_factory:
    # Create an instance of the API class
    api_instance = api_client_factory.build(lusid_drive.FoldersApi)
    id = 'id_example' # str | Unique ID of the folder
    page = 'page_example' # str | The pagination token to use to continue listing contents from a previous call to list contents.              This value is returned from the previous call. If a pagination token is provided the sortBy and filter fields              must not have changed since the original request. Also, if set, a start value cannot be provided. (optional)
    sort_by = ['sort_by_example'] # List[str] | Order the results by these fields. Use use the '-' sign to denote descending order. (optional)
    start = 56 # int | When paginating, skip this number of results. (optional)
    limit = 56 # int | When paginating, limit the number of returned results to this many. (optional)
    filter = '' # str | Expression to filter the result set. (optional) (default to '')

    try:
        # [EARLY ACCESS] GetFolderContents: List contents of a folder
        api_response = await api_instance.get_folder_contents(id, page=page, sort_by=sort_by, start=start, limit=limit, filter=filter)
        print("The response of FoldersApi->get_folder_contents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FoldersApi->get_folder_contents: %s\n" % e)
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

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**404** | No folder with this Id exists |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_root_folder**
> PagedResourceListOfStorageObject get_root_folder(page=page, sort_by=sort_by, start=start, limit=limit, filter=filter)

[EARLY ACCESS] GetRootFolder: List contents of root folder

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid_drive
from lusid_drive.rest import ApiException
from lusid_drive.models.paged_resource_list_of_storage_object import PagedResourceListOfStorageObject
from pprint import pprint

import os
from lusid_drive import (
    ApiClientFactory,
    FoldersApi,
    EnvironmentVariablesConfigurationLoader,
    SecretsFileConfigurationLoader,
    ArgsConfigurationLoader
)

# Use the lusid_drive ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://fbn-prd.lusid.com/drive"
# Path to a secrets.json file containing authentication credentials
# See https://support.lusid.com/knowledgebase/article/KA-01667/en-us
# for a detailed guide to setting up the SDK make authenticated calls to LUSID APIs
secrets_path = os.getenv("FBN_SECRETS_PATH")
app_name="LusidJupyterNotebook"

config_loaders = [
	EnvironmentVariablesConfigurationLoader(),
	SecretsFileConfigurationLoader(api_secrets_file=secrets_path),
	ArgsConfigurationLoader(api_url=api_url, app_name=app_name)
]
api_client_factory = ApiClientFactory(config_loaders=config_loaders)


# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.



# Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
async with api_client_factory:
    # Create an instance of the API class
    api_instance = api_client_factory.build(lusid_drive.FoldersApi)
    page = 'page_example' # str | The pagination token to use to continue listing contents from a previous call to list contents.              This value is returned from the previous call. If a pagination token is provided the sortBy and filter fields              must not have changed since the original request. Also, if set, a start value cannot be provided. (optional)
    sort_by = ['sort_by_example'] # List[str] | Order the results by these fields. Use use the '-' sign to denote descending order. (optional)
    start = 56 # int | When paginating, skip this number of results. (optional)
    limit = 56 # int | When paginating, limit the number of returned results to this many. (optional)
    filter = 'true' # str | Expression to filter the result set. (optional) (default to 'true')

    try:
        # [EARLY ACCESS] GetRootFolder: List contents of root folder
        api_response = await api_instance.get_root_folder(page=page, sort_by=sort_by, start=start, limit=limit, filter=filter)
        print("The response of FoldersApi->get_root_folder:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FoldersApi->get_root_folder: %s\n" % e)
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

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **move_folder**
> PagedResourceListOfStorageObject move_folder(id, request_body, overwrite=overwrite, delete_source=delete_source)

[EARLY ACCESS] MoveFolder: Move files to specified folder

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid_drive
from lusid_drive.rest import ApiException
from lusid_drive.models.paged_resource_list_of_storage_object import PagedResourceListOfStorageObject
from pprint import pprint

import os
from lusid_drive import (
    ApiClientFactory,
    FoldersApi,
    EnvironmentVariablesConfigurationLoader,
    SecretsFileConfigurationLoader,
    ArgsConfigurationLoader
)

# Use the lusid_drive ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://fbn-prd.lusid.com/drive"
# Path to a secrets.json file containing authentication credentials
# See https://support.lusid.com/knowledgebase/article/KA-01667/en-us
# for a detailed guide to setting up the SDK make authenticated calls to LUSID APIs
secrets_path = os.getenv("FBN_SECRETS_PATH")
app_name="LusidJupyterNotebook"

config_loaders = [
	EnvironmentVariablesConfigurationLoader(),
	SecretsFileConfigurationLoader(api_secrets_file=secrets_path),
	ArgsConfigurationLoader(api_url=api_url, app_name=app_name)
]
api_client_factory = ApiClientFactory(config_loaders=config_loaders)


# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.



# Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
async with api_client_factory:
    # Create an instance of the API class
    api_instance = api_client_factory.build(lusid_drive.FoldersApi)
    id = 'id_example' # str | Unique ID of the folder where the files should be moved
    request_body = ["FolderID1","FolderID2","FolderID3"] # List[str] | Enumerable of unique IDs of files that should be moved
    overwrite = False # bool | True if the destination has file with same name if should be overwritten (optional) (default to False)
    delete_source = False # bool | If true after moving the original file is deleted (optional) (default to False)

    try:
        # [EARLY ACCESS] MoveFolder: Move files to specified folder
        api_response = await api_instance.move_folder(id, request_body, overwrite=overwrite, delete_source=delete_source)
        print("The response of FoldersApi->move_folder:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FoldersApi->move_folder: %s\n" % e)
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

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**404** | No folder or file with the supplied Id exists |  -  |
**409** | There is already a file with the same name at this location |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_folder**
> StorageObject update_folder(id, update_folder)

[EARLY ACCESS] UpdateFolder: Update an existing folder's name, path

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid_drive
from lusid_drive.rest import ApiException
from lusid_drive.models.storage_object import StorageObject
from lusid_drive.models.update_folder import UpdateFolder
from pprint import pprint

import os
from lusid_drive import (
    ApiClientFactory,
    FoldersApi,
    EnvironmentVariablesConfigurationLoader,
    SecretsFileConfigurationLoader,
    ArgsConfigurationLoader
)

# Use the lusid_drive ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://fbn-prd.lusid.com/drive"
# Path to a secrets.json file containing authentication credentials
# See https://support.lusid.com/knowledgebase/article/KA-01667/en-us
# for a detailed guide to setting up the SDK make authenticated calls to LUSID APIs
secrets_path = os.getenv("FBN_SECRETS_PATH")
app_name="LusidJupyterNotebook"

config_loaders = [
	EnvironmentVariablesConfigurationLoader(),
	SecretsFileConfigurationLoader(api_secrets_file=secrets_path),
	ArgsConfigurationLoader(api_url=api_url, app_name=app_name)
]
api_client_factory = ApiClientFactory(config_loaders=config_loaders)


# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.



# Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
async with api_client_factory:
    # Create an instance of the API class
    api_instance = api_client_factory.build(lusid_drive.FoldersApi)
    id = 'id_example' # str | Unique ID of the folder
    update_folder = {"path":"/Documents/Common/Legal/","name":"FolderName"} # UpdateFolder | An UpdateFolder object that defines the new name or path of the folder

    try:
        # [EARLY ACCESS] UpdateFolder: Update an existing folder's name, path
        api_response = await api_instance.update_folder(id, update_folder)
        print("The response of FoldersApi->update_folder:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FoldersApi->update_folder: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique ID of the folder | 
 **update_folder** | [**UpdateFolder**](UpdateFolder.md)| An UpdateFolder object that defines the new name or path of the folder | 

### Return type

[**StorageObject**](StorageObject.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**404** | No folder with this Id exists |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

