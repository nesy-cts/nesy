## Books

### French
A French book is a txt file written in French.



## Raw Logs

### Linux
Raw logs in linux are syslog file.

### Windows
Raw logs in windows are evtx file.



## Logs
Logs are parquet files.

### Linux
The schema in linux is :
- `logged_at : string`
- `hostname : string`
- `app-name : string`
- `process_id : string`
- `message : string`


### Windows
The schema in windows is :
- `logged_at : string`
- `provider_name : string`
- `level : string`
- `keywords : string`
- `event_id : int`
- `event_record_id : int`
- `task : string`
- `computer : string`
- `all_info : string`



## Temporal CTS
Temporal CTS are parquet file.
The schema is :
- `instant : string`
- `category : string`

## CTS
CTS are parquet file.
The schema is :
- `category : string`
