from backports import configparser
import subprocess


from .init_settings import Config_File, Config_file_Exist


class Start_Enviroment:
    """This will create config file to initialize"""

    def __init__(self) -> None:
        self.config_object = configparser.ConfigParser()
        self.check_file = Config_file_Exist()
        self.file_exist = self.check_file.exist_file()

    def evaluate_environment(self) -> None:

        config = Config_File()
        config.sh_parser()
        config.write_config_file()

        if self.file_exist[0]:
            self.config_object.read(self.file_exist[1])
            GET_YAML = self.config_object["SH_GET_AIRFLOW_YAML"]
            subprocess.run(GET_YAML["get_ymal_file"], shell=True)

    def create_airflow_folder(self) -> None:

        if self.file_exist[0]:
            self.config_object.read(self.file_exist[1])
            FOLDERS = self.config_object["SH_CREATE_FOLDERS"]
            subprocess.run(FOLDERS["create_folder"], shell=True)

    def set_permissions(self) -> None:

        if self.file_exist[0]:
            self.config_object.read(self.file_exist[1])
            subprocess.run('echo "\nAIRFLOW_UID=$(id -u)\nAIRFLOW_GID=0" >> .env', shell=True)

    def initialize_airflow(self) -> None:
        if self.file_exist[0]:
            self.config_object.read(self.file_exist[1])
            INIT_SETUP = self.config_object["SH_INIT_SETUP"]
            subprocess.run(INIT_SETUP["airflow_init"], shell=True)
            subprocess.run(INIT_SETUP["start_service"], shell=True)
