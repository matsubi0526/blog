# -*- coding: utf-8 -*-
import numpy as np
import numpy.ma as ma
import matplotlib.pyplot as plt

def main():
    nx = 1201; ny = 1261
    f = open("LANDSEA.LFM_2K","rb")
    sldat = np.fromfile(f,">f",nx*ny).reshape((nx,ny),order="F")
    f.close
    
    msldat = ma.masked_values(sldat, -1)
    
    fig = plt.figure(figsize=(6,6))
    ax = fig.add_subplot(1,1,1)
    ax.contour(msldat.T,levels=[0.1],colors="black",linewidths=1)
    ax.invert_yaxis()
    ax.set_title("LANDSEA.LFM_2K")
    
    plt.savefig("lfm_sl.png")
    plt.close

if __name__ == "__main__":
    main()
