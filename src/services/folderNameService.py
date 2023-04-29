import sys
import re
sys.path.append('../')
from systems.master import Master

class FolderNameService():
    
    def countSpace(self, text):
        try:
            result = text.count(' ')

            return result
        except Exception as e:
            print(e)
            return False
        
    def removeSpecialCharacter(self, text):        
        try:
            result = re.sub('[!@#$:+.,]', '', text)
            # print(result)
            return result
        except Exception as e:
            print(e)
            return False
        
    def word(self, name):
        try:
            textFirst = ''
            textLast = ''
            textLength = len(name)
            if textLength <= 3:
               textFirst = name[:1]
               textLast = name[-1:]
            elif textLength <= 6:
               textFirst = name[:2]
               textLast = name[-1:]  
            elif textLength > 6:
               textFirst = name[:3]
               textLast = name[-2:]
            result = textFirst+textLast
            return result
        except Exception as e:
            print(e)
            return False   

    def convert(self, type, title):
        try:
            Master.typeString[0]
            text = self.removeSpecialCharacter(title)
            arrayTitle = text.split(' ')
            archiveName = '' 
            stringResult = ''
            for row in arrayTitle:
                textRow = self.word(row)
                stringResult=stringResult+textRow
            
            if type == Master.typeString[0]: #'anime':
                archiveName = '['+Master.brand+']'+stringResult
            elif type == Master.typeString[1]: #'artist':
                archiveName = stringResult
            elif type == Master.typeString[2]: #'song':
                archiveName = '-'+stringResult
            
            return archiveName
        except Exception as e:
            print(e)
            return False   

    def getIndex(text, sparated):
        try:
            value = text.index(sparated)
            valueIndex = value-1
            # print(value)
            return valueIndex
        except Exception as e:
            print(e)
            return False 