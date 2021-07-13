import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from sklearn.cluster import Birch, MiniBatchKMeans, AgglomerativeClustering, MeanShift
from sklearn import metrics

def upload():
    global filename
    filename = filedialog.askopenfilename(
            initialdir="/",title="Select A Text File",
            filetypes=(("Text files", "*.txt"),("all files", "*.*")))

def plot_data(data1, data2, ymax, ymin, ymax2, ymin2, xmax, xmin):
    figure = Figure(figsize=(11, 5), dpi=100)
    
    plot1 = figure.add_subplot(1, 2, 1)
    plot1.scatter(data1[:,1], data1[:,0], c=birch1, cmap='rainbow')
    plot1.set_xlim(xmin - 1000, xmax + 1000)
    plot1.set_ylim(ymin - 500, ymax + 500)
    plot1.set_title('Vp - Impedance')
    plot1.set_xlabel('Impedance')
    plot1.set_ylabel('Vp')
    
    plot2 = figure.add_subplot(1, 2, 2)
    plot2.scatter(data2[:,1], data2[:,0], c=birch2, cmap='rainbow')
    plot2.set_xlim(xmin - 1000, xmax + 1000)
    plot2.set_ylim(ymin2 - 0.15, ymax2 + 0.15)
    plot2.set_title('Rho - Impedance')
    plot2.set_xlabel('Impedance')
    plot2.set_ylabel('Rho')
    canvas = FigureCanvasTkAgg(figure, root)
    return canvas

def welcome_window():
    #labels and grid
    ttk.Button(root,text=
               "Please select a text file containing density and velocity",
               command=upload).grid(column=0, row=1, columnspan=3)
    ttk.Button(root, text="Next", command=display_data_window).grid(column=0,
              row=10, columnspan=3)
    return root

def display_data_window():
    global birch1, birch2, mbk1, mbk2, ac1, ac2, ms1, ms2
    for widget in root.winfo_children():
        widget.destroy()
    #Read data file and calculate impedance
    well_data = np.loadtxt(filename, comments="#", delimiter="\t",
                           unpack=False)
    IP = np.zeros_like(well_data[:,0])
    for num, (rho, vel) in enumerate(well_data):
        IP[num] = well_data[num,0] * well_data[num,1]
    #Set maximums and minimums for x and y label
    Vp_max = np.amax(well_data[:,1])
    Vp_min = np.amin(well_data[:,1])
    Rho_max = np.amax(well_data[:,0])
    Rho_min = np.amin(well_data[:,0])
    IP_max = int(np.amax(IP))
    IP_min = int(np.amin(IP))
    #Create Vp-IP and Rho-IP matrices for clustering and plotting
    VpIP = np.zeros_like(well_data)
    RhoIP = np.zeros_like(well_data)
    VpIP[:,0], VpIP[:,1] = well_data[:,1], IP
    RhoIP[:,0], RhoIP[:,1] = well_data[:,0], IP
    #Clustering
    #BIRCH
    cluster1 = Birch(branching_factor = 50, n_clusters = 2, threshold=1200)
    cluster1.fit(VpIP)
    birch1 = cluster1.predict(VpIP)
    cluster1.fit(RhoIP)
    birch2 = cluster1.predict(RhoIP)
    #Minibatch K-Means
    cluster2 = MiniBatchKMeans(n_clusters = 2, init='k-means++')
    cluster2.fit(VpIP)
    mbk1 = cluster2.predict(VpIP)
    cluster2.fit(RhoIP)
    mbk2 = cluster2.predict(RhoIP)
    #Agglomerative clustering
    cluster3 = AgglomerativeClustering(n_clusters=2, connectivity=None,
                                       linkage='ward')
    ac1 = cluster3.fit_predict(VpIP)
    ac2 = cluster3.fit_predict(RhoIP)
    #Mean Shift
    cluster4 = MeanShift()
    cluster4.fit(VpIP)
    ms1 = cluster4.predict(VpIP)
    cluster4.fit(RhoIP)
    ms2 = cluster4.predict(RhoIP)
    
    first_plot = plot_data(VpIP, RhoIP, Vp_max, Vp_min, Rho_max, Rho_min,
                           IP_max, IP_min)
    first_plot.get_tk_widget().pack()
    return root

#window widget asking the user for file/parameters
root = Tk()
root.title("Fluid/lithology discrimination Program")

welcome_frame = welcome_window()
root.mainloop()
