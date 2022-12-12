# thirdeye_client.AppAnalyticsApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_analytics_payload**](AppAnalyticsApi.md#get_analytics_payload) | **GET** /api/app-analytics | 
[**get_version**](AppAnalyticsApi.md#get_version) | **GET** /api/app-analytics/version | 


# **get_analytics_payload**
> get_analytics_payload()



### Example
```python
from __future__ import print_function
import time
import thirdeye_client
from thirdeye_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = thirdeye_client.AppAnalyticsApi()

try:
    api_instance.get_analytics_payload()
except ApiException as e:
    print("Exception when calling AppAnalyticsApi->get_analytics_payload: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_version**
> get_version()



### Example
```python
from __future__ import print_function
import time
import thirdeye_client
from thirdeye_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = thirdeye_client.AppAnalyticsApi()

try:
    api_instance.get_version()
except ApiException as e:
    print("Exception when calling AppAnalyticsApi->get_version: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

