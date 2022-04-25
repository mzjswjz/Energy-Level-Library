#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tues April 12 2022

@author: Ming Zhu
"""

from tkinter import *
from tkinter import ttk
import Data_processer as DataPro
import tkinter.messagebox as tkmb


class HandleData:

    def __init__(self, master):

        master.title('Welcome to Energy Library!')
        master.geometry('')
        tabControl = ttk.Notebook(master)
        master.resizable(False, False)
        # master.configure(background = 'grey')


        # style background not working with 'Aqua' theme
        self.style = ttk.Style()
        self.style.configure('TFrame', font = ('Arial', 12))
        self.style.configure('TButton', font = ('Arial', 12))
        self.style.configure('TLabel', font = ('Arial', 12))
        self.style.configure('Header.TLabel', font = ('Arial', 18, 'bold'))

        tabRecord = ttk.Frame(tabControl)
        tabRead = ttk.Frame(tabControl)


        tabControl.add(tabRecord, text = 'Report Data to Library')
        tabControl.add(tabRead, text = 'Search Data in Library')
        tabControl.pack(expand = 1, fill = 'both')



        #UI design for data record tab
        self.tabRecord_header = ttk.Frame(tabRecord)
        self.tabRecord_header.pack()



        self.logo = PhotoImage(file = 'Cat.gif').subsample(12,12)
        ttk.Label(self.tabRecord_header, image = self.logo).grid(row = 0, column = 0, rowspan = 2)
        ttk.Label(self.tabRecord_header, text = 'Thanks for contributing!', style = 'Header.TLabel').grid(row = 0, column = 1)
        ttk.Label(self.tabRecord_header, wraplength = 300, text = ("This is a energy level library for organic semiconductor materials. "
                                                               "Please report energy levels of new molecules。")).grid(row = 1, column =1)


        self.tabRecord_content = ttk.Frame(tabRecord)
        self.tabRecord_content.pack()


        ttk.Label(self.tabRecord_content, text = 'Reference (DOI):', style = 'TLabel').grid(row = 0, column = 0, padx = 5, sticky = 'sw')
        ttk.Label(self.tabRecord_content, text = 'Molecule name (chemical name):', style = 'TLabel').grid(row = 0, column = 1, padx = 5,sticky = 'sw')
        ttk.Label(self.tabRecord_content, text = 'HOMO (eV):', style = 'TLabel').grid(row = 2, column = 0, padx = 5, sticky = 'sw')
        ttk.Label(self.tabRecord_content, text = 'LUMO (eV):', style = 'TLabel').grid(row = 2, column = 1, padx = 5, sticky = 'sw')
        ttk.Label(self.tabRecord_content, text = 'IE (eV):', style = 'TLabel').grid(row = 4, column = 0, padx = 5, sticky = 'sw')
        ttk.Label(self.tabRecord_content, text = 'EA (eV):', style = 'TLabel').grid(row = 4, column = 1, padx = 5, sticky = 'sw')
        ttk.Label(self.tabRecord_content, text = 'Technique used:', style = 'TLabel').grid(row = 6, column = 0, columnspan = 2, padx = 5, sticky = 'sw')
        ttk.Label(self.tabRecord_content, text = 'TXT file location (including .txt):', style = 'TLabel').grid(row = 8, column = 0, columnspan = 2, padx = 5, sticky = 'sw')

        self.entry_Reference = ttk.Entry(self.tabRecord_content, width = 30, font = ('Arial', 10))
        self.entry_Molecule_name = ttk.Entry(self.tabRecord_content, width = 30, font = ('Arial', 10))
        self.entry_HOMO = ttk.Entry(self.tabRecord_content, width = 30, font = ('Arial', 10))
        self.entry_LUMO = ttk.Entry(self.tabRecord_content, width = 30, font = ('Arial', 10))
        self.entry_IE = ttk.Entry(self.tabRecord_content, width = 30, font = ('Arial', 10))
        self.entry_EA = ttk.Entry(self.tabRecord_content, width = 30, font = ('Arial', 10))
        self.entry_Technique = ttk.Entry(self.tabRecord_content, width = 60, font = ('Arial', 10))
        self.entry_txtLocation = ttk.Entry(self.tabRecord_content, width = 60, font = ('Arial', 10))

        self.entry_Reference.grid(row = 1, column = 0, padx = 5)
        self.entry_Molecule_name.grid(row = 1, column = 1, padx = 5)
        self.entry_HOMO.grid(row = 3, column = 0, padx = 5)
        self.entry_LUMO.grid(row = 3, column = 1, padx = 5)
        self.entry_IE.grid(row = 5, column = 0, padx = 5)
        self.entry_EA.grid(row = 5, column = 1, padx = 5)
        self.entry_Technique.grid(row = 7, column = 0, columnspan = 2, padx = 5,sticky = 'sw')
        self.entry_txtLocation.grid(row = 9, column = 0, columnspan = 2, padx = 5,sticky = 'sw')



        ttk.Button(self.tabRecord_content, text = 'Submit', command = self.submit, style = 'TButton').grid(row = 10, column = 0, padx = 5, pady = 5, sticky = 'e')
        ttk.Button(self.tabRecord_content, text = 'Clear', command = self.clear, style = 'TButton').grid(row = 10, column = 1, padx = 5, pady = 5, sticky = 'w')


        # UI design for search data tab
        self.tabRead_header = ttk.Frame(tabRead)
        self.tabRead_header.pack()

        ttk.Label(self.tabRead_header,
                  wraplength = 400,
                  text = 'You can search for energy levels and related information of molecules stored in this library!',
                  style = 'Header.TLabel').grid(row = 0, column = 1)

        self.tabRead_content = ttk.Frame(tabRead)
        self.tabRead_content.pack()

        ttk.Label(self.tabRead_content, text = 'Step1: Enter the location of TXT file (including .txt)', style = 'TLabel').grid(row = 0, column = 0, padx = 10, sticky = 'sw')
        ttk.Label(self.tabRead_content, text = 'Step2: Enter the name of the molecule', style = 'TLabel').grid(row = 3, column = 0, padx = 10, sticky = 'sw')

        self.search_txtLocation = ttk.Entry(self.tabRead_content, width = 60, font = ('Arial', 12))
        self.search_txtLocation.grid(row = 1, column = 0, columnspan = 2, padx = 5, pady = 5)

        ttk.Button(self.tabRead_content,
                   text = 'Submit',
                   command = self.submitSearch,
                   style = 'TButton').grid(row = 2, column = 0, padx = 5, pady = 5, sticky = 's')
        ttk.Button(self.tabRead_content,
                   text = 'Clear',
                   command = self.clearSearch,
                   style = 'TButton').grid(row = 2, column = 1, padx = 5, pady = 5, sticky = 'w')



        self.search_molecule = StringVar()
        self.combobox = ttk.Combobox(self.tabRead_content, textvariable = self.search_molecule)
        self.combobox.grid(row = 3, column = 1, padx = 10)
        ttk.Button(self.tabRead_content,
                   text = 'Get Information of This Molecule',
                   command = self.GetInfo, style = 'TButton').grid(row = 4, column = 0, padx = 5, pady = 5, sticky = 's')
        ttk.Button(self.tabRead_content,
                   text = 'Clear',
                   command = self.ClearInfo, style = 'TButton').grid(row = 4, column = 1, padx = 5, pady = 5, sticky = 'w')
        self.InfoText = Text(self.tabRead_content, height = 10, width = 60)
        self.InfoText.grid(row = 5, column = 0, columnspan = 2, padx = 5, pady = 5)
        # self.InfoText.insert('1.0', 'Line1\n')
        # self.InfoText.insert('2.0', 'Line2\n')







        #MoleculeNumber = DataPro
        self.combobox.config(values = ())
        self.search_molecule.set('Please select a molecule!')









    def submit(self):
        permission = False
        Entry = [self.entry_Reference.get(), self.entry_Molecule_name.get(), self.entry_HOMO.get(), self.entry_LUMO.get(), self.entry_IE.get(), self.entry_EA.get(), self.entry_Technique.get(), self.entry_txtLocation.get()]
        TxtLoc = Entry[-1] # get location of txt file

        for u in Entry[2:5]:
            if u == '':
                pass
            else:
                try:
                    float(u)
                except ValueError:
                    tkmb.showerror(title = 'Wrong data type entered', message= 'Please check if you enter numerial values for energy levels!')



        # check if we have a txt file location
        if self.entry_txtLocation.get() == '':
            tkmb.showerror(title = 'No target txt file is assigned', message= 'Please enter a location for the txt file!')
        else:
            try:
                txttest = open(TxtLoc, 'r')
                txttest.close()
                permission = True
            except FileNotFoundError:
                tkmb.showerror(title = 'Wrong txt file location', message= 'Please check if you entered a correct location for the txt file')

        # record input values and write into txt file
        if permission == True:
            Record = DataPro.datapro()

            ValueTaken = dict({})
            num = 0

            for u in Record.get_name_list():
                ValueTaken[u] = Entry[num]
                num += 1

            Record.write_file(TxtLoc,ValueTaken)
            self.clear()
            tkmb.showinfo(title = 'Data Recorded!', message = 'Thank you for contributing!')


    def clear(self):
        self.entry_Reference.delete(0, 'end')
        self.entry_Molecule_name.delete(0, 'end')
        self.entry_HOMO.delete(0, 'end')
        self.entry_LUMO.delete(0, 'end')
        self.entry_IE.delete(0, 'end')
        self.entry_EA.delete(0, 'end')
        self.entry_Technique.delete(0, 'end')
        self.entry_txtLocation.delete(0, 'end')

    def submitSearch(self):
        flag = False
        SearchLoc = self.search_txtLocation.get()
        self.SearchData = DataPro.datapro()

        if SearchLoc == '':
            tkmb.showerror(title = 'No target txt file is assigned', message= 'Please enter a location for the txt file!')
        else:
            try:
                Stxttest = open(SearchLoc, 'r')
                Stxttest.close()
                flag = True
            except FileNotFoundError:
                tkmb.showerror(title = 'Wrong txt file location', message= 'Please check if you entered a correct location for the txt file')


        if flag is True:

            self.ImportedData = self.SearchData.read_file(file = SearchLoc)
            StoredMolecule = []
            for item in self.ImportedData:
                StoredMolecule.append(item.get('Molecule_name'))
            self.combobox.config(values = (StoredMolecule))
            tkmb.showinfo(title = 'Location received', message = 'You can now go to Step 2')



    def clearSearch(self):
        self.search_txtLocation.delete(0,'end')

    def GetInfo(self):

        self.InfoText.delete(1.0, END)
        SelectMolecule = self.combobox.get()
        for item in self.ImportedData:
            if item.get('Molecule_name') == SelectMolecule:
                lineNum = 1.0
                for key in item:
                    self.InfoText.insert(lineNum, f'{key}: {item[key]}\n')
                    lineNum += 1.0
    def ClearInfo(self):
        self.InfoText.delete(1.0, 'end')







def main():
     root = Tk()
     DataRecorded = HandleData(root)
     root.mainloop()

if __name__ == "__main__": main()