#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tues April 12 2022

@author: Ming Zhu




"""

from EnergyLibrary_UI import HandleData
from Data_processer import datapro
from tkinter import *
from tkinter import ttk

#starting the main software
root = Tk()
Record = HandleData(root)
root.mainloop()

