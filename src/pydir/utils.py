import platformdirs
import os
import colorama
import json


APP_AUTHOR = "R3dans"
APP_NAME = "Pydir"
USER_CONFIG=platformdirs.user_config_dir(APP_NAME, APP_AUTHOR)




os.makedirs(USER_CONFIG)


def debug(text):
    
    print(text)

