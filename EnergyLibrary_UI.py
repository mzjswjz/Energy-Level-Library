from tkinter import *
from tkinter import ttk
import Data_processer as DataPro
import tkinter.messagebox as tkmb


class RecordData:

    def __init__(self, master):
        self.frame_header = ttk.Frame(master)
        self.frame_header.pack()


        self.logo = PhotoImage(file = 'Cat.gif').subsample(11,11)
        ttk.Label(self.frame_header, image = self.logo).grid(row = 0, column = 0, rowspan = 2)
        ttk.Label(self.frame_header, text = 'Thanks for contributing!').grid(row = 0, column = 1)
        ttk.Label(self.frame_header, wraplength = 300, text = ("This is a energy level library for organic semiconductor materials. "
                                                               "Please report energy levels of new molecules")).grid(row = 1, column =1)


        self.frame_content = ttk.Frame(master)
        self.frame_content.pack()


        ttk.Label(self.frame_content, text = 'Reference (DOI):').grid(row = 0, column = 0, padx = 5, sticky = 'sw')
        ttk.Label(self.frame_content, text = 'Molecule name (chemical name):').grid(row = 0, column = 1, padx = 5,sticky = 'sw')
        ttk.Label(self.frame_content, text = 'HOMO (eV):').grid(row = 2, column = 0, padx = 5, sticky = 'sw')
        ttk.Label(self.frame_content, text = 'LUMO (eV):').grid(row = 2, column = 1, padx = 5, sticky = 'sw')
        ttk.Label(self.frame_content, text = 'IE (eV):').grid(row = 4, column = 0, padx = 5, sticky = 'sw')
        ttk.Label(self.frame_content, text = 'EA (eV):').grid(row = 4, column = 1, padx = 5, sticky = 'sw')
        ttk.Label(self.frame_content, text = 'Technique used:').grid(row = 6, column = 0, columnspan = 2, padx = 5, sticky = 'sw')
        ttk.Label(self.frame_content, text = 'TXT file location (including .txt):').grid(row = 8, column = 0, columnspan = 2, padx = 5, sticky = 'sw')

        self.entry_Reference = ttk.Entry(self.frame_content, width = 20)
        self.entry_Molecule_name = ttk.Entry(self.frame_content, width = 20)
        self.entry_HOMO = ttk.Entry(self.frame_content, width = 20)
        self.entry_LUMO = ttk.Entry(self.frame_content, width = 20)
        self.entry_IE = ttk.Entry(self.frame_content, width = 20)
        self.entry_EA = ttk.Entry(self.frame_content, width = 20)
        self.entry_Technique = ttk.Entry(self.frame_content, width = 40)
        self.entry_txtLocation = ttk.Entry(self.frame_content, width = 40)

        self.entry_Reference.grid(row = 1, column = 0, padx = 5)
        self.entry_Molecule_name.grid(row = 1, column = 1, padx = 5)
        self.entry_HOMO.grid(row = 3, column = 0, padx = 5)
        self.entry_LUMO.grid(row = 3, column = 1, padx = 5)
        self.entry_IE.grid(row = 5, column = 0, padx = 5)
        self.entry_EA.grid(row = 5, column = 1, padx = 5)
        self.entry_Technique.grid(row = 7, column = 0, columnspan = 2, padx = 5,sticky = 'sw')
        self.entry_txtLocation.grid(row = 9, column = 0, columnspan = 2, padx = 5,sticky = 'sw')



        ttk.Button(self.frame_content, text = 'Submit', command = self.submit).grid(row = 10, column = 0, padx = 5, pady = 5, sticky = 'e')
        ttk.Button(self.frame_content, text = 'Clear', command = self.clear).grid(row = 10, column = 1, padx = 5, pady = 5, sticky = 'w')

    def submit(self):
        ValueTaken = {'Reference': self.entry_Reference.get(),
                      'Molecule_name': self.entry_Molecule_name.get(),
                      'HOMO': self.entry_HOMO.get(),
                      'LUMO': self.entry_LUMO.get(),
                      'IE': self.entry_IE.get(),
                      'EA': self.entry_EA.get(),
                      'Technique': self.entry_Technique.get()}

        Record = DataPro.datapro()
        Record.write_file(self.entry_txtLocation.get(),ValueTaken)
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


def main():
    root = Tk()
    DataRecorded = RecordData(root)
    root.mainloop()

if __name__ == "__main__": main()