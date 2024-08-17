import os
import re
import errno
import configparser

def check_config(config_path:str) -> configparser.ConfigParser:

    if not os.path.exists(config_path):
        raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), config_path)
    
    return configparser.ConfigParser()

def remove_number(text:str) -> str:
    return re.sub(r"[0-9]+","",text)

def is_game_log_file(file_name:str) -> bool:
    return re.match("\d", file_name) is not None and re.search("ERROR\.log$", file_name) is None