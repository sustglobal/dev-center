# PhysicalRiskDatasetSummaryResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**portfolio_name** | **str** | Name of the corresponding portfolio | 
**portfolio_index** | **int** | Portfolio-scoped index of the asset | 
**entity_id** | **str** | ID of the asset | 
**entity_name** | **str** | Name of the asset | 
**window** | **int** | Size of annual summary window | 
**window_start_year** | **int** | Left boundary of window | 
**scenario** | **str** | Climate scenario | 
**risk_summaries** | [**[PhysicalRiskSummaryItem]**](PhysicalRiskSummaryItem.md) |  | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


