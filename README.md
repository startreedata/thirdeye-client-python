# thirdeye-client-python
No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.108.0
- Package version: 1.108.0

## Requirements.

Python 3.4+

## Installation & Usage
### pip install

Install the latest version from Github via pip

```sh
pip install git+https://github.com/startreedata/thirdeye-client-python.git
```

To install a specific version that corresponds to your ThirdEye instance, use

```
pip install git+https://github.com/startreedata/thirdeye-client-python.git@x.y.z
```
with `x.y.z` the version of ThirdEye you need.
The ThirdEye instance version can be obtained with the `GET /api/app-analytics/version` endpoint.

## Getting Started

The following shows how you would create an alert.

```python
from __future__ import print_function
import thirdeye_client
from thirdeye_client.rest import ApiException
from thirdeye_client.api.alert_api import AlertApi
import json

# Configure API key authorization
configuration = thirdeye_client.Configuration()
# see how to get a token here https://dev.startree.ai/docs/startree-enterprise-edition/startree-thirdeye/how-tos/use-the-api#using-swagger
configuration.api_key['Authorization'] = 'Bearer 123456'
# use your thirdeye environment
configuration.host = "https://thirdeye.YOUR.ENV.startree.cloud"
http_call_config = dict(_preload_content=False)

# create an Alert client
alert_api_client = AlertApi(thirdeye_client.ApiClient(configuration))

new_alert = {
    "name": "my-alert",
    "description": "my new alert",
    "template": {
        "name": "startree-ets"
    },
    "templateProperties": {
        "dataSource": "pinot",
        "dataset": "MY_DATASET",
        "aggregationFunction": "sum",
        "seasonalityPeriod": "P7D",
        "lookback": "P21D",
        "monitoringGranularity": "P1D",
        "sensitivity": "1",
        "aggregationColumn": "MY_METRIC_COLUMN"
    },
    "cron": "0 0 5 ? * * *"
}

# create a new alert
try:
    res = alert_api_client.create_multiple3(body=[new_alert], **http_call_config)
    data = res.data
    d = json.loads(data)
    print(d)
except ApiException as e:
    print("Exception when calling AlertApi: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to `https://thirdeye.YOUR.ENV.startree.cloud`.

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AlertApi* | [**count_with_predicate3**](docs/AlertApi.md#count_with_predicate3) | **GET** /api/alerts/count | 
*AlertApi* | [**create_multiple3**](docs/AlertApi.md#create_multiple3) | **POST** /api/alerts | 
*AlertApi* | [**delete3**](docs/AlertApi.md#delete3) | **DELETE** /api/alerts/{id} | 
*AlertApi* | [**delete_all3**](docs/AlertApi.md#delete_all3) | **DELETE** /api/alerts/all | 
*AlertApi* | [**edit_multiple3**](docs/AlertApi.md#edit_multiple3) | **PUT** /api/alerts | 
*AlertApi* | [**evaluate**](docs/AlertApi.md#evaluate) | **POST** /api/alerts/evaluate | 
*AlertApi* | [**get7**](docs/AlertApi.md#get7) | **GET** /api/alerts/{id} | 
*AlertApi* | [**get8**](docs/AlertApi.md#get8) | **GET** /api/alerts/name/{name} | 
*AlertApi* | [**get_all3**](docs/AlertApi.md#get_all3) | **GET** /api/alerts | 
*AlertApi* | [**get_analytics**](docs/AlertApi.md#get_analytics) | **GET** /api/alerts/{id}/stats | 
*AlertApi* | [**get_insights**](docs/AlertApi.md#get_insights) | **GET** /api/alerts/{id}/insights | 
*AlertApi* | [**get_insights1**](docs/AlertApi.md#get_insights1) | **POST** /api/alerts/insights | 
*AlertApi* | [**reset**](docs/AlertApi.md#reset) | **POST** /api/alerts/{id}/reset | Delete associated anomalies and rerun detection till present
*AlertApi* | [**run_task**](docs/AlertApi.md#run_task) | **POST** /api/alerts/{id}/run | 
*AlertApi* | [**validate_multiple**](docs/AlertApi.md#validate_multiple) | **POST** /api/alerts/validate | 
*AlertTemplateApi* | [**count_with_predicate4**](docs/AlertTemplateApi.md#count_with_predicate4) | **GET** /api/alert-templates/count | 
*AlertTemplateApi* | [**create_multiple4**](docs/AlertTemplateApi.md#create_multiple4) | **POST** /api/alert-templates | 
*AlertTemplateApi* | [**delete4**](docs/AlertTemplateApi.md#delete4) | **DELETE** /api/alert-templates/{id} | 
*AlertTemplateApi* | [**delete_all4**](docs/AlertTemplateApi.md#delete_all4) | **DELETE** /api/alert-templates/all | 
*AlertTemplateApi* | [**edit_multiple4**](docs/AlertTemplateApi.md#edit_multiple4) | **PUT** /api/alert-templates | 
*AlertTemplateApi* | [**get10**](docs/AlertTemplateApi.md#get10) | **GET** /api/alert-templates/name/{name} | 
*AlertTemplateApi* | [**get9**](docs/AlertTemplateApi.md#get9) | **GET** /api/alert-templates/{id} | 
*AlertTemplateApi* | [**get_all4**](docs/AlertTemplateApi.md#get_all4) | **GET** /api/alert-templates | 
*AlertTemplateApi* | [**load_recommended_templates**](docs/AlertTemplateApi.md#load_recommended_templates) | **POST** /api/alert-templates/load-defaults | 
*AnomalyApi* | [**count_with_predicate7**](docs/AnomalyApi.md#count_with_predicate7) | **GET** /api/anomalies/count | 
*AnomalyApi* | [**create_multiple7**](docs/AnomalyApi.md#create_multiple7) | **POST** /api/anomalies | 
*AnomalyApi* | [**delete7**](docs/AnomalyApi.md#delete7) | **DELETE** /api/anomalies/{id} | 
*AnomalyApi* | [**delete_all7**](docs/AnomalyApi.md#delete_all7) | **DELETE** /api/anomalies/all | 
*AnomalyApi* | [**edit_multiple7**](docs/AnomalyApi.md#edit_multiple7) | **PUT** /api/anomalies | 
*AnomalyApi* | [**get15**](docs/AnomalyApi.md#get15) | **GET** /api/anomalies/{id} | 
*AnomalyApi* | [**get16**](docs/AnomalyApi.md#get16) | **GET** /api/anomalies/name/{name} | 
*AnomalyApi* | [**get_all7**](docs/AnomalyApi.md#get_all7) | **GET** /api/anomalies | 
*AnomalyApi* | [**set_feedback**](docs/AnomalyApi.md#set_feedback) | **POST** /api/anomalies/{id}/feedback | 
*AppAnalyticsApi* | [**get_analytics_payload**](docs/AppAnalyticsApi.md#get_analytics_payload) | **GET** /api/app-analytics | 
*AppAnalyticsApi* | [**get_version**](docs/AppAnalyticsApi.md#get_version) | **GET** /api/app-analytics/version | 
*AuthApi* | [**login**](docs/AuthApi.md#login) | **POST** /api/auth/login | 
*AuthApi* | [**logout**](docs/AuthApi.md#logout) | **POST** /api/auth/logout | 
*AuthInfoApi* | [**get**](docs/AuthInfoApi.md#get) | **GET** /api/info | 
*DataSourceApi* | [**clear_data_source_cache**](docs/DataSourceApi.md#clear_data_source_cache) | **DELETE** /api/data-sources/cache | 
*DataSourceApi* | [**count_with_predicate**](docs/DataSourceApi.md#count_with_predicate) | **GET** /api/data-sources/count | 
*DataSourceApi* | [**create_multiple**](docs/DataSourceApi.md#create_multiple) | **POST** /api/data-sources | 
*DataSourceApi* | [**delete**](docs/DataSourceApi.md#delete) | **DELETE** /api/data-sources/{id} | 
*DataSourceApi* | [**delete_all**](docs/DataSourceApi.md#delete_all) | **DELETE** /api/data-sources/all | 
*DataSourceApi* | [**edit_multiple**](docs/DataSourceApi.md#edit_multiple) | **PUT** /api/data-sources | 
*DataSourceApi* | [**get1**](docs/DataSourceApi.md#get1) | **GET** /api/data-sources/{id} | 
*DataSourceApi* | [**get2**](docs/DataSourceApi.md#get2) | **GET** /api/data-sources/name/{name} | 
*DataSourceApi* | [**get_all**](docs/DataSourceApi.md#get_all) | **GET** /api/data-sources | 
*DataSourceApi* | [**get_datasets**](docs/DataSourceApi.md#get_datasets) | **GET** /api/data-sources/name/{name}/datasets | 
*DataSourceApi* | [**offboard_all**](docs/DataSourceApi.md#offboard_all) | **DELETE** /api/data-sources/offboard-all | 
*DataSourceApi* | [**onboard_all**](docs/DataSourceApi.md#onboard_all) | **POST** /api/data-sources/onboard-all | 
*DataSourceApi* | [**onboard_dataset**](docs/DataSourceApi.md#onboard_dataset) | **POST** /api/data-sources/onboard-dataset | 
*DataSourceApi* | [**validate**](docs/DataSourceApi.md#validate) | **GET** /api/data-sources/validate | 
*DatasetApi* | [**count_with_predicate1**](docs/DatasetApi.md#count_with_predicate1) | **GET** /api/datasets/count | 
*DatasetApi* | [**create_multiple1**](docs/DatasetApi.md#create_multiple1) | **POST** /api/datasets | 
*DatasetApi* | [**delete1**](docs/DatasetApi.md#delete1) | **DELETE** /api/datasets/{id} | 
*DatasetApi* | [**delete_all1**](docs/DatasetApi.md#delete_all1) | **DELETE** /api/datasets/all | 
*DatasetApi* | [**edit_multiple1**](docs/DatasetApi.md#edit_multiple1) | **PUT** /api/datasets | 
*DatasetApi* | [**get3**](docs/DatasetApi.md#get3) | **GET** /api/datasets/{id} | 
*DatasetApi* | [**get4**](docs/DatasetApi.md#get4) | **GET** /api/datasets/name/{name} | 
*DatasetApi* | [**get_all1**](docs/DatasetApi.md#get_all1) | **GET** /api/datasets | 
*EntityApi* | [**get_entity**](docs/EntityApi.md#get_entity) | **GET** /api/entities/types/{bean_class} | 
*EntityApi* | [**get_entity_info**](docs/EntityApi.md#get_entity_info) | **GET** /api/entities/types/{bean_class}/info | 
*EntityApi* | [**get_raw_entity**](docs/EntityApi.md#get_raw_entity) | **GET** /api/entities/{id} | 
*EntityApi* | [**list_entities**](docs/EntityApi.md#list_entities) | **GET** /api/entities/types | 
*EnumerationItemApi* | [**count_with_predicate5**](docs/EnumerationItemApi.md#count_with_predicate5) | **GET** /api/enumeration-items/count | 
*EnumerationItemApi* | [**create_multiple5**](docs/EnumerationItemApi.md#create_multiple5) | **POST** /api/enumeration-items | 
*EnumerationItemApi* | [**delete5**](docs/EnumerationItemApi.md#delete5) | **DELETE** /api/enumeration-items/{id} | 
*EnumerationItemApi* | [**delete_all5**](docs/EnumerationItemApi.md#delete_all5) | **DELETE** /api/enumeration-items/all | 
*EnumerationItemApi* | [**edit_multiple5**](docs/EnumerationItemApi.md#edit_multiple5) | **PUT** /api/enumeration-items | 
*EnumerationItemApi* | [**get11**](docs/EnumerationItemApi.md#get11) | **GET** /api/enumeration-items/{id} | 
*EnumerationItemApi* | [**get12**](docs/EnumerationItemApi.md#get12) | **GET** /api/enumeration-items/name/{name} | 
*EnumerationItemApi* | [**get_all5**](docs/EnumerationItemApi.md#get_all5) | **GET** /api/enumeration-items | 
*EventApi* | [**count_with_predicate9**](docs/EventApi.md#count_with_predicate9) | **GET** /api/events/count | 
*EventApi* | [**create_multiple9**](docs/EventApi.md#create_multiple9) | **POST** /api/events | 
*EventApi* | [**delete9**](docs/EventApi.md#delete9) | **DELETE** /api/events/{id} | 
*EventApi* | [**delete_all9**](docs/EventApi.md#delete_all9) | **DELETE** /api/events/all | 
*EventApi* | [**edit_multiple9**](docs/EventApi.md#edit_multiple9) | **PUT** /api/events | 
*EventApi* | [**get19**](docs/EventApi.md#get19) | **GET** /api/events/{id} | 
*EventApi* | [**get20**](docs/EventApi.md#get20) | **GET** /api/events/name/{name} | 
*EventApi* | [**get_all9**](docs/EventApi.md#get_all9) | **GET** /api/events | 
*EventApi* | [**load_holidays**](docs/EventApi.md#load_holidays) | **POST** /api/events/create-from-anomaly | 
*EventApi* | [**load_holidays1**](docs/EventApi.md#load_holidays1) | **POST** /api/events/holidays/load | 
*MetricApi* | [**count_with_predicate2**](docs/MetricApi.md#count_with_predicate2) | **GET** /api/metrics/count | 
*MetricApi* | [**create_multiple2**](docs/MetricApi.md#create_multiple2) | **POST** /api/metrics | 
*MetricApi* | [**delete2**](docs/MetricApi.md#delete2) | **DELETE** /api/metrics/{id} | 
*MetricApi* | [**delete_all2**](docs/MetricApi.md#delete_all2) | **DELETE** /api/metrics/all | 
*MetricApi* | [**edit_multiple2**](docs/MetricApi.md#edit_multiple2) | **PUT** /api/metrics | 
*MetricApi* | [**get5**](docs/MetricApi.md#get5) | **GET** /api/metrics/{id} | 
*MetricApi* | [**get6**](docs/MetricApi.md#get6) | **GET** /api/metrics/name/{name} | 
*MetricApi* | [**get_all2**](docs/MetricApi.md#get_all2) | **GET** /api/metrics | 
*RootCauseAnalysisApi* | [**count_with_predicate8**](docs/RootCauseAnalysisApi.md#count_with_predicate8) | **GET** /api/rca/investigations/count | 
*RootCauseAnalysisApi* | [**create_multiple8**](docs/RootCauseAnalysisApi.md#create_multiple8) | **POST** /api/rca/investigations | 
*RootCauseAnalysisApi* | [**data_cube_summary**](docs/RootCauseAnalysisApi.md#data_cube_summary) | **GET** /api/rca/dim-analysis | Retrieve the likely root causes behind an anomaly
*RootCauseAnalysisApi* | [**delete8**](docs/RootCauseAnalysisApi.md#delete8) | **DELETE** /api/rca/investigations/{id} | 
*RootCauseAnalysisApi* | [**delete_all8**](docs/RootCauseAnalysisApi.md#delete_all8) | **DELETE** /api/rca/investigations/all | 
*RootCauseAnalysisApi* | [**edit_multiple8**](docs/RootCauseAnalysisApi.md#edit_multiple8) | **PUT** /api/rca/investigations | 
*RootCauseAnalysisApi* | [**generate_cohorts**](docs/RootCauseAnalysisApi.md#generate_cohorts) | **POST** /api/rca/metrics/cohorts | Builds cohorts based on threshold
*RootCauseAnalysisApi* | [**get17**](docs/RootCauseAnalysisApi.md#get17) | **GET** /api/rca/investigations/{id} | 
*RootCauseAnalysisApi* | [**get18**](docs/RootCauseAnalysisApi.md#get18) | **GET** /api/rca/investigations/name/{name} | 
*RootCauseAnalysisApi* | [**get_all8**](docs/RootCauseAnalysisApi.md#get_all8) | **GET** /api/rca/investigations | 
*RootCauseAnalysisApi* | [**get_anomalies_events**](docs/RootCauseAnalysisApi.md#get_anomalies_events) | **GET** /api/rca/related/anomalies | Returns anomalies related to the anomaly. Anomalies are ordered by the scoring function.
*RootCauseAnalysisApi* | [**get_anomaly_heatmap**](docs/RootCauseAnalysisApi.md#get_anomaly_heatmap) | **GET** /api/rca/metrics/heatmap | Returns heatmap for the specified anomaly.  Aligns time stamps if necessary and omits null values.
*RootCauseAnalysisApi* | [**get_calendar_events**](docs/RootCauseAnalysisApi.md#get_calendar_events) | **GET** /api/rca/related/events | Returns calendar events related to the anomaly. Events are ordered by the scoring function.
*SubscriptionGroupApi* | [**count_with_predicate6**](docs/SubscriptionGroupApi.md#count_with_predicate6) | **GET** /api/subscription-groups/count | 
*SubscriptionGroupApi* | [**create_multiple6**](docs/SubscriptionGroupApi.md#create_multiple6) | **POST** /api/subscription-groups | 
*SubscriptionGroupApi* | [**delete6**](docs/SubscriptionGroupApi.md#delete6) | **DELETE** /api/subscription-groups/{id} | 
*SubscriptionGroupApi* | [**delete_all6**](docs/SubscriptionGroupApi.md#delete_all6) | **DELETE** /api/subscription-groups/all | 
*SubscriptionGroupApi* | [**edit_multiple6**](docs/SubscriptionGroupApi.md#edit_multiple6) | **PUT** /api/subscription-groups | 
*SubscriptionGroupApi* | [**get13**](docs/SubscriptionGroupApi.md#get13) | **GET** /api/subscription-groups/{id} | 
*SubscriptionGroupApi* | [**get14**](docs/SubscriptionGroupApi.md#get14) | **GET** /api/subscription-groups/name/{name} | 
*SubscriptionGroupApi* | [**get_all6**](docs/SubscriptionGroupApi.md#get_all6) | **GET** /api/subscription-groups | 
*SubscriptionGroupApi* | [**reset1**](docs/SubscriptionGroupApi.md#reset1) | **POST** /api/subscription-groups/{id}/reset | 
*TaskApi* | [**count_with_predicate10**](docs/TaskApi.md#count_with_predicate10) | **GET** /api/tasks/count | 
*TaskApi* | [**delete10**](docs/TaskApi.md#delete10) | **DELETE** /api/tasks/{id} | 
*TaskApi* | [**delete_all10**](docs/TaskApi.md#delete_all10) | **DELETE** /api/tasks/all | 
*TaskApi* | [**get21**](docs/TaskApi.md#get21) | **GET** /api/tasks/{id} | 
*TaskApi* | [**get22**](docs/TaskApi.md#get22) | **GET** /api/tasks/name/{name} | 
*TaskApi* | [**get_all10**](docs/TaskApi.md#get_all10) | **GET** /api/tasks | 
*TaskApi* | [**purge**](docs/TaskApi.md#purge) | **DELETE** /api/tasks/purge | 
*UIConfigurationApi* | [**get23**](docs/UIConfigurationApi.md#get23) | **GET** /api/ui/config | 
*ZzzAllEndpointsZzzApi* | [**clear_data_source_cache**](docs/ZzzAllEndpointsZzzApi.md#clear_data_source_cache) | **DELETE** /api/data-sources/cache | 
*ZzzAllEndpointsZzzApi* | [**count_with_predicate**](docs/ZzzAllEndpointsZzzApi.md#count_with_predicate) | **GET** /api/data-sources/count | 
*ZzzAllEndpointsZzzApi* | [**count_with_predicate1**](docs/ZzzAllEndpointsZzzApi.md#count_with_predicate1) | **GET** /api/datasets/count | 
*ZzzAllEndpointsZzzApi* | [**count_with_predicate10**](docs/ZzzAllEndpointsZzzApi.md#count_with_predicate10) | **GET** /api/tasks/count | 
*ZzzAllEndpointsZzzApi* | [**count_with_predicate2**](docs/ZzzAllEndpointsZzzApi.md#count_with_predicate2) | **GET** /api/metrics/count | 
*ZzzAllEndpointsZzzApi* | [**count_with_predicate3**](docs/ZzzAllEndpointsZzzApi.md#count_with_predicate3) | **GET** /api/alerts/count | 
*ZzzAllEndpointsZzzApi* | [**count_with_predicate4**](docs/ZzzAllEndpointsZzzApi.md#count_with_predicate4) | **GET** /api/alert-templates/count | 
*ZzzAllEndpointsZzzApi* | [**count_with_predicate5**](docs/ZzzAllEndpointsZzzApi.md#count_with_predicate5) | **GET** /api/enumeration-items/count | 
*ZzzAllEndpointsZzzApi* | [**count_with_predicate6**](docs/ZzzAllEndpointsZzzApi.md#count_with_predicate6) | **GET** /api/subscription-groups/count | 
*ZzzAllEndpointsZzzApi* | [**count_with_predicate7**](docs/ZzzAllEndpointsZzzApi.md#count_with_predicate7) | **GET** /api/anomalies/count | 
*ZzzAllEndpointsZzzApi* | [**count_with_predicate8**](docs/ZzzAllEndpointsZzzApi.md#count_with_predicate8) | **GET** /api/rca/investigations/count | 
*ZzzAllEndpointsZzzApi* | [**count_with_predicate9**](docs/ZzzAllEndpointsZzzApi.md#count_with_predicate9) | **GET** /api/events/count | 
*ZzzAllEndpointsZzzApi* | [**create_all_tables**](docs/ZzzAllEndpointsZzzApi.md#create_all_tables) | **POST** /internal/db-admin/create-all-tables | 
*ZzzAllEndpointsZzzApi* | [**create_multiple**](docs/ZzzAllEndpointsZzzApi.md#create_multiple) | **POST** /api/data-sources | 
*ZzzAllEndpointsZzzApi* | [**create_multiple1**](docs/ZzzAllEndpointsZzzApi.md#create_multiple1) | **POST** /api/datasets | 
*ZzzAllEndpointsZzzApi* | [**create_multiple2**](docs/ZzzAllEndpointsZzzApi.md#create_multiple2) | **POST** /api/metrics | 
*ZzzAllEndpointsZzzApi* | [**create_multiple3**](docs/ZzzAllEndpointsZzzApi.md#create_multiple3) | **POST** /api/alerts | 
*ZzzAllEndpointsZzzApi* | [**create_multiple4**](docs/ZzzAllEndpointsZzzApi.md#create_multiple4) | **POST** /api/alert-templates | 
*ZzzAllEndpointsZzzApi* | [**create_multiple5**](docs/ZzzAllEndpointsZzzApi.md#create_multiple5) | **POST** /api/enumeration-items | 
*ZzzAllEndpointsZzzApi* | [**create_multiple6**](docs/ZzzAllEndpointsZzzApi.md#create_multiple6) | **POST** /api/subscription-groups | 
*ZzzAllEndpointsZzzApi* | [**create_multiple7**](docs/ZzzAllEndpointsZzzApi.md#create_multiple7) | **POST** /api/anomalies | 
*ZzzAllEndpointsZzzApi* | [**create_multiple8**](docs/ZzzAllEndpointsZzzApi.md#create_multiple8) | **POST** /api/rca/investigations | 
*ZzzAllEndpointsZzzApi* | [**create_multiple9**](docs/ZzzAllEndpointsZzzApi.md#create_multiple9) | **POST** /api/events | 
*ZzzAllEndpointsZzzApi* | [**data_cube_summary**](docs/ZzzAllEndpointsZzzApi.md#data_cube_summary) | **GET** /api/rca/dim-analysis | Retrieve the likely root causes behind an anomaly
*ZzzAllEndpointsZzzApi* | [**delete**](docs/ZzzAllEndpointsZzzApi.md#delete) | **DELETE** /api/data-sources/{id} | 
*ZzzAllEndpointsZzzApi* | [**delete1**](docs/ZzzAllEndpointsZzzApi.md#delete1) | **DELETE** /api/datasets/{id} | 
*ZzzAllEndpointsZzzApi* | [**delete10**](docs/ZzzAllEndpointsZzzApi.md#delete10) | **DELETE** /api/tasks/{id} | 
*ZzzAllEndpointsZzzApi* | [**delete2**](docs/ZzzAllEndpointsZzzApi.md#delete2) | **DELETE** /api/metrics/{id} | 
*ZzzAllEndpointsZzzApi* | [**delete3**](docs/ZzzAllEndpointsZzzApi.md#delete3) | **DELETE** /api/alerts/{id} | 
*ZzzAllEndpointsZzzApi* | [**delete4**](docs/ZzzAllEndpointsZzzApi.md#delete4) | **DELETE** /api/alert-templates/{id} | 
*ZzzAllEndpointsZzzApi* | [**delete5**](docs/ZzzAllEndpointsZzzApi.md#delete5) | **DELETE** /api/enumeration-items/{id} | 
*ZzzAllEndpointsZzzApi* | [**delete6**](docs/ZzzAllEndpointsZzzApi.md#delete6) | **DELETE** /api/subscription-groups/{id} | 
*ZzzAllEndpointsZzzApi* | [**delete7**](docs/ZzzAllEndpointsZzzApi.md#delete7) | **DELETE** /api/anomalies/{id} | 
*ZzzAllEndpointsZzzApi* | [**delete8**](docs/ZzzAllEndpointsZzzApi.md#delete8) | **DELETE** /api/rca/investigations/{id} | 
*ZzzAllEndpointsZzzApi* | [**delete9**](docs/ZzzAllEndpointsZzzApi.md#delete9) | **DELETE** /api/events/{id} | 
*ZzzAllEndpointsZzzApi* | [**delete_all**](docs/ZzzAllEndpointsZzzApi.md#delete_all) | **DELETE** /api/data-sources/all | 
*ZzzAllEndpointsZzzApi* | [**delete_all1**](docs/ZzzAllEndpointsZzzApi.md#delete_all1) | **DELETE** /api/datasets/all | 
*ZzzAllEndpointsZzzApi* | [**delete_all10**](docs/ZzzAllEndpointsZzzApi.md#delete_all10) | **DELETE** /api/tasks/all | 
*ZzzAllEndpointsZzzApi* | [**delete_all2**](docs/ZzzAllEndpointsZzzApi.md#delete_all2) | **DELETE** /api/metrics/all | 
*ZzzAllEndpointsZzzApi* | [**delete_all3**](docs/ZzzAllEndpointsZzzApi.md#delete_all3) | **DELETE** /api/alerts/all | 
*ZzzAllEndpointsZzzApi* | [**delete_all4**](docs/ZzzAllEndpointsZzzApi.md#delete_all4) | **DELETE** /api/alert-templates/all | 
*ZzzAllEndpointsZzzApi* | [**delete_all5**](docs/ZzzAllEndpointsZzzApi.md#delete_all5) | **DELETE** /api/enumeration-items/all | 
*ZzzAllEndpointsZzzApi* | [**delete_all6**](docs/ZzzAllEndpointsZzzApi.md#delete_all6) | **DELETE** /api/subscription-groups/all | 
*ZzzAllEndpointsZzzApi* | [**delete_all7**](docs/ZzzAllEndpointsZzzApi.md#delete_all7) | **DELETE** /api/anomalies/all | 
*ZzzAllEndpointsZzzApi* | [**delete_all8**](docs/ZzzAllEndpointsZzzApi.md#delete_all8) | **DELETE** /api/rca/investigations/all | 
*ZzzAllEndpointsZzzApi* | [**delete_all9**](docs/ZzzAllEndpointsZzzApi.md#delete_all9) | **DELETE** /api/events/all | 
*ZzzAllEndpointsZzzApi* | [**delete_all_data**](docs/ZzzAllEndpointsZzzApi.md#delete_all_data) | **DELETE** /internal/db-admin/truncate-all-tables | 
*ZzzAllEndpointsZzzApi* | [**delete_all_tables**](docs/ZzzAllEndpointsZzzApi.md#delete_all_tables) | **DELETE** /internal/db-admin/drop-all-tables | 
*ZzzAllEndpointsZzzApi* | [**edit_multiple**](docs/ZzzAllEndpointsZzzApi.md#edit_multiple) | **PUT** /api/data-sources | 
*ZzzAllEndpointsZzzApi* | [**edit_multiple1**](docs/ZzzAllEndpointsZzzApi.md#edit_multiple1) | **PUT** /api/datasets | 
*ZzzAllEndpointsZzzApi* | [**edit_multiple2**](docs/ZzzAllEndpointsZzzApi.md#edit_multiple2) | **PUT** /api/metrics | 
*ZzzAllEndpointsZzzApi* | [**edit_multiple3**](docs/ZzzAllEndpointsZzzApi.md#edit_multiple3) | **PUT** /api/alerts | 
*ZzzAllEndpointsZzzApi* | [**edit_multiple4**](docs/ZzzAllEndpointsZzzApi.md#edit_multiple4) | **PUT** /api/alert-templates | 
*ZzzAllEndpointsZzzApi* | [**edit_multiple5**](docs/ZzzAllEndpointsZzzApi.md#edit_multiple5) | **PUT** /api/enumeration-items | 
*ZzzAllEndpointsZzzApi* | [**edit_multiple6**](docs/ZzzAllEndpointsZzzApi.md#edit_multiple6) | **PUT** /api/subscription-groups | 
*ZzzAllEndpointsZzzApi* | [**edit_multiple7**](docs/ZzzAllEndpointsZzzApi.md#edit_multiple7) | **PUT** /api/anomalies | 
*ZzzAllEndpointsZzzApi* | [**edit_multiple8**](docs/ZzzAllEndpointsZzzApi.md#edit_multiple8) | **PUT** /api/rca/investigations | 
*ZzzAllEndpointsZzzApi* | [**edit_multiple9**](docs/ZzzAllEndpointsZzzApi.md#edit_multiple9) | **PUT** /api/events | 
*ZzzAllEndpointsZzzApi* | [**evaluate**](docs/ZzzAllEndpointsZzzApi.md#evaluate) | **POST** /api/alerts/evaluate | 
*ZzzAllEndpointsZzzApi* | [**execute_query**](docs/ZzzAllEndpointsZzzApi.md#execute_query) | **GET** /internal/db-admin/execute-query | 
*ZzzAllEndpointsZzzApi* | [**generate_cohorts**](docs/ZzzAllEndpointsZzzApi.md#generate_cohorts) | **POST** /api/rca/metrics/cohorts | Builds cohorts based on threshold
*ZzzAllEndpointsZzzApi* | [**generate_html_email**](docs/ZzzAllEndpointsZzzApi.md#generate_html_email) | **GET** /internal/email/html | 
*ZzzAllEndpointsZzzApi* | [**get**](docs/ZzzAllEndpointsZzzApi.md#get) | **GET** /api/info | 
*ZzzAllEndpointsZzzApi* | [**get1**](docs/ZzzAllEndpointsZzzApi.md#get1) | **GET** /api/data-sources/{id} | 
*ZzzAllEndpointsZzzApi* | [**get10**](docs/ZzzAllEndpointsZzzApi.md#get10) | **GET** /api/alert-templates/name/{name} | 
*ZzzAllEndpointsZzzApi* | [**get11**](docs/ZzzAllEndpointsZzzApi.md#get11) | **GET** /api/enumeration-items/{id} | 
*ZzzAllEndpointsZzzApi* | [**get12**](docs/ZzzAllEndpointsZzzApi.md#get12) | **GET** /api/enumeration-items/name/{name} | 
*ZzzAllEndpointsZzzApi* | [**get13**](docs/ZzzAllEndpointsZzzApi.md#get13) | **GET** /api/subscription-groups/{id} | 
*ZzzAllEndpointsZzzApi* | [**get14**](docs/ZzzAllEndpointsZzzApi.md#get14) | **GET** /api/subscription-groups/name/{name} | 
*ZzzAllEndpointsZzzApi* | [**get15**](docs/ZzzAllEndpointsZzzApi.md#get15) | **GET** /api/anomalies/{id} | 
*ZzzAllEndpointsZzzApi* | [**get16**](docs/ZzzAllEndpointsZzzApi.md#get16) | **GET** /api/anomalies/name/{name} | 
*ZzzAllEndpointsZzzApi* | [**get17**](docs/ZzzAllEndpointsZzzApi.md#get17) | **GET** /api/rca/investigations/{id} | 
*ZzzAllEndpointsZzzApi* | [**get18**](docs/ZzzAllEndpointsZzzApi.md#get18) | **GET** /api/rca/investigations/name/{name} | 
*ZzzAllEndpointsZzzApi* | [**get19**](docs/ZzzAllEndpointsZzzApi.md#get19) | **GET** /api/events/{id} | 
*ZzzAllEndpointsZzzApi* | [**get2**](docs/ZzzAllEndpointsZzzApi.md#get2) | **GET** /api/data-sources/name/{name} | 
*ZzzAllEndpointsZzzApi* | [**get20**](docs/ZzzAllEndpointsZzzApi.md#get20) | **GET** /api/events/name/{name} | 
*ZzzAllEndpointsZzzApi* | [**get21**](docs/ZzzAllEndpointsZzzApi.md#get21) | **GET** /api/tasks/{id} | 
*ZzzAllEndpointsZzzApi* | [**get22**](docs/ZzzAllEndpointsZzzApi.md#get22) | **GET** /api/tasks/name/{name} | 
*ZzzAllEndpointsZzzApi* | [**get23**](docs/ZzzAllEndpointsZzzApi.md#get23) | **GET** /api/ui/config | 
*ZzzAllEndpointsZzzApi* | [**get3**](docs/ZzzAllEndpointsZzzApi.md#get3) | **GET** /api/datasets/{id} | 
*ZzzAllEndpointsZzzApi* | [**get4**](docs/ZzzAllEndpointsZzzApi.md#get4) | **GET** /api/datasets/name/{name} | 
*ZzzAllEndpointsZzzApi* | [**get5**](docs/ZzzAllEndpointsZzzApi.md#get5) | **GET** /api/metrics/{id} | 
*ZzzAllEndpointsZzzApi* | [**get6**](docs/ZzzAllEndpointsZzzApi.md#get6) | **GET** /api/metrics/name/{name} | 
*ZzzAllEndpointsZzzApi* | [**get7**](docs/ZzzAllEndpointsZzzApi.md#get7) | **GET** /api/alerts/{id} | 
*ZzzAllEndpointsZzzApi* | [**get8**](docs/ZzzAllEndpointsZzzApi.md#get8) | **GET** /api/alerts/name/{name} | 
*ZzzAllEndpointsZzzApi* | [**get9**](docs/ZzzAllEndpointsZzzApi.md#get9) | **GET** /api/alert-templates/{id} | 
*ZzzAllEndpointsZzzApi* | [**get_all**](docs/ZzzAllEndpointsZzzApi.md#get_all) | **GET** /api/data-sources | 
*ZzzAllEndpointsZzzApi* | [**get_all1**](docs/ZzzAllEndpointsZzzApi.md#get_all1) | **GET** /api/datasets | 
*ZzzAllEndpointsZzzApi* | [**get_all10**](docs/ZzzAllEndpointsZzzApi.md#get_all10) | **GET** /api/tasks | 
*ZzzAllEndpointsZzzApi* | [**get_all2**](docs/ZzzAllEndpointsZzzApi.md#get_all2) | **GET** /api/metrics | 
*ZzzAllEndpointsZzzApi* | [**get_all3**](docs/ZzzAllEndpointsZzzApi.md#get_all3) | **GET** /api/alerts | 
*ZzzAllEndpointsZzzApi* | [**get_all4**](docs/ZzzAllEndpointsZzzApi.md#get_all4) | **GET** /api/alert-templates | 
*ZzzAllEndpointsZzzApi* | [**get_all5**](docs/ZzzAllEndpointsZzzApi.md#get_all5) | **GET** /api/enumeration-items | 
*ZzzAllEndpointsZzzApi* | [**get_all6**](docs/ZzzAllEndpointsZzzApi.md#get_all6) | **GET** /api/subscription-groups | 
*ZzzAllEndpointsZzzApi* | [**get_all7**](docs/ZzzAllEndpointsZzzApi.md#get_all7) | **GET** /api/anomalies | 
*ZzzAllEndpointsZzzApi* | [**get_all8**](docs/ZzzAllEndpointsZzzApi.md#get_all8) | **GET** /api/rca/investigations | 
*ZzzAllEndpointsZzzApi* | [**get_all9**](docs/ZzzAllEndpointsZzzApi.md#get_all9) | **GET** /api/events | 
*ZzzAllEndpointsZzzApi* | [**get_analytics**](docs/ZzzAllEndpointsZzzApi.md#get_analytics) | **GET** /api/alerts/{id}/stats | 
*ZzzAllEndpointsZzzApi* | [**get_analytics_payload**](docs/ZzzAllEndpointsZzzApi.md#get_analytics_payload) | **GET** /api/app-analytics | 
*ZzzAllEndpointsZzzApi* | [**get_anomalies_events**](docs/ZzzAllEndpointsZzzApi.md#get_anomalies_events) | **GET** /api/rca/related/anomalies | Returns anomalies related to the anomaly. Anomalies are ordered by the scoring function.
*ZzzAllEndpointsZzzApi* | [**get_anomaly_heatmap**](docs/ZzzAllEndpointsZzzApi.md#get_anomaly_heatmap) | **GET** /api/rca/metrics/heatmap | Returns heatmap for the specified anomaly.  Aligns time stamps if necessary and omits null values.
*ZzzAllEndpointsZzzApi* | [**get_calendar_events**](docs/ZzzAllEndpointsZzzApi.md#get_calendar_events) | **GET** /api/rca/related/events | Returns calendar events related to the anomaly. Events are ordered by the scoring function.
*ZzzAllEndpointsZzzApi* | [**get_datasets**](docs/ZzzAllEndpointsZzzApi.md#get_datasets) | **GET** /api/data-sources/name/{name}/datasets | 
*ZzzAllEndpointsZzzApi* | [**get_entity**](docs/ZzzAllEndpointsZzzApi.md#get_entity) | **GET** /api/entities/types/{bean_class} | 
*ZzzAllEndpointsZzzApi* | [**get_entity_info**](docs/ZzzAllEndpointsZzzApi.md#get_entity_info) | **GET** /api/entities/types/{bean_class}/info | 
*ZzzAllEndpointsZzzApi* | [**get_insights**](docs/ZzzAllEndpointsZzzApi.md#get_insights) | **GET** /api/alerts/{id}/insights | 
*ZzzAllEndpointsZzzApi* | [**get_insights1**](docs/ZzzAllEndpointsZzzApi.md#get_insights1) | **POST** /api/alerts/insights | 
*ZzzAllEndpointsZzzApi* | [**get_package_info**](docs/ZzzAllEndpointsZzzApi.md#get_package_info) | **GET** /internal/package-info | 
*ZzzAllEndpointsZzzApi* | [**get_raw_entity**](docs/ZzzAllEndpointsZzzApi.md#get_raw_entity) | **GET** /api/entities/{id} | 
*ZzzAllEndpointsZzzApi* | [**get_tables**](docs/ZzzAllEndpointsZzzApi.md#get_tables) | **GET** /internal/db-admin/tables | 
*ZzzAllEndpointsZzzApi* | [**get_version**](docs/ZzzAllEndpointsZzzApi.md#get_version) | **GET** /api/app-analytics/version | 
*ZzzAllEndpointsZzzApi* | [**home**](docs/ZzzAllEndpointsZzzApi.md#home) | **GET** / | 
*ZzzAllEndpointsZzzApi* | [**list_entities**](docs/ZzzAllEndpointsZzzApi.md#list_entities) | **GET** /api/entities/types | 
*ZzzAllEndpointsZzzApi* | [**load_holidays**](docs/ZzzAllEndpointsZzzApi.md#load_holidays) | **POST** /api/events/create-from-anomaly | 
*ZzzAllEndpointsZzzApi* | [**load_holidays1**](docs/ZzzAllEndpointsZzzApi.md#load_holidays1) | **POST** /api/events/holidays/load | 
*ZzzAllEndpointsZzzApi* | [**load_recommended_templates**](docs/ZzzAllEndpointsZzzApi.md#load_recommended_templates) | **POST** /api/alert-templates/load-defaults | 
*ZzzAllEndpointsZzzApi* | [**login**](docs/ZzzAllEndpointsZzzApi.md#login) | **POST** /api/auth/login | 
*ZzzAllEndpointsZzzApi* | [**logout**](docs/ZzzAllEndpointsZzzApi.md#logout) | **POST** /api/auth/logout | 
*ZzzAllEndpointsZzzApi* | [**notify**](docs/ZzzAllEndpointsZzzApi.md#notify) | **POST** /internal/notify | 
*ZzzAllEndpointsZzzApi* | [**offboard_all**](docs/ZzzAllEndpointsZzzApi.md#offboard_all) | **DELETE** /api/data-sources/offboard-all | 
*ZzzAllEndpointsZzzApi* | [**onboard_all**](docs/ZzzAllEndpointsZzzApi.md#onboard_all) | **POST** /api/data-sources/onboard-all | 
*ZzzAllEndpointsZzzApi* | [**onboard_dataset**](docs/ZzzAllEndpointsZzzApi.md#onboard_dataset) | **POST** /api/data-sources/onboard-dataset | 
*ZzzAllEndpointsZzzApi* | [**ping**](docs/ZzzAllEndpointsZzzApi.md#ping) | **GET** /internal/ping | 
*ZzzAllEndpointsZzzApi* | [**post**](docs/ZzzAllEndpointsZzzApi.md#post) | **POST** /internal/http-detector | 
*ZzzAllEndpointsZzzApi* | [**purge**](docs/ZzzAllEndpointsZzzApi.md#purge) | **DELETE** /api/tasks/purge | 
*ZzzAllEndpointsZzzApi* | [**reset**](docs/ZzzAllEndpointsZzzApi.md#reset) | **POST** /api/alerts/{id}/reset | Delete associated anomalies and rerun detection till present
*ZzzAllEndpointsZzzApi* | [**reset1**](docs/ZzzAllEndpointsZzzApi.md#reset1) | **POST** /api/subscription-groups/{id}/reset | 
*ZzzAllEndpointsZzzApi* | [**run_task**](docs/ZzzAllEndpointsZzzApi.md#run_task) | **POST** /api/alerts/{id}/run | 
*ZzzAllEndpointsZzzApi* | [**set_feedback**](docs/ZzzAllEndpointsZzzApi.md#set_feedback) | **POST** /api/anomalies/{id}/feedback | 
*ZzzAllEndpointsZzzApi* | [**trigger_webhook**](docs/ZzzAllEndpointsZzzApi.md#trigger_webhook) | **POST** /internal/trigger/webhook | 
*ZzzAllEndpointsZzzApi* | [**validate**](docs/ZzzAllEndpointsZzzApi.md#validate) | **GET** /api/data-sources/validate | 
*ZzzAllEndpointsZzzApi* | [**validate_multiple**](docs/ZzzAllEndpointsZzzApi.md#validate_multiple) | **POST** /api/alerts/validate | 
*ZzzAllEndpointsZzzApi* | [**webhook_dummy**](docs/ZzzAllEndpointsZzzApi.md#webhook_dummy) | **POST** /internal/webhook | 
*ZzzAllEndpointsZzzApi* | [**worker_id**](docs/ZzzAllEndpointsZzzApi.md#worker_id) | **GET** /internal/worker/id | 
*ZzzInternalZzzApi* | [**create_all_tables**](docs/ZzzInternalZzzApi.md#create_all_tables) | **POST** /internal/db-admin/create-all-tables | 
*ZzzInternalZzzApi* | [**delete_all_data**](docs/ZzzInternalZzzApi.md#delete_all_data) | **DELETE** /internal/db-admin/truncate-all-tables | 
*ZzzInternalZzzApi* | [**delete_all_tables**](docs/ZzzInternalZzzApi.md#delete_all_tables) | **DELETE** /internal/db-admin/drop-all-tables | 
*ZzzInternalZzzApi* | [**execute_query**](docs/ZzzInternalZzzApi.md#execute_query) | **GET** /internal/db-admin/execute-query | 
*ZzzInternalZzzApi* | [**generate_html_email**](docs/ZzzInternalZzzApi.md#generate_html_email) | **GET** /internal/email/html | 
*ZzzInternalZzzApi* | [**get_package_info**](docs/ZzzInternalZzzApi.md#get_package_info) | **GET** /internal/package-info | 
*ZzzInternalZzzApi* | [**get_tables**](docs/ZzzInternalZzzApi.md#get_tables) | **GET** /internal/db-admin/tables | 
*ZzzInternalZzzApi* | [**notify**](docs/ZzzInternalZzzApi.md#notify) | **POST** /internal/notify | 
*ZzzInternalZzzApi* | [**ping**](docs/ZzzInternalZzzApi.md#ping) | **GET** /internal/ping | 
*ZzzInternalZzzApi* | [**post**](docs/ZzzInternalZzzApi.md#post) | **POST** /internal/http-detector | 
*ZzzInternalZzzApi* | [**trigger_webhook**](docs/ZzzInternalZzzApi.md#trigger_webhook) | **POST** /internal/trigger/webhook | 
*ZzzInternalZzzApi* | [**webhook_dummy**](docs/ZzzInternalZzzApi.md#webhook_dummy) | **POST** /internal/webhook | 
*ZzzInternalZzzApi* | [**worker_id**](docs/ZzzInternalZzzApi.md#worker_id) | **GET** /internal/worker/id | 


## Documentation For Models

 - [AccessControlModel](docs/AccessControlModel.md)
 - [AlertApiModel](docs/AlertApiModel.md)
 - [AlertEvaluationApiModel](docs/AlertEvaluationApiModel.md)
 - [AlertInsightsRequestApiModel](docs/AlertInsightsRequestApiModel.md)
 - [AlertMetadataApiModel](docs/AlertMetadataApiModel.md)
 - [AlertNodeApiModel](docs/AlertNodeApiModel.md)
 - [AlertResourceModel](docs/AlertResourceModel.md)
 - [AlertTemplateApiModel](docs/AlertTemplateApiModel.md)
 - [AlertTemplateResourceModel](docs/AlertTemplateResourceModel.md)
 - [AnomalyApiModel](docs/AnomalyApiModel.md)
 - [AnomalyFeedbackApiModel](docs/AnomalyFeedbackApiModel.md)
 - [AnomalyLabelApiModel](docs/AnomalyLabelApiModel.md)
 - [AnomalyResourceModel](docs/AnomalyResourceModel.md)
 - [ApiResourceModel](docs/ApiResourceModel.md)
 - [AppAnalyticsResourceModel](docs/AppAnalyticsResourceModel.md)
 - [AuthInfoResourceModel](docs/AuthInfoResourceModel.md)
 - [AuthResourceModel](docs/AuthResourceModel.md)
 - [CohortComputationApiModel](docs/CohortComputationApiModel.md)
 - [DataSourceApiModel](docs/DataSourceApiModel.md)
 - [DataSourceMetaApiModel](docs/DataSourceMetaApiModel.md)
 - [DataSourceResourceModel](docs/DataSourceResourceModel.md)
 - [DatasetApiModel](docs/DatasetApiModel.md)
 - [DatasetResourceModel](docs/DatasetResourceModel.md)
 - [DetectionDataApiModel](docs/DetectionDataApiModel.md)
 - [DetectionEvaluationApiModel](docs/DetectionEvaluationApiModel.md)
 - [DimensionFilterContributionApiModel](docs/DimensionFilterContributionApiModel.md)
 - [DurationModel](docs/DurationModel.md)
 - [EmailSchemeApiModel](docs/EmailSchemeApiModel.md)
 - [EntityResourceModel](docs/EntityResourceModel.md)
 - [EntityTagModel](docs/EntityTagModel.md)
 - [EnumerationItemApiModel](docs/EnumerationItemApiModel.md)
 - [EnumerationItemResourceModel](docs/EnumerationItemResourceModel.md)
 - [EvaluationContextApiModel](docs/EvaluationContextApiModel.md)
 - [EventApiModel](docs/EventApiModel.md)
 - [EventContextApiModel](docs/EventContextApiModel.md)
 - [EventResourceModel](docs/EventResourceModel.md)
 - [HttpDetectorResourceModel](docs/HttpDetectorResourceModel.md)
 - [InputApiModel](docs/InputApiModel.md)
 - [LinkModel](docs/LinkModel.md)
 - [LocaleModel](docs/LocaleModel.md)
 - [LogicalViewModel](docs/LogicalViewModel.md)
 - [MediaTypeModel](docs/MediaTypeModel.md)
 - [MetricApiModel](docs/MetricApiModel.md)
 - [MetricResourceModel](docs/MetricResourceModel.md)
 - [NewCookieModel](docs/NewCookieModel.md)
 - [NotificationSchemesApiModel](docs/NotificationSchemesApiModel.md)
 - [NotificationSpecApiModel](docs/NotificationSpecApiModel.md)
 - [NumberModel](docs/NumberModel.md)
 - [OutputApiModel](docs/OutputApiModel.md)
 - [PlanNodeApiModel](docs/PlanNodeApiModel.md)
 - [RcaDimensionAnalysisResourceModel](docs/RcaDimensionAnalysisResourceModel.md)
 - [RcaInvestigationApiModel](docs/RcaInvestigationApiModel.md)
 - [RcaInvestigationResourceModel](docs/RcaInvestigationResourceModel.md)
 - [RcaMetadataApiModel](docs/RcaMetadataApiModel.md)
 - [RcaMetricResourceModel](docs/RcaMetricResourceModel.md)
 - [RcaRelatedResourceModel](docs/RcaRelatedResourceModel.md)
 - [RcaResourceModel](docs/RcaResourceModel.md)
 - [ResponseModel](docs/ResponseModel.md)
 - [StatusTypeModel](docs/StatusTypeModel.md)
 - [SubscriptionGroupApiModel](docs/SubscriptionGroupApiModel.md)
 - [SubscriptionGroupResourceModel](docs/SubscriptionGroupResourceModel.md)
 - [TaskResourceModel](docs/TaskResourceModel.md)
 - [TemplatableListStringModel](docs/TemplatableListStringModel.md)
 - [TemplatableModel](docs/TemplatableModel.md)
 - [TemplatableObjectModel](docs/TemplatableObjectModel.md)
 - [TemplatePropertyMetadataModel](docs/TemplatePropertyMetadataModel.md)
 - [TemporalUnitModel](docs/TemporalUnitModel.md)
 - [TimeColumnApiModel](docs/TimeColumnApiModel.md)
 - [TimeWindowSuppressorApiModel](docs/TimeWindowSuppressorApiModel.md)
 - [UiResourceModel](docs/UiResourceModel.md)
 - [UriBuilderModel](docs/UriBuilderModel.md)
 - [UserApiModel](docs/UserApiModel.md)
 - [WebhookSchemeApiModel](docs/WebhookSchemeApiModel.md)


## Documentation For Authorization


## oauth

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Author



