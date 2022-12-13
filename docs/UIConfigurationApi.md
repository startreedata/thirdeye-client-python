# thirdeye_client.UIConfigurationApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get23**](UIConfigurationApi.md#get23) | **GET** /api/ui/config | 


# **get23**
> get23()



### Example
```python
from __future__ import print_function
import time
import thirdeye_client
from thirdeye_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = thirdeye_client.UIConfigurationApi()

try:
    api_instance.get23()
except ApiException as e:
    print("Exception when calling UIConfigurationApi->get23: %s\n" % e)
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

