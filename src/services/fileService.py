import os
import sys
import re
sys.path.append('../')
# from systems.master import Master
from services.folderNameService import FolderNameService as DNS

class FileService():
    def rename_file(self, pathSource, pathDestination):
        try:
            os.rename(pathSource, pathDestination)
            return True
        except Exception as e:
            print(e)
            # responseResult = Responses.response('failed')
            # responseResult['message'] = e
            return False
    
    def rename_batch(self, directoryObject, pathMain):
        try:
            for row in directoryObject:
                folder = row.name
                # print(pathMain+'\\'+folder)
                readFile = os.scandir(pathMain+'\\'+folder)
                for row2 in readFile:
                    rowNumber = row2.name[-4:]                    
                    if rowNumber == '.mp3':                     
                    
                        textIndexLast = int(DNS.getIndex(folder, '_-_')) +1
                        textpharse1 = folder[:textIndexLast]
                        
                        textIndexLast = int(DNS.getIndex(folder, '_-_')) +1
                        textpharse1 = folder[:textIndexLast]
                        textIndexFirst = int(DNS.getIndex(textpharse1, '__')) + 3
                        textpharse2 = textpharse1[textIndexFirst:]
                        
                        fileName = row2.name
                        pathSource = pathMain+'\\'+folder+'\\'+fileName
                        pathDestination = pathMain+'\\'+folder+'\\'+textpharse2+'.mp3'
                        
                        # print('pathSource : '+pathSource )
                        # print('pathDestination : '+pathDestination )
                        self.rename_file(pathSource, pathDestination)
            return True
        except Exception as e:
            print(e)
            return False
