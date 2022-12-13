# SubscriptionGroupApiModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**active** | **bool** |  | [optional] 
**type** | **str** |  | [optional] 
**alerts** | [**list[AlertApiModel]**](AlertApiModel.md) |  | [optional] 
**cron** | **str** |  | [optional] 
**created** | **datetime** |  | [optional] 
**updated** | **datetime** |  | [optional] 
**owner** | [**UserApiModel**](UserApiModel.md) |  | [optional] 
**specs** | [**list[NotificationSpecApiModel]**](NotificationSpecApiModel.md) |  | [optional] 
**notification_schemes** | [**NotificationSchemesApiModel**](NotificationSchemesApiModel.md) |  | [optional] 
**alert_suppressors** | [**TimeWindowSuppressorApiModel**](TimeWindowSuppressorApiModel.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


