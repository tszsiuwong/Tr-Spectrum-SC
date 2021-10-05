import os
import numpy as np
class FileData():
    def __init__(self, file, file_info) -> None:
        """
        file_info = {
        "f_path":f_path,
        "power_from": power_from,
        "power_to": power_to,
        "reverse": True,
        }
        """

        power_from = file_info["power_from"]
        power_to = file_info["power_to"]

        power = file[power_from:power_to]
        power_d = file[power_to+1:power_to+2]

        self.power = int(power)+int(power_d)/10

        file_name = file_info["f_path"] + file
        data = np.loadtxt(file_name)

        position = data[1:-1,1]
        time = data[1:-1,0]
        value = data[1:-1,2]

        self.file_name = file
        self.time = time
        self.position = position
        self.value = value
