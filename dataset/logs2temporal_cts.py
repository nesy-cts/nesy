import pandas as pd

system = 'open_stack'
if system == 'linux':
    category_name = 'app-name'
    frt = '%b %d %H:%M:%S'
elif system == 'windows':
    category_name = 'provider_name'
    # frt = '%Y-%m-%d %H:%M:%S.%f'
    # frt = 'ISO8601'
    frt = '%Y-%m-%d-%H%M%S'
elif system == 'hdfs':
    category_name = 'EventId'
else:
    category_name = 'EventId'


logs_location = "logs_dataset/" + system + "/logs_2.parquet"
temporal_cts_location = "temporal_cts_dataset/" + system + '_' + category_name + "/logs_2.parquet"

logs = pd.read_parquet(logs_location, engine='pyarrow')
temporal_cts = pd.DataFrame(data={'instant': logs['Date'].values, 'category': logs[category_name].values})
temporal_cts.instant = pd.to_datetime(temporal_cts.instant.astype(str), errors='coerce', infer_datetime_format=True)
temporal_cts.sort_values(by=['instant'], inplace=True, ignore_index=True)
temporal_cts.to_parquet(path=temporal_cts_location)
