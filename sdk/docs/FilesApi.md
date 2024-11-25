# lusid_drive.FilesApi

All URIs are relative to *https://fbn-prd.lusid.com/drive*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_file**](FilesApi.md#create_file) | **POST** /api/files | CreateFile: Uploads a file to Lusid Drive. If using an SDK, consider using the UploadAsStreamAsync function for larger files instead.
[**delete_file**](FilesApi.md#delete_file) | **DELETE** /api/files/{id} | [EARLY ACCESS] DeleteFile: Deletes a file from Drive.
[**download_file**](FilesApi.md#download_file) | **GET** /api/files/{id}/contents | DownloadFile: Download the file from Drive.
[**get_file**](FilesApi.md#get_file) | **GET** /api/files/{id} | [EARLY ACCESS] GetFile: Get a file stored in Drive.
[**update_file_contents**](FilesApi.md#update_file_contents) | **PUT** /api/files/{id}/contents | [EARLY ACCESS] UpdateFileContents: Updates contents of a file in Drive.
[**update_file_metadata**](FilesApi.md#update_file_metadata) | **PUT** /api/files/{id} | [EARLY ACCESS] UpdateFileMetadata: Updates metadata for a file in Drive.


# **create_file**
> StorageObject create_file(x_lusid_drive_filename, x_lusid_drive_path, content_length, body)

CreateFile: Uploads a file to Lusid Drive. If using an SDK, consider using the UploadAsStreamAsync function for larger files instead.

### Example

```python
from lusid_drive.exceptions import ApiException
from lusid_drive.extensions.configuration_options import ConfigurationOptions
from lusid_drive.models import *
from pprint import pprint
from lusid_drive import (
    SyncApiClientFactory,
    FilesApi
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
    api_instance = api_client_factory.build(FilesApi)
    x_lusid_drive_filename = 'x_lusid_drive_filename_example' # str | File name.
    x_lusid_drive_path = 'x_lusid_drive_path_example' # str | File path.
    content_length = 56 # int | The size in bytes of the file to be uploaded
    body = None # bytearray | 

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.create_file(x_lusid_drive_filename, x_lusid_drive_path, content_length, body, opts=opts)

        # CreateFile: Uploads a file to Lusid Drive. If using an SDK, consider using the UploadAsStreamAsync function for larger files instead.
        api_response = api_instance.create_file(x_lusid_drive_filename, x_lusid_drive_path, content_length, body)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling FilesApi->create_file: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_lusid_drive_filename** | **str**| File name. | 
 **x_lusid_drive_path** | **str**| File path. | 
 **content_length** | **int**| The size in bytes of the file to be uploaded | 
 **body** | **bytearray**|  | 

### Return type

[**StorageObject**](StorageObject.md)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **delete_file**
> delete_file(id)

[EARLY ACCESS] DeleteFile: Deletes a file from Drive.

### Example

```python
from lusid_drive.exceptions import ApiException
from lusid_drive.extensions.configuration_options import ConfigurationOptions
from lusid_drive.models import *
from pprint import pprint
from lusid_drive import (
    SyncApiClientFactory,
    FilesApi
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
    api_instance = api_client_factory.build(FilesApi)
    id = 'id_example' # str | Identifier of the file to be deleted.

    try:
        # uncomment the below to set overrides at the request level
        #  api_instance.delete_file(id, opts=opts)

        # [EARLY ACCESS] DeleteFile: Deletes a file from Drive.
        api_instance.delete_file(id)
    except ApiException as e:
        print("Exception when calling FilesApi->delete_file: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the file to be deleted. | 

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
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **download_file**
> bytearray download_file(id)

DownloadFile: Download the file from Drive.

### Example

```python
from lusid_drive.exceptions import ApiException
from lusid_drive.extensions.configuration_options import ConfigurationOptions
from lusid_drive.models import *
from pprint import pprint
from lusid_drive import (
    SyncApiClientFactory,
    FilesApi
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
    api_instance = api_client_factory.build(FilesApi)
    id = 'id_example' # str | Identifier of the file to be downloaded.

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.download_file(id, opts=opts)

        # DownloadFile: Download the file from Drive.
        api_response = api_instance.download_file(id)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling FilesApi->download_file: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the file to be downloaded. | 

### Return type

**bytearray**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**410** | Malware detected, restricted from downloading file. |  -  |
**423** | Virus scan in progress, restricted from downloading file. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_file**
> StorageObject get_file(id)

[EARLY ACCESS] GetFile: Get a file stored in Drive.

### Example

```python
from lusid_drive.exceptions import ApiException
from lusid_drive.extensions.configuration_options import ConfigurationOptions
from lusid_drive.models import *
from pprint import pprint
from lusid_drive import (
    SyncApiClientFactory,
    FilesApi
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
    api_instance = api_client_factory.build(FilesApi)
    id = 'id_example' # str | Identifier of the file to be retrieved.

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_file(id, opts=opts)

        # [EARLY ACCESS] GetFile: Get a file stored in Drive.
        api_response = api_instance.get_file(id)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling FilesApi->get_file: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the file to be retrieved. | 

### Return type

[**StorageObject**](StorageObject.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **update_file_contents**
> StorageObject update_file_contents(id, content_length, body)

[EARLY ACCESS] UpdateFileContents: Updates contents of a file in Drive.

### Example

```python
from lusid_drive.exceptions import ApiException
from lusid_drive.extensions.configuration_options import ConfigurationOptions
from lusid_drive.models import *
from pprint import pprint
from lusid_drive import (
    SyncApiClientFactory,
    FilesApi
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
    api_instance = api_client_factory.build(FilesApi)
    id = 'id_example' # str | The unique file identifier
    content_length = 56 # int | The size in bytes of the file to be uploaded
    body = None # bytearray | 

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.update_file_contents(id, content_length, body, opts=opts)

        # [EARLY ACCESS] UpdateFileContents: Updates contents of a file in Drive.
        api_response = api_instance.update_file_contents(id, content_length, body)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling FilesApi->update_file_contents: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique file identifier | 
 **content_length** | **int**| The size in bytes of the file to be uploaded | 
 **body** | **bytearray**|  | 

### Return type

[**StorageObject**](StorageObject.md)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **update_file_metadata**
> StorageObject update_file_metadata(id, update_file)

[EARLY ACCESS] UpdateFileMetadata: Updates metadata for a file in Drive.

### Example

```python
from lusid_drive.exceptions import ApiException
from lusid_drive.extensions.configuration_options import ConfigurationOptions
from lusid_drive.models import *
from pprint import pprint
from lusid_drive import (
    SyncApiClientFactory,
    FilesApi
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
    api_instance = api_client_factory.build(FilesApi)
    id = 'id_example' # str | Identifier of the file to be updated

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # update_file = UpdateFile.from_json("")
    # update_file = UpdateFile.from_dict({})
    update_file = UpdateFile()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.update_file_metadata(id, update_file, opts=opts)

        # [EARLY ACCESS] UpdateFileMetadata: Updates metadata for a file in Drive.
        api_response = api_instance.update_file_metadata(id, update_file)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling FilesApi->update_file_metadata: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the file to be updated | 
 **update_file** | [**UpdateFile**](UpdateFile.md)| Update to be applied to file | 

### Return type

[**StorageObject**](StorageObject.md)

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

