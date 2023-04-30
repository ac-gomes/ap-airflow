import subprocess
from os import getenv
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
GET_YAML = getenv('SH_GET_AIRFLOW_YAML')

CREATE_FOLDERS = getenv('SH_CREATE_FOLDERS')

REMOVE_FOLDERS = getenv('SH_REMOVE_FOLDERS')

GET_CONTAINERS_PERMISSIONS = getenv('SH_GET_PERMISSIONS')

# subprocess.run(YAML_URL, shell=True)
# subprocess.run(CREATE_FOLDERS, shell=True)
# subprocess.run(REMOVE_FOLDERS, shell=True)
# subprocess.run(GET_CONTAINERS_PERMISSIONS, shell=True)


nl=['5E','6E']
print(ord(nl))
