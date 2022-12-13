# thirdeye_client.DataSourceApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clear_data_source_cache**](DataSourceApi.md#clear_data_source_cache) | **DELETE** /api/data-sources/cache | 
[**count_with_predicate**](DataSourceApi.md#count_with_predicate) | **GET** /api/data-sources/count | 
[**create_multiple**](DataSourceApi.md#create_multiple) | **POST** /api/data-sources | 
[**delete**](DataSourceApi.md#delete) | **DELETE** /api/data-sources/{id} | 
[**delete_all**](DataSourceApi.md#delete_all) | **DELETE** /api/data-sources/all | 
[**edit_multiple**](DataSourceApi.md#edit_multiple) | **PUT** /api/data-sources | 
[**get1**](DataSourceApi.md#get1) | **GET** /api/data-sources/{id} | 
[**get2**](DataSourceApi.md#get2) | **GET** /api/data-sources/name/{name} | 
[**get_all**](DataSourceApi.md#get_all) | **GET** /api/data-sources | 
[**get_datasets**](DataSourceApi.md#get_datasets) | **GET** /api/data-sources/name/{name}/datasets | 
[**offboard_all**](DataSourceApi.md#offboard_all) | **DELETE** /api/data-sources/offboard-all | 
[**onboard_all**](DataSourceApi.md#onboard_all) | **POST** /api/data-sources/onboard-all | 
[**onboard_dataset**](DataSourceApi.md#onboard_dataset) | **POST** /api/data-sources/onboard-dataset | 
[**validate**](DataSourceApi.md#validate) | **GET** /api/data-sources/validate | 


# **clear_data_source_cache**
> clear_data_source_cache()



### Example
```python
from __future__ import print_function
import time
import thirdeye_client
from thirdeye_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: oauth
configuration = thirdeye_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = thirdeye_client.DataSourceApi(thirdeye_client.ApiClient(configuration))

try:
    api_instance.clear_data_source_cache()
except ApiException as e:
    print("Exception when calling DataSourceApi->clear_data_source_cache: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **count_with_predicate**
> count_with_predicate()



### Example
```python
from __future__ import print_function
import time
import thirdeye_client
from thirdeye_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: oauth
configuration = thirdeye_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = thirdeye_client.DataSourceApi(thirdeye_client.ApiClient(configuration))

try:
    api_instance.count_with_predicate()
except ApiException as e:
    print("Exception when calling DataSourceApi->count_with_predicate: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_multiple**
> create_multiple(body=body)



### Example
```python
from __future__ import print_function
import time
import thirdeye_client
from thirdeye_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: oauth
configuration = thirdeye_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = thirdeye_client.DataSourceApi(thirdeye_client.ApiClient(configuration))
body = [thirdeye_client.DataSourceApiModel()] # list[DataSourceApiModel] |  (optional)

try:
    api_instance.create_multiple(body=body)
except ApiException as e:
    print("Exception when calling DataSourceApi->create_multiple: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[DataSourceApiModel]**](DataSourceApiModel.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> delete(id)



### Example
```python
from __future__ import print_function
import time
import thirdeye_client
from thirdeye_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: oauth
configuration = thirdeye_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = thirdeye_client.DataSourceApi(thirdeye_client.ApiClient(configuration))
id = 789 # int | 

try:
    api_instance.delete(id)
except ApiException as e:
    print("Exception when calling DataSourceApi->delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_all**
> delete_all()



### Example
```python
from __future__ import print_function
import time
import thirdeye_client
from thirdeye_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: oauth
configuration = thirdeye_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = thirdeye_client.DataSourceApi(thirdeye_client.ApiClient(configuration))

try:
    api_instance.delete_all()
except ApiException as e:
    print("Exception when calling DataSourceApi->delete_all: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_multiple**
> edit_multiple(body=body)



### Example
```python
from __future__ import print_function
import time
import thirdeye_client
from thirdeye_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: oauth
configuration = thirdeye_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = thirdeye_client.DataSourceApi(thirdeye_client.ApiClient(configuration))
body = [thirdeye_client.DataSourceApiModel()] # list[DataSourceApiModel] |  (optional)

try:
    api_instance.edit_multiple(body=body)
except ApiException as e:
    print("Exception when calling DataSourceApi->edit_multiple: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[DataSourceApiModel]**](DataSourceApiModel.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get1**
> get1(id)



### Example
```python
from __future__ import print_function
import time
import thirdeye_client
from thirdeye_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: oauth
configuration = thirdeye_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = thirdeye_client.DataSourceApi(thirdeye_client.ApiClient(configuration))
id = 789 # int | 

try:
    api_instance.get1(id)
except ApiException as e:
    print("Exception when calling DataSourceApi->get1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get2**
> get2(name)



### Example
```python
from __future__ import print_function
import time
import thirdeye_client
from thirdeye_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: oauth
configuration = thirdeye_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = thirdeye_client.DataSourceApi(thirdeye_client.ApiClient(configuration))
name = 'name_example' # str | 

try:
    api_instance.get2(name)
except ApiException as e:
    print("Exception when calling DataSourceApi->get2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all**
> get_all()



### Example
```python
from __future__ import print_function
import time
import thirdeye_client
from thirdeye_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: oauth
configuration = thirdeye_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = thirdeye_client.DataSourceApi(thirdeye_client.ApiClient(configuration))

try:
    api_instance.get_all()
except ApiException as e:
    print("Exception when calling DataSourceApi->get_all: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_datasets**
> get_datasets(name)



### Example
```python
from __future__ import print_function
import time
import thirdeye_client
from thirdeye_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: oauth
configuration = thirdeye_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = thirdeye_client.DataSourceApi(thirdeye_client.ApiClient(configuration))
name = 'name_example' # str | 

try:
    api_instance.get_datasets(name)
except ApiException as e:
    print("Exception when calling DataSourceApi->get_datasets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **offboard_all**
> offboard_all(name=name)



### Example
```python
from __future__ import print_function
import time
import thirdeye_client
from thirdeye_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: oauth
configuration = thirdeye_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = thirdeye_client.DataSourceApi(thirdeye_client.ApiClient(configuration))
name = 'name_example' # str |  (optional)

try:
    api_instance.offboard_all(name=name)
except ApiException as e:
    print("Exception when calling DataSourceApi->offboard_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **onboard_all**
> onboard_all(name=name)



### Example
```python
from __future__ import print_function
import time
import thirdeye_client
from thirdeye_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: oauth
configuration = thirdeye_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = thirdeye_client.DataSourceApi(thirdeye_client.ApiClient(configuration))
name = 'name_example' # str |  (optional)

try:
    api_instance.onboard_all(name=name)
except ApiException as e:
    print("Exception when calling DataSourceApi->onboard_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **onboard_dataset**
> onboard_dataset(data_source_name=data_source_name, dataset_name=dataset_name)



### Example
```python
from __future__ import print_function
import time
import thirdeye_client
from thirdeye_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: oauth
configuration = thirdeye_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = thirdeye_client.DataSourceApi(thirdeye_client.ApiClient(configuration))
data_source_name = 'data_source_name_example' # str |  (optional)
dataset_name = 'dataset_name_example' # str |  (optional)

try:
    api_instance.onboard_dataset(data_source_name=data_source_name, dataset_name=dataset_name)
except ApiException as e:
    print("Exception when calling DataSourceApi->onboard_dataset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_source_name** | **str**|  | [optional] 
 **dataset_name** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate**
> validate(name=name)



### Example
```python
from __future__ import print_function
import time
import thirdeye_client
from thirdeye_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: oauth
configuration = thirdeye_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = thirdeye_client.DataSourceApi(thirdeye_client.ApiClient(configuration))
name = 'name_example' # str |  (optional)

try:
    api_instance.validate(name=name)
except ApiException as e:
    print("Exception when calling DataSourceApi->validate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

