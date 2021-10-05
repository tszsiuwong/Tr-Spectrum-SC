import os

def file_sort(file_info):
    f_path = file_info["f_path"]
    reverse = file_info["reverse"]
    power_from = file_info["power_from"]
    power_to = file_info["power_to"]
    files = os.listdir(f_path)

    files.sort(key= lambda x:int(x[power_from:power_to]))
    if reverse:
        files.reverse()
    return files