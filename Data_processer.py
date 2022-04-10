import re #better

class datapro:
    __name_list = {'Reference': str,
                   'Molecule_name': str,
                   'HOMO': float,
                   'LUMO': float,
                   'IE': float,
                   'EA': float,
                   'Technique': str,
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




if __name__ == '__main__':
    pass
    # DP = datapro()
    # Data_result= DP.read_file('data.hld.txt')
    # print(Data_result)
    # print(Data_result[0]['LUMO']
    # Trydict= {'Reference': 'doi1', 'Molecule_name': 'DCV5T', 'HOMO': -3.0,'LUMO': -5.0,'IE': None,'EA': None, 'Technique': 'CV'  }
    # Try = datapro()
    # Try.write_file('data.hld.txt',Trydict)

