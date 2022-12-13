# AlertTemplateApiModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**cron** | **str** |  | [optional] 
**created** | **datetime** |  | [optional] 
**updated** | **datetime** |  | [optional] 
**owner** | [**UserApiModel**](UserApiModel.md) |  | [optional] 
**nodes** | [**list[PlanNodeApiModel]**](PlanNodeApiModel.md) |  | [optional] 
**rca** | [**RcaMetadataApiModel**](RcaMetadataApiModel.md) |  | [optional] 
**metadata** | [**AlertMetadataApiModel**](AlertMetadataApiModel.md) |  | [optional] 
**default_properties** | **dict(str, object)** |  | [optional] 
**properties** | [**list[TemplatePropertyMetadataModel]**](TemplatePropertyMetadataModel.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


