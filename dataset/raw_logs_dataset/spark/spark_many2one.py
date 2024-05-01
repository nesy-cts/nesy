import glob
import os

applications_path = glob.glob('application_*')

for application in applications_path:
    os.system('cp -r -u ' + application + '/* all')