import pandas as pd
import pickle
from realizing_space.cts import CTS

temporal_cts_location = "temporal_cts_dataset/open_stack_EventId/logs_2.parquet"
cts_location = "cts_dataset/open_stack_logs_2.pickle"

temporal_cts = pd.read_parquet(temporal_cts_location, engine='pyarrow')

cts = CTS(series=temporal_cts.category.to_list())

with open(cts_location, "wb") as cts_file:
    pickle.dump(obj=cts, file=cts_file)
