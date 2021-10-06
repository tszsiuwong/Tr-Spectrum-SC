import os

def file_sort(file_info, reverse):
    f_path = file_info["f_path"]
    power_from = file_info["power_from"]
    power_to = file_info["power_to"]
    files = os.listdir(f_path)
    
    files.sort(key= lambda x:int(x[power_from:power_to]))
    if reverse:
        files.reverse()

    num_files = len(files)
    if reverse:
        num_power_max = 0
    else:
        num_power_max = num_files
    
    return files, num_files, num_power_max