from backports import configparser
import subprocess

from init_settings import Config_File


class Start_Enviroment:
    """This will create config file to initialize"""

    config = Config_File()
    config_object = config.sh_parser()
    config.write_config_file()



    # def
    # config_object = configparser.ConfigParser()
    # config_object.read("src/settings/config.ini")
    # GET_YAML = config_object["SH_GET_AIRFLOW_YAML"]

    # print(GET_YAML["get_ymal_file"])
    # subprocess.run(GET_YAML["get_ymal_file"], shell=True)