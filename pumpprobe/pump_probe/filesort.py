import os

def file_sort(file_info, reverse):
    f_path = file_info["f_path"]
    para_from = file_info["para_from"]
    para_to = file_info["para_to"]
    files = os.listdir(f_path)
    
    files.sort(key= lambda x:int(x[para_from:para_to]))
    if reverse:
        files.reverse()

    num_files = len(files)
    if reverse:
        num_para_max = 0
    else:
        num_para_max = num_files
    
    return files, num_files, num_para_max