import os
import pandas as pd
import pyarrow.parquet as pq
import pyarrow as pa
import glob
import time

os.chdir('..')
files_path = glob.glob('tmp/parquets/*')


def main():
    st = time.time()
    parquet_file = 'windows/logs.parquet'
    if os.path.exists(parquet_file):
        os.remove(parquet_file)

    schema = pa.schema([('logged_at', pa.string()), ('provider_name', pa.string()), ('level', pa.string()),
                        ('keywords', pa.string()), ('event_id', pa.int32()), ('event_record_id', pa.int64()),
                        ('task', pa.string()), ('computer', pa.string()), ('all_info', pa.string())])
    pqwriter = pq.ParquetWriter(parquet_file, schema)

    for i, file in enumerate(files_path):
        print(' ')
        print(f'File n°{i}')
        print('Name: ', file)

        logs = pd.read_parquet(file, engine='pyarrow')
        logs.columns = ['logged_at', 'provider_name', 'level', 'keywords', 'event_id', 'event_record_id',
                        'task', 'computer', 'all_info']
        table = pa.Table.from_pandas(logs)
        pqwriter.write_table(table)

    # close the parquet writer
    if pqwriter:
        pqwriter.close()
    print(f'main timing: {time.time() - st}')


if __name__ == '__main__':
    main()
