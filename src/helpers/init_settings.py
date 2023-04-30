from backports import configparser
import os


config_object = configparser.ConfigParser()

config_object['SH_GET_AIRFLOW_YAML'] = {
    "get_ymal_file": "curl -LfO 'http://apache-airflow-docs.s3-website.eu-central-1.amazonaws.com/docs/apache-airflow/latest/docker-compose.yaml'"
}

config_object['SH_CREATE_FOLDERS'] = {
    "create_folder": "mkdir ./dags ./plugins ./logs"
}

config_object['SH_REMOVE_FOLDERS'] = {
    "remove_folder": "rm -rf ./dags ./plugins ./logs"
}

config_object['SH_GET_PERMISSIONS'] = {
    "create_folder": ascii("echo \nAIRFLOW_UID=$(id -u) \nAIRFLOW_GID=0 >> .env")
}

config_object['SH_INIT_SETUP'] = {
    "create_folder": "docker-compose up airflow-init",
    "start-service": "docker-compose up"
}

file_location = os.path.join('src/settings/','config.ini')

with open(file_location, 'w') as conf:
    config_object.write(conf)


