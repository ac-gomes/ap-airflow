from src.init_env import Start_Environment


def main():

    start = Start_Environment()
    start.evaluate_environment()
    start.create_airflow_folder()
    start.set_permissions()
    start.initialize_airflow()

    print("""
        \ndefault Login: airflow
        \ndefault password: airflow
        \nYour environment is now ready. Enjoy!""")


if __name__ == '__main__':
    main()
