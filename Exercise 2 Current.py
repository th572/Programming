#!/usr/bin/env python
# coding: utf-8

# In[6]:


import glob
import re
from numpy import *
import matplotlib.pyplot as plt
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from mpl_toolkits.mplot3d import Axes3D

def extract():
    pattern_e = re.compile('SCF Done')
    pattern_tr = re.compile('Input=')
    folder_contents = []
    e_list = []
    t_list = []
    r_list = []

    for name in glob.glob('/Users/T/H2Soutfiles/*'): 
        folder_contents.append(name)

    for file in folder_contents:
        read_file = open(file, 'r+')

        for line in read_file:
            for match in re.finditer(pattern_e, line):
                e_list.append(float(line[22:36]))
            for match in re.finditer(pattern_tr, line):
                t_list.append(float(line[21:25]))
                r_list.append(float(line[12:16]))
    
    return (e_list, r_list, t_list)

def plot(data):            
    fig = plt.figure(figsize=(20,10))
    
    ax = fig.gca(projection='3d')
    x = data[1]
    y = data[2]
    z = data[0]
    
    ax.plot_trisurf(x, y, z, cmap='ocean', vmax=-398.0)

    '''customizing the z-axis'''
    ax.set_zlim(-398.7, -398.0)

    ax.set_title('The Potential Energy Surface for H2S')
    ax.set_xlabel('r / Angstroms')
    ax.set_ylabel('theta / degrees')
    ax.set_zlabel('Energy / Hartrees')

    plt.show()
    
def eqm_geometry(data):
    '''finding minimum energy'''

    min_index = data[0].index(min(data[0], key=float))
    min_e = data[0][min_index]
    min_r = data[1][min_index]
    min_t = data[2][min_index]

    print('The equilibrium geometry of H2S')
    print('E:', min_e)
    print('r:', min_r)
    print('theta:', min_t)
    
def vib_freq():
    '''calculating vibrational frequencies'''

    mu = 1.66*(10^-27)

    v1 = 1/(2*pi)*(k_r/(2*mu))^0.5
    v2 = 1/(2*pi)*(k_t/(min_r^2*0.5*mu))^0.5
    
def overall():
    file_data = extract()
    
    plot(file_data)
    
    eqm_geometry(file_data)
    
overall()


# In[10]:


import glob
import re
from numpy import *
import matplotlib.pyplot as plt
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from mpl_toolkits.mplot3d import Axes3D

def extract():
    pattern_e = re.compile('SCF Done')
    pattern_tr = re.compile('Input=')
    folder_contents = []
    e_list = []
    t_list = []
    r_list = []

    for name in glob.glob('/Users/T/H2Ofiles/*'): 
        folder_contents.append(name)

    for file in folder_contents:
        read_file = open(file, 'r+')

        for line in read_file:
            for match in re.finditer(pattern_e, line):
                e_list.append(float(line[22:36]))
            for match in re.finditer(pattern_tr, line):
                t_list.append(float(line[21:25]))
                r_list.append(float(line[12:16]))
    
    return (e_list, r_list, t_list)

def plot(data):
    fig = plt.figure(figsize=(20,10))
    
    ax = fig.gca(projection='3d')
    x = data[1]
    y = data[2]
    z = data[0]
    
    ax.plot_trisurf(x, y, z, cmap='ocean')

    '''customizing the z-axis'''
    #ax.set_zlim(-398.7, -398.0)

    ax.set_title('The Potential Energy Surface for H2O')
    ax.set_xlabel('r / Angstroms')
    ax.set_ylabel('theta / degrees')
    ax.set_zlabel('Energy / Hartrees')

    plt.show()
    
def eqm_geometry(data):
    '''finding minimum energy'''

    min_index = data[0].index(min(data[0], key=float))
    min_e = data[0][min_index]
    min_r = data[1][min_index]
    min_t = data[2][min_index]

    print('The equilibrium geometry of H2O')
    print('E:', min_e)
    print('r:', min_r)
    print('theta:', min_t)
    
def vib_freq():
    '''calculating vibrational frequencies'''

    mu = 1.66*(10^-27)

    v1 = 1/(2*pi)*(k_r/(2*mu))^0.5
    v2 = 1/(2*pi)*(k_t/(min_r^2*0.5*mu))^0.5
    
def overall():
    file_data = extract()
    
    plot(file_data)
    
    eqm_geometry(file_data)
    
overall()

