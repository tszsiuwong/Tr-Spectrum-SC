import numpy as np

def generating_color(num_files, color_bar_style):
    if color_bar_style == "rainbow" or "rainbow_r":
        num = num_files//4 - 1
        Color_R = np.append(np.linspace(227,34,5),np.linspace(37,0,num))
        Color_R = np.append(Color_R,np.linspace(1,0,num))
        Color_R = np.append(Color_R,np.linspace(1,230,num))
        Color_R = np.append(Color_R,np.linspace(230,229,num))

        Color_G = np.append(np.linspace(0,34,5),np.linspace(35,160,num))
        Color_G = np.append(Color_G,np.linspace(161,151,num))
        Color_G = np.append(Color_G,np.linspace(150,230,num))
        Color_G = np.append(Color_G,np.linspace(230,31,num))

        Color_B = np.append(np.linspace(126,136,5),np.linspace(135,223,num))
        Color_B = np.append(Color_B,np.linspace(222,75,num))
        Color_B = np.append(Color_B,np.linspace(74,0,num))
        Color_B = np.append(Color_B,np.linspace(1,31,num))

        if color_bar_style == "rainbow_r":
            Color_R = Color_R[::-1]/255
            Color_G = Color_G[::-1]/255
            Color_B = Color_B[::-1]/255
        else:
            Color_R = Color_R/255
            Color_G = Color_G/255
            Color_B = Color_B/255

        color_list = []
        for i in range(num_files):
            color_list.append([Color_R[i], Color_G[i], Color_B[i]])

    return color_list