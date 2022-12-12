# thirdeye_client.EventApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**count_with_predicate9**](EventApi.md#count_with_predicate9) | **GET** /api/events/count | 
[**create_multiple9**](EventApi.md#create_multiple9) | **POST** /api/events | 
[**delete9**](EventApi.md#delete9) | **DELETE** /api/events/{id} | 
[**delete_all9**](EventApi.md#delete_all9) | **DELETE** /api/events/all | 
[**edit_multiple9**](EventApi.md#edit_multiple9) | **PUT** /api/events | 
[**get19**](EventApi.md#get19) | **GET** /api/events/name/{name} | 
[**get20**](EventApi.md#get20) | **GET** /api/events/{id} | 
[**get_all9**](EventApi.md#get_all9) | **GET** /api/events | 
[**load_holidays**](EventApi.md#load_holidays) | **POST** /api/events/holidays/load | 
[**load_holidays1**](EventApi.md#load_holidays1) | **POST** /api/events/create-from-anomaly | 


# **count_with_predicate9**
> count_with_predicate9()



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
api_instance = thirdeye_client.EventApi(thirdeye_client.ApiClient(configuration))

try:
    api_instance.count_with_predicate9()
except ApiException as e:
    print("Exception when calling EventApi->count_with_predicate9: %s\n" % e)
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

# **create_multiple9**
> create_multiple9(body=body)



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
api_instance = thirdeye_client.EventApi(thirdeye_client.ApiClient(configuration))
body = [thirdeye_client.EventApi()] # list[EventApi] |  (optional)

try:
    api_instance.create_multiple9(body=body)
except ApiException as e:
    print("Exception when calling EventApi->create_multiple9: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[EventApi]**](EventApi.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete9**
> delete9(id)



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
api_instance = thirdeye_client.EventApi(thirdeye_client.ApiClient(configuration))
id = 789 # int | 

try:
    api_instance.delete9(id)
except ApiException as e:
    print("Exception when calling EventApi->delete9: %s\n" % e)
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

# **delete_all9**
> delete_all9()



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
api_instance = thirdeye_client.EventApi(thirdeye_client.ApiClient(configuration))

try:
    api_instance.delete_all9()
except ApiException as e:
    print("Exception when calling EventApi->delete_all9: %s\n" % e)
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

# **edit_multiple9**
> edit_multiple9(body=body)



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
api_instance = thirdeye_client.EventApi(thirdeye_client.ApiClient(configuration))
body = [thirdeye_client.EventApi()] # list[EventApi] |  (optional)

try:
    api_instance.edit_multiple9(body=body)
except ApiException as e:
    print("Exception when calling EventApi->edit_multiple9: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[EventApi]**](EventApi.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get19**
> get19(name)



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
api_instance = thirdeye_client.EventApi(thirdeye_client.ApiClient(configuration))
name = 'name_example' # str | 

try:
    api_instance.get19(name)
except ApiException as e:
    print("Exception when calling EventApi->get19: %s\n" % e)
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

# **get20**
> get20(id)



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
api_instance = thirdeye_client.EventApi(thirdeye_client.ApiClient(configuration))
id = 789 # int | 

try:
    api_instance.get20(id)
except ApiException as e:
    print("Exception when calling EventApi->get20: %s\n" % e)
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

# **get_all9**
> get_all9()



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
api_instance = thirdeye_client.EventApi(thirdeye_client.ApiClient(configuration))

try:
    api_instance.get_all9()
except ApiException as e:
    print("Exception when calling EventApi->get_all9: %s\n" % e)
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

# **load_holidays**
> load_holidays(start_time=start_time, end_time=end_time)



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
api_instance = thirdeye_client.EventApi(thirdeye_client.ApiClient(configuration))
start_time = 789 # int |  (optional)
end_time = 789 # int |  (optional)

try:
    api_instance.load_holidays(start_time=start_time, end_time=end_time)
except ApiException as e:
    print("Exception when calling EventApi->load_holidays: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **load_holidays1**
> load_holidays1(anomaly_id=anomaly_id)



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
api_instance = thirdeye_client.EventApi(thirdeye_client.ApiClient(configuration))
anomaly_id = 789 # int |  (optional)

try:
    api_instance.load_holidays1(anomaly_id=anomaly_id)
except ApiException as e:
    print("Exception when calling EventApi->load_holidays1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **anomaly_id** | **int**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

