import numpy as np

class PlotFigure:
    def __init__(self, plt, fileData_list, num_files) -> None:
        self.plt = plt
        self.fileData_list = fileData_list
        self.num_files = num_files

    def plot_time_domain(self, plot_info):
        color_bar_style = plot_info["color_bar_style"]
        with_fit_lines = plot_info["with_fit_lines"]
        figsize = plot_info["figsize"]
        xlim = plot_info["xlim"]
        color_list = self.generating_color(color_bar_style)
        plt = self.plt
        
        plt.figure(figsize=figsize)
        plt.rcParams['xtick.direction'] = 'in' 
        plt.rcParams['ytick.direction'] = 'in'

        shift = plot_info["shift"]

        i = 0

        for file_data in self.fileData_list:
            time = file_data.time
            value_t = file_data.value
            para = file_data.para

            time_from_zeros = file_data.time_from_zeros
            value_fit = file_data.value_fit
            plt.plot(time, value_t+shift*(self.num_files-i-1),
            label=str(int(para)),color=color_list[i],linewidth=3)
            if with_fit_lines:
                plt.plot(time_from_zeros, 
                value_fit+shift*(self.num_files-i-1), '--k')
            if plot_info["marker"] == "text":
                plt.text(-1.4,(shift)*(self.num_files-i-1)+0.01,str(para)+'K',
                fontdict={'size':'20','color':color_list[i]})
            i += 1

        plt.xticks(fontsize=40)
        plt.yticks(fontsize=40)
        plt.xlabel('Time Delay (ps)',fontsize=40)
        plt.ylabel(r'$\Delta$R/R (10$^{-4}$)',fontsize=40)

        if plot_info["marker"] == "legend":
            plt.legend(fontsize=17,frameon=False,loc='lower left')
        
        plt.xlim(xlim)
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
            name = 'output/para dependent time domain with fits.eps'
        else:
            name = 'output/para dependent time domain.eps'

        plt.savefig(name, bbox_inches = 'tight')
        plt.show()

    def plot_fre_domain(self, plot_info):
        color_bar_style = plot_info["color_bar_style"]
        shift = plot_info["shift"]
        figsize = plot_info["figsize"]
        xlim = plot_info["xlim"]
        ylim = plot_info["ylim"]

        color_list = self.generating_color(color_bar_style)
        plt = self.plt

        plt.figure(figsize=figsize)
        i = 0
        for file_data in self.fileData_list:

            fre = file_data.frequency
            value_f = file_data.value_f
            para = file_data.para

            # if para == 0.5 or para == 2.3 or para == 5.5 or para == 12.5:
            #     plt.text(5,value_f[-1]+shift*(self.num_files-i)+2,
            #     str(para),fontdict={'size':'20','color':color_list[i]})
            # if para == 30:
            #     plt.text(5,value_f[-1]+shift*(self.num_files-i)+4,
            #     str(para)+r' $\mu$ J cm$^{-2}$',fontdict={'size':'20','color':color_list[i]})

            plt.plot(fre,value_f+shift*(self.num_files-i),color=color_list[i],linewidth=2)
            i += 1


        plt.xticks(fontsize=40)
        plt.yticks((),fontsize=40)
        plt.xlabel('Frequency (THz)',fontsize=40)
        plt.ylabel('arb. units', fontsize=40)

        set_lw = 3
        ax=plt.gca()
        ax.spines['bottom'].set_linewidth(set_lw)
        ax.spines['left'].set_linewidth(set_lw)
        ax.spines['right'].set_linewidth(set_lw)
        ax.spines['top'].set_linewidth(set_lw)
        plt.xlim(xlim)
        plt.ylim(ylim)

        for tickline in ax.xaxis.get_ticklines():
            tickline.set_markersize(10)
            tickline.set_markeredgewidth(5)
        for tickline in ax.yaxis.get_ticklines():
            tickline.set_markersize(10)
            tickline.set_markeredgewidth(5)
        ax.yaxis.set_ticks_position("left")
        ax.xaxis.set_ticks_position("bottom")

        plt.savefig('output/Fluence dependent fre domain.eps',bbox_inches = 'tight')
        plt.show()
    
    def plot_phonon_map(self):
        plt = self.plt
        plt.figure(figsize=(20,15))
        para = np.array([])
        value_f_map = np.array([])

        for file_data in self.fileData_list:
            fre = file_data.frequency
            para = np.append(para, file_data.para)
            value_f_map = np.append(value_f_map, file_data.value_f)

        X,Y = np.meshgrid(fre,para)
        value_f_map = value_f_map.reshape(np.shape(X))

        plt.pcolor(X[para<100], Y[para<100], value_f_map[para<100], cmap="viridis")

        plt.xticks(fontsize=40)
        plt.yticks(fontsize=40)
        plt.xlabel('Frequency (THz)',fontsize=40)
        plt.ylabel(r'Fluence ($\mu$ J cm$^{-2}$)',fontsize=40)

        set_lw = 1
        ax=plt.gca()

        ax.spines['bottom'].set_linewidth(set_lw)
        ax.spines['left'].set_linewidth(set_lw)
        ax.spines['right'].set_linewidth(set_lw)
        ax.spines['top'].set_linewidth(set_lw)
        plt.colorbar()
        x = np.arange(0,5,0.01)
        y = np.ones(len(x))
        plt.xlim(1.2,4.6)
        plt.plot(x,23*y,'--',color=[1,1,0],linewidth = 5)
        plt.plot(x,55*y,'--',color=[1,1,0],linewidth = 5)
        plt.text(1.5,10,'1.3 THz',fontdict={'size':'30','color':[1,1,1],'fontweight':'bold',})
        plt.text(3.3,10,'3.1 THz',fontdict={'size':'30','color':[1,1,1],'fontweight':'bold',})
        plt.text(3.5,85,'4.1 THz',fontdict={'size':'30','color':[1,1,1],'fontweight':'bold',})
        plt.text(2,24,r'23 $\mu$J cm$^{-2}$',
        fontdict={'size':'30','color':[1,1,0],'fontweight':'bold',})
        plt.text(2,51,r'55 $\mu$J cm$^{-2}$',
        fontdict={'size':'30','color':[1,1,0],'fontweight':'bold',})

        plt.savefig('output/Fluence dependent fre domain waterfall.eps',bbox_inches = 'tight')
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
        
        if color_bar_style == "blue_red":
            num = self.num_files
            Color_R = np.linspace(230,77,num)/255
            Color_G = np.linspace(50,67,num)/255
            Color_B = np.linspace(18,152,num)/255
            color_list = []
            for i in range(self.num_files):
                color_list.append([Color_R[i], Color_G[i], Color_B[i]])
        return color_list

    