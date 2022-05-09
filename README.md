# Energy-Level-Library
Here I'm developing a library of HOMO and LUMO levels of organic semiconductor materials with UI. 
Version 1.0.0 Introduction:
This version allows users to record information of new organic semiconductors and search information of molecules stored in txt file 'energy_data.txt'.
There are in total 21 inputs but you don't have to fill them all to report a new molecule to the library. You should be able to add or correct information to existing data in further versions. Unfortunately, the current library can only be used locally, which means you cannot access the data that others put in. You will have your own material library for now. This problem should be solved in further versions. Currently, you cannot delete data through the software. You can edit the txt file directly but IT IS NOT RECOMMENDED! It may cause problems for the software to run properly! If you have to change it, please FOLLOW THE FORMAT of the txt file! 

To use the software:
1. Please download or clone the whole file 'Energy-Level-Library-master' to your laptop. 
2. DO NOT move any of the files in the original folders.
3. Open 'Start_Building_Library_main.py' with python 3.9.10 with package 'tkinter' installed.
4. You should be able to see a window pop up, otherwise check the terminal to see if you installed all the packages needed. 


When you want to report a new molecule:
1. First, use search function on tab 'Search data in Library' to see if this molecule has been recorded and whether the information you want to record already exists. 
2. Second, enter the information of molecule on tab 'Report data to Library'. Please make sure you enter numeric values in 'Molecular weight', 'Density', 'HOMO', 'LUMO', 'IE', 'EA'. Please be aware that 'HOMO', 'LUMO', 'IE', 'EA' used here are NEGATIVE values. 
3. MAKE SURE YOU DON'T INCLUDE ADDITIONAL 'RETURN' WHEN YOU ENTER VALUES! This can cause serious problems to the data library in current version.
4. Check the information you entered is correct and then hit 'Submit' button. 

When you want to search the information of existing molecules in the library:
1. Use tab 'Search data in Library'.
2. Enter the location of the txt file 'energy_data.txt'. (including the file name.txt)
3. Follow the instruction in the software. 
