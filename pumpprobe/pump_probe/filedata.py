import os
import numpy as np
from scipy.optimize import curve_fit

class FileData():
    def __init__(self, file, file_info) -> None:
        """
        file_info = {
        "f_path":f_path,
        "para_from": para_from,
        "para_to": para_to,
        "reverse": True,
        }
        """

        para_from = file_info["para_from"]
        para_to = file_info["para_to"]

        para = file[para_from:para_to]
        para_d = file[para_to+1:para_to+2]

        file_name = file_info["f_path"] + file
        data = np.loadtxt(file_name)

        position = data[1:-1,1]
        time = data[1:-1,0]
        value = data[1:-1,2]
        # parameter
        self.para = int(para)+int(para_d)/10
        # 
        self.file_name = file

        self.time = time
        self.position = position
        self.value = value

        self.time_from_zeros = time
        self.value_from_zeros = value

        self.value_fit = value
        
        self.A_1 = 0
        self.A_2 = 0
        self.tau_1 = 0
        self.tau_2 = 0
        self.tau_1_err = 0
        self.tau_2_err = 0


    def get_peak_position(self):
        peak_position = np.argmax(abs(self.value))
        return peak_position

    def set_time_position_at_peak(self, peak_position):
        self.time -= self.time[peak_position]
        self.time_from_zeros = self.time[peak_position:-1]
        self.value_from_zeros = self.value[peak_position:-1]


    def set_value_to_zero(self):
        """Subtracting the dorsal base before the signal comes
        Args:
            None
        Return:
            None
        """
        self.value -= self.value[0]


    def decay_fit(self, double_exp, fit_para_init):
        popt, pcov = curve_fit(double_exp, self.time_from_zeros, self.value_from_zeros, fit_para_init)
        b = popt[0]
        c = popt[1]
        p = popt[2]
        q = popt[3]
        self.value_fit = double_exp(self.time_from_zeros, b, c, p, q)
        self.A_1 = b
        self.A_2 = c
        self.tau_1 = -p
        self.tau_1_err = pcov[1,1]
        self.tau_2 = -q
        self.tau_2_n = pcov[3,3]
