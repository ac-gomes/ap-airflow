from backports import configparser
import os

from os import getenv
from dotenv import load_dotenv, find_dotenv


class Config_File:
    """Class to create config file"""

    def __init__(self):
        self.config_object = configparser.ConfigParser()

    def sh_parser(self) -> None:
        """This method will receive all shell commands and prepare it to write to the config file"""

        self.config_object['SH_GET_AIRFLOW_YAML'] = {
            "get_ymal_file": "curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.6.0/docker-compose.yaml'"
        }

        self.config_object['SH_CREATE_FOLDERS'] = {
            "create_folder": "mkdir ./dags ./plugins ./logs"
        }

        self.config_object['SH_REMOVE_FOLDERS'] = {
            "remove_folder": "rm -rf ./dags ./plugins ./logs"
        }

        self.config_object['SH_INIT_SETUP'] = {
            "airflow_init": 'docker compose up airflow-init',
            "start_service": 'docker compose up -d'
        }

    def write_config_file(self) -> None:
        """This method will write the configuration file to disk"""

        file_location = os.path.join('src/settings/', 'config.ini')

        try:
            with open(file_location, 'w') as conf:
                self.config_object.write(conf)

        except Exception as error:
            print("Something went wrong with the contents of the configuration file: {} ".format(error))


class Config_file_Exist:
    """check if the config file exists"""
    def __init__(self) -> None:
        load_dotenv(find_dotenv())
        self.file_path = getenv('CONFIG_FILE_PATH')

    def exist_file(self) -> list:

        try:
            file_exist = os.path.exists(self.file_path)
            return [file_exist, self.file_path]
        except Exception as error:
            print("Something went wrong {}".format(error))
