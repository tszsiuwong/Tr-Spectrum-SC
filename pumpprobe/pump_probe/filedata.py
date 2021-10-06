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



        file_name = file_info["f_path"] + file
        data = np.loadtxt(file_name)

        position = data[1:-1,1]
        time = data[1:-1,0]
        value = data[1:-1,2]

        self.power = int(power)+int(power_d)/10
        self.file_name = file
        self.time = time
        self.position = position
        self.value = value

    def get_peak_position(self):
        position = np.argmax(abs(self.value))
        return self.time[position]

    def set_time_position_at_peak(self, time_peak_position):
        self.time -= time_peak_position

    def set_value_to_zero(self):
        """Subtracting the dorsal base before the signal comes
        Args:
            None
        Return:
            None
        """
        self.value -= self.value[0]




