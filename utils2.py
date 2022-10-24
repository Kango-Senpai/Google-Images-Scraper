import time
from os import system
from os.path import exists
from random import randint as rnd
from resources import LogFile
def start_log():
    with open(LogFile.path,'a') as log_file:
        log_file.write(f"Program started at {time.asctime()}\n")

def log(message):
    with open(LogFile.path,'a') as log_file:
        log_file.write(message + "\n")

def safe_int(default_value,min_value,max_value):
    user_input = default_value
    cc = ""
    try:
        user_input = input(f"\nSelection: ")
        cc = user_input
        user_input = int(user_input) - 1
    except:
        user_input = default_value
        log(f"User input \"{cc}\" was invalid.")
    finally:
        if user_input < max_value and user_input > min_value:
            return user_input
        else:
            return default_value

def safe_string(default_value,message):
    user_input = default_value
    try:
        user_input = input(f"{message}")
    except:
        user_input = default_value
    finally:
        return user_input    

def generate_name(input_string):
    return_string = ""
    if len(input_string) > 5:
        for i in range(len(input_string)-1,len(input_string)-6,-1):
            return_string += input_string[i]
        return return_string
    else:
        return ""

def slim_list(old_list,size):
    new_list = old_list
    while len(new_list) > size:
        new_list.pop(rnd(0,len(new_list)-1))
    return new_list