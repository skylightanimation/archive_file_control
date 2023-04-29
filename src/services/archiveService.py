import os
import subprocess
import sys
sys.path.append('../')
from systems.thirdparty import Thirdparty
from systems.security import Archive
from services.folderNameService import FolderNameService

class ArchiveService():
    		 
    def archive(self, pathResult, pathDirection):
        try:
            pathArchive = Thirdparty.archive
            # print(Archive._code)
            password = '-p' + str(Archive._code)
            # print(password)
            
            
            subprocess.run([pathArchive, 'a', pathResult, pathDirection, '-p'+str(Archive._code)])
            # 7z a secure.7z * -pSECRET
            return True
        except Exception as e:
            print(e)
            return False
    
    def doArchive(self, path, directoryObject):
        try:
            pathArchive = Thirdparty.archive
            # print(pathArchive)
            for entry in directoryObject : 
                if entry.is_dir() or entry.is_file(): 
                    directoryName = entry.name
                    # print(directoryName)
                    # print(path)
                    
                    textIndex = int(FolderNameService.getIndex(directoryName, "_-_"))
                    # print("INDEX : "+str(textIndex))
                    # print("INDEX : "+directoryName[textIndex])
                    
                    index  = textIndex+4
                    # print("INDEX : "+str(index))
                    # print("")
                    # print("Name : "+directoryName[index:])
                    
                    # print("")
                    
                    pathDirection = path+'\\'+directoryName
                    pathResult = path+'\\'+directoryName[index:]+'.7z'
                    # pathFileDesitination = path+'\\'+singleName+'.cbz'

                    # print(pathDirection)
                    # print(pathResult)
                    self.archive(pathResult, pathDirection)
                        # # print(pathFileDestination)
                    # subprocess.run([pathArchive, 'a', pathResult, pathDirection])
                        # os.rename(pathResult, pathFileDesitination)
                        
            return True
        except Exception as e:
            print(e)
            return False