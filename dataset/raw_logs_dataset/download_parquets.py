from botocore.config import Config
import boto3
import datetime
import os
import glob

os.chdir('..')

my_config = Config(
    proxies={'https': 'https://ecs.xefi.fr'},
    s3={'addressing_style': 'path'},
    proxies_config={'proxy_use_forwarding_for_https': True}
)


def delete_parquet_files():
    files_path = glob.glob('tmp/parquets/*.parquet')
    for file_path in files_path:
        os.remove(file_path)


def date_in_range(key, begin_date, end_date):
    date_string = str(key).split('/')[-3]
    date = datetime.datetime.strptime(date_string, '%Y-%m-%d')
    begin_date = datetime.datetime.strptime(begin_date, '%Y-%m-%d-%H%M%S')
    end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d-%H%M%S')
    return begin_date.date() <= date.date() <= end_date.date()


begin_date = '2023-07-20-000000'
end_date = '2023-07-26-000000'

delete_parquet_files()
s3 = boto3.resource('s3',
                    aws_access_key_id='key_id',
                    aws_secret_access_key='access_key',
                    config=my_config)
bucket = s3.Bucket('xfi-hypervision-bkt-01')
# key = 'dev/XEFI_VENDOME/45037F10-A590-E811-816B-00155D142918/DESKTOP-0B3KG52-1686317819/'
key = 'dev/XEFI_NIMES/BF306BB5-9D90-E811-816B-00155D142918/HVZ-windows-10-1682609225/'
objs = list(bucket.objects.filter(Prefix=key))

counter = 0
for i, obj in enumerate(objs):
    if obj.key.endswith('.parquet'):
        if date_in_range(obj.key, begin_date, end_date):
            file_name = str(obj.key).split('/')[-1]
            print(file_name)
            print()
            # print(str(obj.key).split('/')[-2])
            print(' ')
            counter += 1
            bucket.download_file(Key=obj.key,
                                 Filename='tmp/parquets/' + str(i) + '_' + file_name)
print("total de fichiers traités : ", counter)
