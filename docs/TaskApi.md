# thirdeye_client.TaskApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**count_with_predicate10**](TaskApi.md#count_with_predicate10) | **GET** /api/tasks/count | 
[**delete10**](TaskApi.md#delete10) | **DELETE** /api/tasks/{id} | 
[**delete_all10**](TaskApi.md#delete_all10) | **DELETE** /api/tasks/all | 
[**get21**](TaskApi.md#get21) | **GET** /api/tasks/{id} | 
[**get22**](TaskApi.md#get22) | **GET** /api/tasks/name/{name} | 
[**get_all10**](TaskApi.md#get_all10) | **GET** /api/tasks | 
[**purge**](TaskApi.md#purge) | **DELETE** /api/tasks/purge | 


# **count_with_predicate10**
> count_with_predicate10()



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
api_instance = thirdeye_client.TaskApi(thirdeye_client.ApiClient(configuration))

try:
    api_instance.count_with_predicate10()
except ApiException as e:
    print("Exception when calling TaskApi->count_with_predicate10: %s\n" % e)
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

# **delete10**
> delete10(id)



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
api_instance = thirdeye_client.TaskApi(thirdeye_client.ApiClient(configuration))
id = 789 # int | 

try:
    api_instance.delete10(id)
except ApiException as e:
    print("Exception when calling TaskApi->delete10: %s\n" % e)
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

# **delete_all10**
> delete_all10()



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
api_instance = thirdeye_client.TaskApi(thirdeye_client.ApiClient(configuration))

try:
    api_instance.delete_all10()
except ApiException as e:
    print("Exception when calling TaskApi->delete_all10: %s\n" % e)
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

# **get21**
> get21(id)



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
api_instance = thirdeye_client.TaskApi(thirdeye_client.ApiClient(configuration))
id = 789 # int | 

try:
    api_instance.get21(id)
except ApiException as e:
    print("Exception when calling TaskApi->get21: %s\n" % e)
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

# **get22**
> get22(name)



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
api_instance = thirdeye_client.TaskApi(thirdeye_client.ApiClient(configuration))
name = 'name_example' # str | 

try:
    api_instance.get22(name)
except ApiException as e:
    print("Exception when calling TaskApi->get22: %s\n" % e)
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

# **get_all10**
> get_all10()



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
api_instance = thirdeye_client.TaskApi(thirdeye_client.ApiClient(configuration))

try:
    api_instance.get_all10()
except ApiException as e:
    print("Exception when calling TaskApi->get_all10: %s\n" % e)
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

# **purge**
> purge(older_than_in_days=older_than_in_days, limit=limit)



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
api_instance = thirdeye_client.TaskApi(thirdeye_client.ApiClient(configuration))
older_than_in_days = 30 # int | Older than (number of days) (optional) (default to 30)
limit = 1000 # int | Max Entries to delete (optional) (default to 1000)

try:
    api_instance.purge(older_than_in_days=older_than_in_days, limit=limit)
except ApiException as e:
    print("Exception when calling TaskApi->purge: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **older_than_in_days** | **int**| Older than (number of days) | [optional] [default to 30]
 **limit** | **int**| Max Entries to delete | [optional] [default to 1000]

### Return type

void (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

