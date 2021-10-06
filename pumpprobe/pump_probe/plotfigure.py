import numpy as np

class PlotFigure:
    def __init__(self, plt, fileData_list, num_files) -> None:
        self.plt = plt
        self.fileData_list = fileData_list
        self.num_files = num_files

    def plot_time_domain(self, color_bar_style, with_fit_lines):
        color_list = self.generating_color(color_bar_style)

        plt = self.plt
        
        plt.figure(figsize=(16,12))
        plt.rcParams['xtick.direction'] = 'in' 
        plt.rcParams['ytick.direction'] = 'in'

        shift = 0.0

        i = 0

        for file_data in self.fileData_list:
            time = file_data.time
            value_t = file_data.value
            para = file_data.para

            time_from_zeros = file_data.time_from_zeros
            value_fit = file_data.value_fit
        #     if i <3:
        #         value_t = value_t*0.3
        #         plt.text(time[-1]-2,value_t[-1]+0.2,r'$\times$0.3',fontdict={'size':'28','color':color_list[i]})
        #     if i == len(files)-1:
        #         plt.plot(time,value_t+0*(len(files)-i-1),label=str(int(para*10))+r" $\mu$J cm$^{-2}$",color=color_list[i],linewidth=3)
        #     else:
            plt.plot(time, value_t+shift*(self.num_files-i-1),label=str(int(para*10)),color=color_list[i],linewidth=3)
            if with_fit_lines:
                plt.plot(time_from_zeros, value_fit, '--k')
            i += 1

        plt.xticks(fontsize=40)
        plt.yticks(fontsize=40)
        plt.xlabel('Time Delay (ps)',fontsize=40)
        plt.ylabel(r'$\Delta$R/R (10$^{-4}$)',fontsize=40)
        plt.legend(fontsize=17,frameon=False,loc='lower left')

        set_lw = 3
        ax=plt.gca()
        ax.spines['bottom'].set_linewidth(set_lw)
        ax.spines['left'].set_linewidth(set_lw)
        ax.spines['right'].set_linewidth(set_lw)
        ax.spines['top'].set_linewidth(set_lw)


        for tickline in ax.xaxis.get_ticklines():
            tickline.set_markersize(10)
            tickline.set_markeredgewidth(5)
        for tickline in ax.yaxis.get_ticklines():
            tickline.set_markersize(10)
            tickline.set_markeredgewidth(5)
        ax.yaxis.set_ticks_position("left")
        ax.xaxis.set_ticks_position("bottom")

        if with_fit_lines:
            name = 'output/Power dependent time domain with fits.eps'
        else:
            name = 'output/Power dependent time domain.eps'

        plt.savefig(name, bbox_inches = 'tight')
        plt.show()


    def generating_color(self, color_bar_style):
        if color_bar_style == "rainbow" or "rainbow_r":
            num = self.num_files//4 - 1
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
            for i in range(self.num_files):
                color_list.append([Color_R[i], Color_G[i], Color_B[i]])

        return color_list