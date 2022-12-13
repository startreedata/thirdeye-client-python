# AlertApiModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**template** | [**AlertTemplateApiModel**](AlertTemplateApiModel.md) |  | [optional] 
**template_properties** | **dict(str, object)** |  | [optional] 
**cron** | **str** |  | [optional] 
**last_timestamp** | **datetime** |  | [optional] 
**active** | **bool** |  | [optional] 
**created** | **datetime** |  | [optional] 
**updated** | **datetime** |  | [optional] 
**owner** | [**UserApiModel**](UserApiModel.md) |  | [optional] 
**subscription_groups** | [**list[SubscriptionGroupApiModel]**](SubscriptionGroupApiModel.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


