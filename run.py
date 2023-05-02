from src.init_env import Start_Enviroment


def main():

    start = Start_Enviroment()
    start.evaluate_environment()
    start.create_airflow_folder()
    start.set_permissions()
    start.initialize_airflow()

    print(f"Your environment is now ready. Enjoy!")


if __name__ == '__main__':
    main()
