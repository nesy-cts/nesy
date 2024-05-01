import glob
import pandas as pd
import pyarrow.parquet as pq
import pyarrow as pa
from joblib import Parallel, delayed
import os
import time

os.chdir('..')
files_path = glob.glob('tmp/syslog/*')


def parse_one_log(log):
    log_split = log.split(' ')
    while '' in log_split:
        log_split.remove('')
    date = log_split[0] + ' ' + log_split[1] + ' ' + log_split[2]
    hostname = log_split[3]

    app_name_pid = log_split[4]
    if '[' in app_name_pid:
        app_name_pid = app_name_pid.split('[')
        app_name = app_name_pid[0]
        pid = app_name_pid[1][:-2:]
    else:
        app_name = app_name_pid[:-1:]
        pid = None

    message = ' '.join(log_split[5::])
    return date, hostname, app_name, pid, message


def main():
    st = time.time()
    parquet_file = 'linux/logs.parquet'
    if os.path.exists(parquet_file):
        os.remove(parquet_file)

    schema = pa.schema([('logged_at', pa.string()), ('hostname', pa.string()), ('app_name', pa.string()),
                        ('process_id', pa.string()), ('message', pa.string())])
    pqwriter = pq.ParquetWriter(parquet_file, schema)

    for i, file in enumerate(files_path):
        print(' ')
        print(f'File n°{i}')
        print('Name: ', file)
        with open(file, 'r') as f:
            file_string = f.read()
            logs = file_string.split("\n")
            logs = logs[:-1:]

            logs = Parallel(n_jobs=10)(
                delayed(parse_one_log)(log) for log in logs
            )
            if len(logs) != 0:
                logs = pd.DataFrame(logs)
                logs.columns = ['logged_at', 'hostname', 'app-name', 'process_id', 'message']
                table = pa.Table.from_pandas(logs)
                pqwriter.write_table(table)


    # close the parquet writer
    if pqwriter:
        pqwriter.close()
    print(f'main timing: {time.time() - st}')


if __name__ == '__main__':
    main()
