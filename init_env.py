from backports import configparser
import subprocess

from os import getenv
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
root = getenv('PYTHONPATH')

config_object = configparser.ConfigParser()
config_object.read("src/settings/config.ini")
GET_YAML = config_object["SH_GET_AIRFLOW_YAML"]

print(GET_YAML["get_ymal_file"])
subprocess.run(GET_YAML["get_ymal_file"], shell=True)
