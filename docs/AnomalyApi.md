# thirdeye_client.AnomalyApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**count_with_predicate7**](AnomalyApi.md#count_with_predicate7) | **GET** /api/anomalies/count | 
[**create_multiple7**](AnomalyApi.md#create_multiple7) | **POST** /api/anomalies | 
[**delete7**](AnomalyApi.md#delete7) | **DELETE** /api/anomalies/{id} | 
[**delete_all7**](AnomalyApi.md#delete_all7) | **DELETE** /api/anomalies/all | 
[**edit_multiple7**](AnomalyApi.md#edit_multiple7) | **PUT** /api/anomalies | 
[**get15**](AnomalyApi.md#get15) | **GET** /api/anomalies/{id} | 
[**get16**](AnomalyApi.md#get16) | **GET** /api/anomalies/name/{name} | 
[**get_all7**](AnomalyApi.md#get_all7) | **GET** /api/anomalies | 
[**set_feedback**](AnomalyApi.md#set_feedback) | **POST** /api/anomalies/{id}/feedback | 


# **count_with_predicate7**
> count_with_predicate7()



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
api_instance = thirdeye_client.AnomalyApi(thirdeye_client.ApiClient(configuration))

try:
    api_instance.count_with_predicate7()
except ApiException as e:
    print("Exception when calling AnomalyApi->count_with_predicate7: %s\n" % e)
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

# **create_multiple7**
> create_multiple7(body=body)



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
api_instance = thirdeye_client.AnomalyApi(thirdeye_client.ApiClient(configuration))
body = [thirdeye_client.AnomalyApiModel()] # list[AnomalyApiModel] |  (optional)

try:
    api_instance.create_multiple7(body=body)
except ApiException as e:
    print("Exception when calling AnomalyApi->create_multiple7: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[AnomalyApiModel]**](AnomalyApiModel.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete7**
> delete7(id)



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
api_instance = thirdeye_client.AnomalyApi(thirdeye_client.ApiClient(configuration))
id = 789 # int | 

try:
    api_instance.delete7(id)
except ApiException as e:
    print("Exception when calling AnomalyApi->delete7: %s\n" % e)
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

# **delete_all7**
> delete_all7()



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
api_instance = thirdeye_client.AnomalyApi(thirdeye_client.ApiClient(configuration))

try:
    api_instance.delete_all7()
except ApiException as e:
    print("Exception when calling AnomalyApi->delete_all7: %s\n" % e)
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

# **edit_multiple7**
> edit_multiple7(body=body)



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
api_instance = thirdeye_client.AnomalyApi(thirdeye_client.ApiClient(configuration))
body = [thirdeye_client.AnomalyApiModel()] # list[AnomalyApiModel] |  (optional)

try:
    api_instance.edit_multiple7(body=body)
except ApiException as e:
    print("Exception when calling AnomalyApi->edit_multiple7: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[AnomalyApiModel]**](AnomalyApiModel.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get15**
> get15(id)



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
api_instance = thirdeye_client.AnomalyApi(thirdeye_client.ApiClient(configuration))
id = 789 # int | 

try:
    api_instance.get15(id)
except ApiException as e:
    print("Exception when calling AnomalyApi->get15: %s\n" % e)
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

# **get16**
> get16(name)



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
api_instance = thirdeye_client.AnomalyApi(thirdeye_client.ApiClient(configuration))
name = 'name_example' # str | 

try:
    api_instance.get16(name)
except ApiException as e:
    print("Exception when calling AnomalyApi->get16: %s\n" % e)
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

# **get_all7**
> get_all7()



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
api_instance = thirdeye_client.AnomalyApi(thirdeye_client.ApiClient(configuration))

try:
    api_instance.get_all7()
except ApiException as e:
    print("Exception when calling AnomalyApi->get_all7: %s\n" % e)
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

# **set_feedback**
> set_feedback(id, body=body)



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
api_instance = thirdeye_client.AnomalyApi(thirdeye_client.ApiClient(configuration))
id = 789 # int | 
body = thirdeye_client.AnomalyFeedbackApiModel() # AnomalyFeedbackApiModel |  (optional)

try:
    api_instance.set_feedback(id, body=body)
except ApiException as e:
    print("Exception when calling AnomalyApi->set_feedback: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**AnomalyFeedbackApiModel**](AnomalyFeedbackApiModel.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

