def close_app(app_name: str | int | None , using_file_name: bool | None = None):
    """
    This function closes any application using its pid or the application's name

    :param app_name: -The app you want to terminate
    :type app_name: str | int | None
    :param using_file_name: -If you want to use the file name to terminate an application
    :type using_file_name: bool | None = None


    ###### - [psutil](https://psutil.readthedocs.io/en/latest/)
    ###### - [os](https://docs.python.org/3/library/os.html)
    """
    import psutil
    import os

    fname = os.path.splitext(os.path.basename(__file__))[0] # . . .

    if using_file_name == False:
            for proc2 in psutil.process_iter(['pid', 'name']):
                pid = proc2.info['pid']

                if str(app_name).lower() in proc2.info['name'].lower():
                    try:
                        psutil.Process(pid).terminate()
                    except (psutil.AccessDenied, psutil.NoSuchProcess):
                        print("nuh")

                if isinstance(app_name, int) and proc2.info['pid'] == app_name:
                    try:
                        psutil.Process(app_name).terminate()
                    except (psutil.AccessDenied, psutil.NoSuchProcess):
                        print("peh")

    if using_file_name:
        for proc2 in psutil.process_iter(['pid', 'name']):
                pid = proc2.info['pid']

                if str(fname).lower() in proc2.info['name'].lower():
                    try:
                        psutil.Process(pid).terminate()
                    except (psutil.AccessDenied, psutil.NoSuchProcess):
                        print("nuh")

                if proc2.info['pid'] == fname:
                    try:
                        psutil.Process(int(fname)).terminate()
                    except (psutil.AccessDenied, psutil.NoSuchProcess):
                        print("peh")
    return
#  #  #  #  #  #  #  #  #  #
if __name__ == "__main__":
    close_app('app')
    # close_app('app', True) ## Does not use the app_name parameter
    # close_app(None, True)
    # close_app('app', None)
