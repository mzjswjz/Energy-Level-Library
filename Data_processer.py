#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tues April 12 2022

@author: Ming Zhu
"""
import re #better

class datapro:
    __name_list = {'Molecule_name_abbr': str,
                   'Molecule_name_complete': str,
                   'Empirical_formula': str,
                   'CAS': str,
                   'CIF': str,
                   'Molecular_weight': float,
                   'Density': float,
                   'Provisional_evaporation_T': str,
                   'HOMO': float,
                   'LUMO': float,
                   'IE': float,
                   'EA': float,
                   'Technique_HOMO': str,
                   'Technique_LUMO': str,
                   'Technique_IE': str,
                   'Technique_EA': str,
                   'Reference_HOMO': str,
                   'Reference_LUMO': str,
                   'Reference_IE': str,
                   'Reference_EA': str,
                   'Reference_density': str,
                    }

    def __init__(self):
        pass

    def read_file(self, file):
        EnergyData = []
        with open(file, 'r') as f:
            flag = False
            for line in f:
                if line.strip() == '#START#':
                    CurrentData = dict({})
                    for u in self.__name_list.keys():
                        CurrentData[u] = None
                    flag = True
                elif line.strip() == '#END#':
                    EnergyData.append(CurrentData)
                    del CurrentData
                    flag = False
                elif flag:
                    SplitedLine = line.split('=')
                    DataKey = SplitedLine[0].strip()
                    DataValue = SplitedLine[1].strip()[1:-1]
                    if DataKey in self.__name_list.keys():
                        if DataValue == '':
                            pass
                        else:
                            try:
                                CurrentData[DataKey] = self.__name_list[DataKey](DataValue)
                            except ValueError:
                                raise ValueError(f'Cannot convert {DataValue} to required data type!')

        return EnergyData


    def write_file(self,file,DataDict:dict):
        with open(file, 'a') as f:
            f.write('\n')
            f.write('#START#\n')
            for name in self.__name_list.keys():
                if not (name in DataDict.keys()):
                    continue
                f.write(f'{name}={{{DataDict[name]}}}\n')
            f.write('#END#\n')

    def get_name_list(self):
        name_list = dict({})
        for u in self.__name_list.keys():
            name_list[u] = self.__name_list[u]
        return name_list





# if __name__ == '__main__':
#
#     DP = datapro()
#     print(DP.get_name_list())
    # # print(Data_result)
    # print(Data_result[0]['LUMO']
    # Trydict= {'Reference': 'doi1', 'Molecule_name': 'DCV5T', 'HOMO': -3.0,'LUMO': -5.0,'IE': None,'EA': None, 'Technique': 'CV'  }
    # Try = datapro()
    # Try.write_file('data.hld.txt',Trydict)