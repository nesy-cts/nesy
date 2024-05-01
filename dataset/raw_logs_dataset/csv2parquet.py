import pandas as pd

log_file = 'open_stack/open_stack_2.log_structured.csv'
logs = pd.read_csv(log_file)
logs.to_parquet(path='open_stack/open_stack_2.parquet')
