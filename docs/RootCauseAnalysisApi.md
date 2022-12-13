# thirdeye_client.RootCauseAnalysisApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**count_with_predicate8**](RootCauseAnalysisApi.md#count_with_predicate8) | **GET** /api/rca/investigations/count | 
[**create_multiple8**](RootCauseAnalysisApi.md#create_multiple8) | **POST** /api/rca/investigations | 
[**data_cube_summary**](RootCauseAnalysisApi.md#data_cube_summary) | **GET** /api/rca/dim-analysis | Retrieve the likely root causes behind an anomaly
[**delete8**](RootCauseAnalysisApi.md#delete8) | **DELETE** /api/rca/investigations/{id} | 
[**delete_all8**](RootCauseAnalysisApi.md#delete_all8) | **DELETE** /api/rca/investigations/all | 
[**edit_multiple8**](RootCauseAnalysisApi.md#edit_multiple8) | **PUT** /api/rca/investigations | 
[**generate_cohorts**](RootCauseAnalysisApi.md#generate_cohorts) | **POST** /api/rca/metrics/cohorts | Builds cohorts based on threshold
[**get17**](RootCauseAnalysisApi.md#get17) | **GET** /api/rca/investigations/{id} | 
[**get18**](RootCauseAnalysisApi.md#get18) | **GET** /api/rca/investigations/name/{name} | 
[**get_all8**](RootCauseAnalysisApi.md#get_all8) | **GET** /api/rca/investigations | 
[**get_anomalies_events**](RootCauseAnalysisApi.md#get_anomalies_events) | **GET** /api/rca/related/anomalies | Returns anomalies related to the anomaly. Anomalies are ordered by the scoring function.
[**get_anomaly_heatmap**](RootCauseAnalysisApi.md#get_anomaly_heatmap) | **GET** /api/rca/metrics/heatmap | Returns heatmap for the specified anomaly.  Aligns time stamps if necessary and omits null values.
[**get_calendar_events**](RootCauseAnalysisApi.md#get_calendar_events) | **GET** /api/rca/related/events | Returns calendar events related to the anomaly. Events are ordered by the scoring function.


# **count_with_predicate8**
> count_with_predicate8()



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
api_instance = thirdeye_client.RootCauseAnalysisApi(thirdeye_client.ApiClient(configuration))

try:
    api_instance.count_with_predicate8()
except ApiException as e:
    print("Exception when calling RootCauseAnalysisApi->count_with_predicate8: %s\n" % e)
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

# **create_multiple8**
> create_multiple8(body=body)



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
api_instance = thirdeye_client.RootCauseAnalysisApi(thirdeye_client.ApiClient(configuration))
body = [thirdeye_client.RcaInvestigationApiModel()] # list[RcaInvestigationApiModel] |  (optional)

try:
    api_instance.create_multiple8(body=body)
except ApiException as e:
    print("Exception when calling RootCauseAnalysisApi->create_multiple8: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[RcaInvestigationApiModel]**](RcaInvestigationApiModel.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_cube_summary**
> data_cube_summary(id=id, baseline_offset=baseline_offset, filters=filters, summary_size=summary_size, depth=depth, one_side_error=one_side_error, dimensions=dimensions, excluded_dimensions=excluded_dimensions, hierarchies=hierarchies)

Retrieve the likely root causes behind an anomaly



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
api_instance = thirdeye_client.RootCauseAnalysisApi(thirdeye_client.ApiClient(configuration))
id = 789 # int | id of the anomaly (optional)
baseline_offset = 'P1W' # str | baseline offset identifier in ISO 8601 format(e.g. \"P1W\"). (optional) (default to P1W)
filters = ['filters_example'] # list[str] | dimension filters (e.g. \"dim1=val1\", \"dim2!=val2\") (optional)
summary_size = 4 # int | Number of entries to put in the summary. (optional) (default to 4)
depth = 3 # int | Maximum number of dimensions to drill down by. (optional) (default to 3)
one_side_error = true # bool | If true, only returns changes that have the same direction as the global change. (optional) (default to true)
dimensions = ['dimensions_example'] # list[str] | List of dimensions to use for the analysis. If empty, all dimensions of the datasets are used. (optional)
excluded_dimensions = ['excluded_dimensions_example'] # list[str] | List of dimensions to exclude from the analysis. (optional)
hierarchies = '[]' # str | Hierarchy among some dimensions. The order will be respected in the result. An example of a hierarchical group is {continent, country}. Parameter format is [[\"continent\",\"country\"], [\"dim1\", \"dim2\", \"dim3\"]] (optional) (default to [])

try:
    # Retrieve the likely root causes behind an anomaly
    api_instance.data_cube_summary(id=id, baseline_offset=baseline_offset, filters=filters, summary_size=summary_size, depth=depth, one_side_error=one_side_error, dimensions=dimensions, excluded_dimensions=excluded_dimensions, hierarchies=hierarchies)
except ApiException as e:
    print("Exception when calling RootCauseAnalysisApi->data_cube_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id of the anomaly | [optional] 
 **baseline_offset** | **str**| baseline offset identifier in ISO 8601 format(e.g. \&quot;P1W\&quot;). | [optional] [default to P1W]
 **filters** | [**list[str]**](str.md)| dimension filters (e.g. \&quot;dim1&#x3D;val1\&quot;, \&quot;dim2!&#x3D;val2\&quot;) | [optional] 
 **summary_size** | **int**| Number of entries to put in the summary. | [optional] [default to 4]
 **depth** | **int**| Maximum number of dimensions to drill down by. | [optional] [default to 3]
 **one_side_error** | **bool**| If true, only returns changes that have the same direction as the global change. | [optional] [default to true]
 **dimensions** | [**list[str]**](str.md)| List of dimensions to use for the analysis. If empty, all dimensions of the datasets are used. | [optional] 
 **excluded_dimensions** | [**list[str]**](str.md)| List of dimensions to exclude from the analysis. | [optional] 
 **hierarchies** | **str**| Hierarchy among some dimensions. The order will be respected in the result. An example of a hierarchical group is {continent, country}. Parameter format is [[\&quot;continent\&quot;,\&quot;country\&quot;], [\&quot;dim1\&quot;, \&quot;dim2\&quot;, \&quot;dim3\&quot;]] | [optional] [default to []]

### Return type

void (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete8**
> delete8(id)



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
api_instance = thirdeye_client.RootCauseAnalysisApi(thirdeye_client.ApiClient(configuration))
id = 789 # int | 

try:
    api_instance.delete8(id)
except ApiException as e:
    print("Exception when calling RootCauseAnalysisApi->delete8: %s\n" % e)
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

# **delete_all8**
> delete_all8()



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
api_instance = thirdeye_client.RootCauseAnalysisApi(thirdeye_client.ApiClient(configuration))

try:
    api_instance.delete_all8()
except ApiException as e:
    print("Exception when calling RootCauseAnalysisApi->delete_all8: %s\n" % e)
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

# **edit_multiple8**
> edit_multiple8(body=body)



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
api_instance = thirdeye_client.RootCauseAnalysisApi(thirdeye_client.ApiClient(configuration))
body = [thirdeye_client.RcaInvestigationApiModel()] # list[RcaInvestigationApiModel] |  (optional)

try:
    api_instance.edit_multiple8(body=body)
except ApiException as e:
    print("Exception when calling RootCauseAnalysisApi->edit_multiple8: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[RcaInvestigationApiModel]**](RcaInvestigationApiModel.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_cohorts**
> generate_cohorts(body=body)

Builds cohorts based on threshold



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
api_instance = thirdeye_client.RootCauseAnalysisApi(thirdeye_client.ApiClient(configuration))
body = thirdeye_client.CohortComputationApiModel() # CohortComputationApiModel |  (optional)

try:
    # Builds cohorts based on threshold
    api_instance.generate_cohorts(body=body)
except ApiException as e:
    print("Exception when calling RootCauseAnalysisApi->generate_cohorts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CohortComputationApiModel**](CohortComputationApiModel.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get17**
> get17(id)



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
api_instance = thirdeye_client.RootCauseAnalysisApi(thirdeye_client.ApiClient(configuration))
id = 789 # int | 

try:
    api_instance.get17(id)
except ApiException as e:
    print("Exception when calling RootCauseAnalysisApi->get17: %s\n" % e)
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

# **get18**
> get18(name)



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
api_instance = thirdeye_client.RootCauseAnalysisApi(thirdeye_client.ApiClient(configuration))
name = 'name_example' # str | 

try:
    api_instance.get18(name)
except ApiException as e:
    print("Exception when calling RootCauseAnalysisApi->get18: %s\n" % e)
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

# **get_all8**
> get_all8()



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
api_instance = thirdeye_client.RootCauseAnalysisApi(thirdeye_client.ApiClient(configuration))

try:
    api_instance.get_all8()
except ApiException as e:
    print("Exception when calling RootCauseAnalysisApi->get_all8: %s\n" % e)
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

# **get_anomalies_events**
> get_anomalies_events(anomaly_id, scoring=scoring, limit=limit, lookaround=lookaround)

Returns anomalies related to the anomaly. Anomalies are ordered by the scoring function.



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
api_instance = thirdeye_client.RootCauseAnalysisApi(thirdeye_client.ApiClient(configuration))
anomaly_id = 789 # int | id of the anomaly
scoring = 'TRIANGULAR' # str | Scoring function (optional) (default to TRIANGULAR)
limit = 50 # int | Limit number of anomalies to return. (optional) (default to 50)
lookaround = 'P7D' # str | Period, in ISO-8601 format, to look after and before the anomaly start. (optional) (default to P7D)

try:
    # Returns anomalies related to the anomaly. Anomalies are ordered by the scoring function.
    api_instance.get_anomalies_events(anomaly_id, scoring=scoring, limit=limit, lookaround=lookaround)
except ApiException as e:
    print("Exception when calling RootCauseAnalysisApi->get_anomalies_events: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **anomaly_id** | **int**| id of the anomaly | 
 **scoring** | **str**| Scoring function | [optional] [default to TRIANGULAR]
 **limit** | **int**| Limit number of anomalies to return. | [optional] [default to 50]
 **lookaround** | **str**| Period, in ISO-8601 format, to look after and before the anomaly start. | [optional] [default to P7D]

### Return type

void (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_anomaly_heatmap**
> get_anomaly_heatmap(id=id, baseline_offset=baseline_offset, filters=filters, dimensions=dimensions, excluded_dimensions=excluded_dimensions, limit=limit)

Returns heatmap for the specified anomaly.  Aligns time stamps if necessary and omits null values.



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
api_instance = thirdeye_client.RootCauseAnalysisApi(thirdeye_client.ApiClient(configuration))
id = 789 # int | id of the anomaly (optional)
baseline_offset = 'P1W' # str | baseline offset identifier in ISO 8601 format(e.g. \"P1W\"). (optional) (default to P1W)
filters = ['filters_example'] # list[str] | dimension filters (e.g. \"dim1=val1\", \"dim2!=val2\") (optional)
dimensions = ['dimensions_example'] # list[str] | List of dimensions to use for the analysis. If empty, all dimensions of the datasets are used. (optional)
excluded_dimensions = ['excluded_dimensions_example'] # list[str] | List of dimensions to exclude from the analysis. (optional)
limit = 56 # int | limit results to the top k elements, plus 'OTHER' rollup element (optional)

try:
    # Returns heatmap for the specified anomaly.  Aligns time stamps if necessary and omits null values.
    api_instance.get_anomaly_heatmap(id=id, baseline_offset=baseline_offset, filters=filters, dimensions=dimensions, excluded_dimensions=excluded_dimensions, limit=limit)
except ApiException as e:
    print("Exception when calling RootCauseAnalysisApi->get_anomaly_heatmap: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id of the anomaly | [optional] 
 **baseline_offset** | **str**| baseline offset identifier in ISO 8601 format(e.g. \&quot;P1W\&quot;). | [optional] [default to P1W]
 **filters** | [**list[str]**](str.md)| dimension filters (e.g. \&quot;dim1&#x3D;val1\&quot;, \&quot;dim2!&#x3D;val2\&quot;) | [optional] 
 **dimensions** | [**list[str]**](str.md)| List of dimensions to use for the analysis. If empty, all dimensions of the datasets are used. | [optional] 
 **excluded_dimensions** | [**list[str]**](str.md)| List of dimensions to exclude from the analysis. | [optional] 
 **limit** | **int**| limit results to the top k elements, plus &#39;OTHER&#39; rollup element | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_calendar_events**
> get_calendar_events(anomaly_id, type=type, scoring=scoring, limit=limit, lookaround=lookaround)

Returns calendar events related to the anomaly. Events are ordered by the scoring function.



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
api_instance = thirdeye_client.RootCauseAnalysisApi(thirdeye_client.ApiClient(configuration))
anomaly_id = 789 # int | id of the anomaly
type = 'type_example' # str | Type of event. (optional)
scoring = 'TRIANGULAR' # str | Scoring function (optional) (default to TRIANGULAR)
limit = 50 # int | Limit number of anomalies to return. (optional) (default to 50)
lookaround = 'P7D' # str | Period, in ISO-8601 format, to look after and before the anomaly start. (optional) (default to P7D)

try:
    # Returns calendar events related to the anomaly. Events are ordered by the scoring function.
    api_instance.get_calendar_events(anomaly_id, type=type, scoring=scoring, limit=limit, lookaround=lookaround)
except ApiException as e:
    print("Exception when calling RootCauseAnalysisApi->get_calendar_events: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **anomaly_id** | **int**| id of the anomaly | 
 **type** | **str**| Type of event. | [optional] 
 **scoring** | **str**| Scoring function | [optional] [default to TRIANGULAR]
 **limit** | **int**| Limit number of anomalies to return. | [optional] [default to 50]
 **lookaround** | **str**| Period, in ISO-8601 format, to look after and before the anomaly start. | [optional] [default to P7D]

### Return type

void (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

