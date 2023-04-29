import os
import sys
sys.path.append('../')
from systems.directory import Path

class FolderService():
    
    def isExist(self, path):
        try:
            # path = Path.process
            # pathNew = path+'\\'+name
            if os.path.exists(path):
                # os.makedirs(pathNew)
                return True
            else:
                return False
        except Exception as e:
            print(e)
            return False    
    
    
    def isNotOnArchive(self, name):
        try:
            path = Path.process
            pathNew = path+'\\'+name[0]+'\\'+name
            if not os.path.exists(pathNew):
                # os.makedirs(pathNew)
                return True
            else:
                return False
        except Exception as e:
            print(e)
            return False
            
    def isNotOnProcess(self, path):
        try:
            if not os.path.exists(path):
                # os.makedirs(pathNew)
                return True
            else:
                return False
        except Exception as e:
            print(e)
            return False
    
    def createDirectoryByName(self, name):
        try:
            path = Path.process#+'\\'+name
            pathNew = path+'\\'+name
            checkArchive = self.isNotOnArchive(name)
            checkProcess = self.isNotOnProcess(pathNew)
            
            if checkArchive == True and checkProcess == True:
                os.makedirs(pathNew)
                return True
            else:
                return False
        except Exception as e:
            print(e)
            return False
        
    def createDirectoryByPath(self, path, name):
        try:
            # path = Path.process#+'\\'+name
            pathNew = path+'\\'+name
            checkProcess = self.isNotOnProcess(pathNew)
            
            if checkProcess == True:
                os.makedirs(pathNew)
                return True
            else:
                return False
        except Exception as e:
            print(e)
            return False       

    def removeDirecotry(self, path):
        try:
            
            checkProcess = self.isExist(path)
            
            if checkProcess == True:
                command = 'rmdir /s /q "'+path+'"'
                os.system(command)
                return True
            else:
                return False
        except Exception as e:
            print(e)
            return False

    def readDirectory(self, path):
        try:
            checkProcess = self.isExist(path)            
            
            if checkProcess == True:
                read = os.scandir(path)
                return read
            else:
                return False
        except Exception as e:
            print(e) 
        
    def useDirecotry(self, name):
        try:
            path = Path.process
            pathNew = path+'\\'+name
            checkProcess = self.isNotOnProcess(pathNew)
            
            if checkProcess == False:
                return pathNew
            else:
                print("Folder not Found!")
                return False
        except Exception as e:
            print(e)
            return False
    
    def copy(self, sourcePath, destinationPath):
        try:
            command = r'copy "'+sourcePath+'" "'+destinationPath+'"'
            os.system(command)
            return True
        except Exception as e:
            print(e)
            return False


    def copyFromComponent(self, fileName, destinationPath):
        try:
            # path = Path.process#+'\\'+name
            path = Path.master_component
            pathDestination = destinationPath+'\\'+fileName
            pathSource = path+'\\'+fileName
            # print('pathDestination : '+pathDestination)
            # print('pathSource : '+pathSource)
            self.copy(pathSource, pathDestination)
            # if checkProcess == False:
                # return pathNew
            return True
            # else:
            #     return False
        except Exception as e:
            print(e)
            return False
