# AnomalyApiModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**start_time** | **datetime** |  | [optional] 
**end_time** | **datetime** |  | [optional] 
**avg_current_val** | **float** |  | [optional] 
**avg_baseline_val** | **float** |  | [optional] 
**score** | **float** |  | [optional] 
**weight** | **float** |  | [optional] 
**impact_to_global** | **float** |  | [optional] 
**source_type** | **str** |  | [optional] 
**created** | **datetime** |  | [optional] 
**notified** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 
**alert** | [**AlertApiModel**](AlertApiModel.md) |  | [optional] 
**alert_node** | [**AlertNodeApiModel**](AlertNodeApiModel.md) |  | [optional] 
**metric** | [**MetricApiModel**](MetricApiModel.md) |  | [optional] 
**metadata** | [**AlertMetadataApiModel**](AlertMetadataApiModel.md) |  | [optional] 
**children** | [**list[AnomalyApiModel]**](AnomalyApiModel.md) |  | [optional] 
**type** | **str** |  | [optional] 
**severity** | **str** |  | [optional] 
**feedback** | [**AnomalyFeedbackApiModel**](AnomalyFeedbackApiModel.md) |  | [optional] 
**enumeration_item** | [**EnumerationItemApiModel**](EnumerationItemApiModel.md) |  | [optional] 
**anomaly_labels** | [**list[AnomalyLabelApiModel]**](AnomalyLabelApiModel.md) |  | [optional] 
**child** | **bool** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


