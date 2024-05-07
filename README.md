# Nesy

## Synthetic Data

All the code to generate the different scenarios are in the folder /markov_chain. 

You can generate several CTS for each scenario by changing the name line 8 (or 7) and the seed parameter line 22 (or 17).


## Raw Logs Dataset

Logs always need preprocessing before use. For instance, windows logs are stored in evtx files and needs an extraction its own.

However, all the other types of logs are stored in text files .log, and need a parsing with regex. To this end, we use the library logparser from logpai that we referenced in our paper.

All the code for this preprocessing are stored in /dataset/raw_logs_dataset and there is one converter for each type of logs. There is also one file to convert the resulting csv to parquet file. 


## Logs Dataset

You can convert the logs to CTS thanks to the /dataset/logs2temporal_cts.py and /dataset/temporal_cts2cts.py files. 