from backports import configparser
import subprocess


from helpers.init_settings import Config_File, Config_file_Exist


class Start_Enviroment:
    """This will create config file to initialize"""

    def __init__(self) -> None:
        self.config_object = configparser.ConfigParser()
        self.check_file = Config_file_Exist()
        self.file_exist = self.check_file.exist_file()

    def evaluate_environment(self):

        config = Config_File()
        config.sh_parser()
        config.write_config_file()


        if self.file_exist[0]:
            self.config_object.read(self.file_exist[1])  #"src/settings/config.ini"
            GET_YAML = self.config_object["SH_GET_AIRFLOW_YAML"]
            print(GET_YAML["get_ymal_file"])
            # subprocess.run(GET_YAML["get_ymal_file"], shell=True)

    def create_airflow_folder(self):
        print(self.file_exist)

        if self.file_exist[0]:
            self.config_object.read(self.file_exist[1])
            FOLDERS = self.config_object["SH_CREATE_FOLDERS"]
            print(FOLDERS["create_folder"])
            # subprocess.run(FOLDERS["create_folder"], shell=True)


init_a = Start_Enviroment()

init_a.evaluate_environment()
# init_a.create_airflow_folder()
