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


        #Style setting, note style background does not work with macOS 'Aqua' theme
        self.style = ttk.Style()
        self.style.configure('TFrame', font=('Arial', 14))
        self.style.configure('TButton', font=('Arial', 14, 'bold'))
        self.style.configure('TLabel', font=('Arial', 14, 'bold'))
        self.style.configure('Body.TLabel', font=('Arial', 16))
        self.style.configure('Header.TLabel', font=('Arial', 20, 'bold'))


        #set tabs
        tabRecord = ttk.Frame(tabControl)
        tabRead = ttk.Frame(tabControl)

        #configure tabs
        tabControl.add(tabRecord, text='Report Data to Library')
        tabControl.add(tabRead, text='Search Data in Library')
        tabControl.pack(expand=1, fill='both')



        #UI design for tab to record data
        #Header setting
        self.tabRecord_header = ttk.Frame(tabRecord)
        self.tabRecord_header.pack()



        self.logo = PhotoImage(file='Cat.gif').subsample(6,6)
        ttk.Label(self.tabRecord_header, image=self.logo).grid(row=0, column=0, rowspan = 2)
        ttk.Label(self.tabRecord_header, text='Thanks for contributing!', style='Header.TLabel').grid(row=0, column=2)
        ttk.Label(self.tabRecord_header, wraplength=400, text = ("This is an energy level library for organic semiconductor materials. "
                                                               "Please report information of new molecules。"), style='Body.TLabel').grid(row=1, column=2)
        ttk.Label(self.tabRecord_header, style='Body.TLabel').grid(row=2, column=0, columnspan=4)

        #content settings
        self.tabRecord_content = ttk.Frame(tabRecord)
        self.tabRecord_content.pack()

        ttk.Label(self.tabRecord_content, text='Molecule name (abbreviation):', style='TLabel').grid(row=0, column=0, padx=5, sticky='sw')
        ttk.Label(self.tabRecord_content, text='Molecule name (complete):', style='TLabel').grid(row=0, column=1, columnspan=2, padx=5, sticky='sw')
        ttk.Label(self.tabRecord_content, text='Empirical formula:', style='TLabel').grid(row=0, column=3, padx=5, sticky='sw')
        ttk.Label(self.tabRecord_content, text='CAS:', style='TLabel').grid(row=2, column=0, columnspan=2, padx=5, sticky='sw')
        ttk.Label(self.tabRecord_content, text='CIF:', style='TLabel').grid(row=2, column=2, columnspan=2, padx=5, sticky='sw')
        ttk.Label(self.tabRecord_content, text='Molecular weight (g/mol):', style = 'TLabel').grid(row=4, column=0, padx=5, sticky='sw')
        ttk.Label(self.tabRecord_content, text='Density (g/cm\u00B3):', style='TLabel').grid(row=4, column=2, padx=5, sticky = 'sw')
        ttk.Label(self.tabRecord_content, text='Provisional evaporation Temperature (\u00B0C):', style='TLabel').grid(row=4, column=1, padx=5, sticky='sw')
        ttk.Label(self.tabRecord_content, text='HOMO (eV):', style='TLabel').grid(row=6, column=0, padx=5,
                                                                                        sticky='sw')
        ttk.Label(self.tabRecord_content, text='LUMO (eV):', style='TLabel').grid(row=8, column=0, padx=5,
                                                                                        sticky='sw')
        ttk.Label(self.tabRecord_content, text='IE (eV):', style='TLabel').grid(row=10, column=0, padx=5,
                                                                                        sticky='sw')
        ttk.Label(self.tabRecord_content, text='EA (eV):', style='TLabel').grid(row=12, column=0, padx=5,
                                                                                        sticky='sw')
        ttk.Label(self.tabRecord_content, text='Technique to measure HOMO:', style='TLabel').grid(row=6, column=1, padx=5,
                                                                                        sticky='sw')
        ttk.Label(self.tabRecord_content, text='Technique to measure LUMO:', style='TLabel').grid(row=8, column=1, padx=5,
                                                                                        sticky='sw')
        ttk.Label(self.tabRecord_content, text='Technique to measure IE:', style='TLabel').grid(row=10, column=1, padx=5,
                                                                                        sticky='sw')
        ttk.Label(self.tabRecord_content, text='Technique to measure EA:', style='TLabel').grid(row=12, column=1, padx=5,
                                                                                        sticky='sw')
        ttk.Label(self.tabRecord_content, text='Reference for HOMO (DOI):', style='TLabel').grid(row=6, column=2, columnspan=2, padx=5,
                                                                                        sticky='sw')
        ttk.Label(self.tabRecord_content, text='Reference for LUMO (DOI):', style='TLabel').grid(row=8, column=2, columnspan=2, padx=5,
                                                                                        sticky='sw')
        ttk.Label(self.tabRecord_content, text='Reference for IE (DOI):', style='TLabel').grid(row=10, column=2, columnspan=2, padx=5,
                                                                                        sticky='sw')
        ttk.Label(self.tabRecord_content, text='Reference for EA (DOI):', style='TLabel').grid(row=12, column=2, columnspan=2, padx=5,
                                                                                        sticky='sw')
        ttk.Label(self.tabRecord_content, text='Reference for density (DOI/URL):', style='TLabel').grid(row=4, column=3, padx=5,
                                                                                           sticky='sw')
        ttk.Label(self.tabRecord_content, text = 'TXT file location (including .txt):', style = 'TLabel').grid(row=14, column=0, columnspan=2,
                                                                                                               padx=5, sticky='sw')

        self.entry_Molecule_name_abbr = ttk.Entry(self.tabRecord_content, width=30, font=('Arial', 14))
        self.entry_Molecule_name_complete = ttk.Entry(self.tabRecord_content, width=60, font=('Arial', 14))
        self.entry_Empirical_formula = ttk.Entry(self.tabRecord_content, width=30, font=('Arial', 14))
        self.entry_CAS = ttk.Entry(self.tabRecord_content, width=30, font=('Arial', 14))
        self.entry_CIF = ttk.Entry(self.tabRecord_content, width=30, font=('Arial', 14))
        self.entry_Molecular_weight = ttk.Entry(self.tabRecord_content, width=30, font=('Arial', 14))
        self.entry_Density = ttk.Entry(self.tabRecord_content, width=30, font=('Arial', 14))
        self.entry_Provisional_evaporation_T = ttk.Entry(self.tabRecord_content, width=30, font=('Arial', 14))
        self.entry_HOMO = ttk.Entry(self.tabRecord_content, width=30, font=('Arial', 14))
        self.entry_LUMO = ttk.Entry(self.tabRecord_content, width=30, font=('Arial', 14))
        self.entry_IE = ttk.Entry(self.tabRecord_content, width=30, font=('Arial', 14))
        self.entry_EA = ttk.Entry(self.tabRecord_content, width=30, font=('Arial', 14))
        self.entry_Technique_HOMO = ttk.Entry(self.tabRecord_content, width=30, font=('Arial', 14))
        self.entry_Technique_LUMO = ttk.Entry(self.tabRecord_content, width=30, font=('Arial', 14))
        self.entry_Technique_IE = ttk.Entry(self.tabRecord_content, width=30, font=('Arial', 14))
        self.entry_Technique_EA = ttk.Entry(self.tabRecord_content, width=30, font=('Arial', 14))
        self.entry_Reference_HOMO = ttk.Entry(self.tabRecord_content, width=60, font=('Arial', 14))
        self.entry_Reference_LUMO = ttk.Entry(self.tabRecord_content, width=60, font=('Arial', 14))
        self.entry_Reference_IE = ttk.Entry(self.tabRecord_content, width=60, font=('Arial', 14))
        self.entry_Reference_EA = ttk.Entry(self.tabRecord_content, width=60, font=('Arial', 14))
        self.entry_Reference_Density = ttk.Entry(self.tabRecord_content, width=30, font=('Arial', 14))
        self.entry_record_txtLocation = ttk.Entry(self.tabRecord_content, width=120, font=('Arial', 14))







        self.entry_Molecule_name_abbr.grid(row=1, column=0, padx=5, sticky='sw')
        self.entry_Molecule_name_complete.grid(row=1, column=1, columnspan=2, padx=5, sticky='sw')
        self.entry_Empirical_formula.grid(row=1, column=3, padx=5, sticky='sw')
        self.entry_CAS.grid(row=3, column=0, columnspan=2, padx=5, sticky='sw')
        self.entry_CIF.grid(row=3, column=2, columnspan=2, padx=5, sticky='sw')
        self.entry_Molecular_weight.grid(row=5, column=0, padx=5, sticky='sw')
        self.entry_Provisional_evaporation_T.grid(row=5, column=1, padx=5, sticky='sw')
        self.entry_Density.grid(row=5, column=2, padx=5, sticky='sw')
        self.entry_Reference_Density.grid(row=5, column=3, padx=5, sticky='sw')
        self.entry_HOMO.grid(row=7, column=0, padx=5, sticky='sw')
        self.entry_LUMO.grid(row=9, column=0, padx=5, sticky='sw')
        self.entry_IE.grid(row=11, column=0, padx=5, sticky='sw')
        self.entry_EA.grid(row=13, column=0, padx=5, sticky='sw')
        self.entry_Technique_HOMO.grid(row=7, column=1, padx=5, sticky='sw')
        self.entry_Technique_LUMO.grid(row=9, column=1, padx=5, sticky='sw')
        self.entry_Technique_IE.grid(row=11, column=1, padx=5, sticky='sw')
        self.entry_Technique_EA.grid(row=13, column=1, padx=5, sticky='sw')
        self.entry_Reference_HOMO.grid(row=7, column=2, columnspan=2, padx=5, sticky='sw')
        self.entry_Reference_LUMO.grid(row=9, column=2, columnspan=2, padx=5, sticky='sw')
        self.entry_Reference_IE.grid(row=11, column=2, columnspan=2, padx=5, sticky='sw')
        self.entry_Reference_EA.grid(row=13, column=2, columnspan=2, padx=5, sticky='sw')
        self.entry_record_txtLocation.grid(row=15, column=0, columnspan=4, padx=5, sticky='sw')





        ttk.Button(self.tabRecord_content, text = 'Submit', command = self.submitRecord, style = 'TButton').grid(row = 16, column = 1, padx = 5, pady = 5, sticky = 'w')
        ttk.Button(self.tabRecord_content, text = 'Clear', command = self.clearRecord, style = 'TButton').grid(row = 16, column = 2, padx = 5, pady = 5, sticky = 'e')


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

        self.search_txtLocation = ttk.Entry(self.tabRead_content, width = 50, font = ('Arial', 14))
        self.search_txtLocation.grid(row = 1, column = 0, columnspan = 2, padx = 5, pady = 5, sticky = 'sw')

        ttk.Button(self.tabRead_content,
                   text = 'Submit',
                   command = self.submitSearch,
                   style = 'TButton').grid(row = 2, column = 0, padx = 5, pady = 5, sticky = 'w')
        ttk.Button(self.tabRead_content,
                   text = 'Clear',
                   command = self.clearSearch,
                   style = 'TButton').grid(row = 2, column = 1, padx = 5, pady = 5, sticky = 'w')

        #frame for diaplaying information

        self.search_molecule = StringVar()
        self.combobox = ttk.Combobox(self.tabRead_content, width=30, height=5, textvariable = self.search_molecule)
        self.combobox.grid(row = 3, column = 1, padx = 5)
        ttk.Button(self.tabRead_content,
                   text = 'Get Information of This Molecule',
                   command = self.GetInfo, style = 'TButton').grid(row = 4, column = 0, padx = 5, pady = 5, sticky = 'w')
        ttk.Button(self.tabRead_content,
                   text='Clear',
                   command=self.ClearInfo, style='TButton').grid(row=4, column=1, padx=5, pady=5, sticky='w')

        v = Scrollbar(self.tabRead_content, orient='vertical')
        v.grid(row=5, column=1, sticky= 'w')
        self.InfoText = Text(self.tabRead_content, height = 10, width = 80, yscrollcommand=v.set)
        v.config(command=self.InfoText.yview)
        self.InfoText.grid(row = 5, column = 0, padx = 5, pady = 5)
        # self.InfoText.insert('1.0', 'Line1\n')
        # self.InfoText.insert('2.0', 'Line2\n')


        #MoleculeNumber = DataPro
        self.combobox.config(values = ())
        self.search_molecule.set('Please select a molecule!')









    def submitRecord(self):
        passOne = False
        passTwo = False

        Entry = [self.entry_Molecule_name_abbr.get(), self.entry_Molecule_name_complete.get(), self.entry_Empirical_formula.get(),
                 self.entry_CAS.get(), self.entry_CIF.get(),
                 self.entry_Molecular_weight.get(), self.entry_Density.get(), self.entry_Provisional_evaporation_T.get(),
                 self.entry_HOMO.get(), self.entry_LUMO.get(), self.entry_IE.get(), self.entry_EA.get(),
                 self.entry_Technique_HOMO.get(), self.entry_Technique_LUMO.get(), self.entry_Technique_IE.get(), self.entry_Technique_EA.get(),
                 self.entry_Reference_HOMO.get(), self.entry_Reference_LUMO.get(), self.entry_Reference_IE.get(), self.entry_Reference_EA.get(),
                 self.entry_Reference_Density.get(),
                 self.entry_record_txtLocation.get()]
        TxtLocRecord = Entry[-1] # get location of txt file

        NumEntry = [Entry[5], Entry[6], Entry[8], Entry[9], Entry[10], Entry[11]]
        NameEntry = [Entry[0], Entry[1], Entry[2]]

        #check if some entry is numeric value or not
        for u in NumEntry:
            if u == '':
                pass
                passOne = True
            else:
                try:
                    passOne = False
                    float(u)
                    passOne = True
                except ValueError:
                    tkmb.showerror(title = 'Wrong data type entered', message= 'Please check if you enter numerial values for Molecular weight, density or energy levels!')
                    break

        #check if the user at least enter one name
        numEmptyName = 0
        for n in NameEntry:
            if n == '':
                numEmptyName += 1
        if numEmptyName == len(NameEntry):
            passOne = False



        #check if all the entrys are empty
        numEmptyEntry = 0
        for e in Entry[0:-1]:
            if e == '':
                numEmptyEntry += 1
        if numEmptyEntry == len(Entry[0:-1]):
            passOne = False



        # check if we have a txt file location
        if TxtLocRecord == '':
            tkmb.showerror(title = 'No target txt file is assigned', message= 'Please enter a location for the txt file!')
        else:
            try:
                txttest = open(TxtLocRecord, 'r')
                txttest.close()
                passTwo = True
            except FileNotFoundError:
                tkmb.showerror(title = 'Wrong txt file location', message= 'Please check if you entered a correct location for the txt file')

        # record input values and write into txt file
        if passOne == True and passTwo == True:
            Record = DataPro.datapro()

            ValueTaken = dict({})
            num = 0

            for u in Record.get_name_list():
                ValueTaken[u] = Entry[num]
                num += 1

            Record.write_file(TxtLocRecord,ValueTaken)
            self.clearRecord()
            tkmb.showinfo(title = 'Data Recorded!', message = 'Thank you for contributing!')
        else:
            tkmb.showerror(title='Not enough inputs!', message='Please check if you entered enough inputs!')



    def clearRecord(self):
        self.entry_Molecule_name_abbr.delete(0, 'end')
        self.entry_Molecule_name_complete.delete(0, 'end')
        self.entry_Empirical_formula.delete(0, 'end')
        self.entry_CAS.delete(0, 'end')
        self.entry_CIF.delete(0, 'end')
        self.entry_Molecular_weight.delete(0, 'end')
        self.entry_Density.delete(0, 'end')
        self.entry_Provisional_evaporation_T.delete(0, 'end')
        self.entry_HOMO.delete(0, 'end')
        self.entry_LUMO.delete(0, 'end')
        self.entry_IE.delete(0, 'end')
        self.entry_EA.delete(0, 'end')
        self.entry_Technique_HOMO.delete(0, 'end')
        self.entry_Technique_LUMO.delete(0, 'end')
        self.entry_Technique_IE.delete(0, 'end')
        self.entry_Technique_EA.delete(0, 'end')
        self.entry_Reference_HOMO.delete(0, 'end')
        self.entry_Reference_LUMO.delete(0, 'end')
        self.entry_Reference_IE.delete(0, 'end')
        self.entry_Reference_EA.delete(0, 'end')
        self.entry_Reference_Density.delete(0, 'end')


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
                StoredMolecule.append(item.get('Molecule_name_abbr'))
            self.combobox.config(values = (StoredMolecule))
            tkmb.showinfo(title = 'Location received', message = 'You can now go to Step 2')



    def clearSearch(self):
        self.search_txtLocation.delete(0,'end')

    def GetInfo(self):

        self.InfoText.delete(1.0, END)
        SelectMolecule = self.combobox.get()
        for item in self.ImportedData:
            if item.get('Molecule_name_abbr') == SelectMolecule:
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