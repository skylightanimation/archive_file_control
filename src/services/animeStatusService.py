import sys
sys.path.append('../')
from repositories.animeStatusRepository import AnimeStatusRepository as AnimeStatusRepo
from vmodels.vm_anime_status import AnimeStatusSchema, anime_status_schema
from systems.response import Responses

class AnimeStatusService():
    def getById(id):
        try:
            data = AnimeStatusRepo.get_by_id(id)
            result = anime_status_schema.dump(data)
            return result
        except Exception as e:
            print(e)
            return False
        
        
    def isExist(self, id):
        try:
            check = AnimeStatusRepo.get_by_id(id)
            result = anime_status_schema.dump(check)
            
            print(check)
            print(result)         
            # save = []
            if(len(result) < 0):
                # save['id'] = id
                # data = AnimeStatusRepo.add(save)
                return True
            else:
                return False
                # data = AnimeStatusRepo.saveIsFolder(save)
                # print(result)
                # return result
        except Exception as e:
            print(e)
            return False
    
    
    def statusControl(self, id, type):
        try:
            checkStatus = self.isExist(id)
            # check = AnimeStatusRepo.get_by_id(id)
            # result = anime_status_schema.dump(check)
            print(checkStatus)
            save = []
            if(checkStatus == False):
                # save['id'] = id
                do = AnimeStatusRepo.add(id)
                return True
            else:
                if(type == 'create_folder'):
                    save['is_folder'] = id
                    do = AnimeStatusRepo.saveIsFolder(save)
                elif(type == 'rename_file'):
                    save['is_rename'] = id
                    do = AnimeStatusRepo.saveIsRename(save)
                elif(type == 'create_archive'):
                    save['is_archive'] = id
                    do = AnimeStatusRepo.saveIsArchive(save)
                # print(result)
                return True
                # return result
        except Exception as e:
            print(e)
            return False


    def resetStatus(id):
        try:
            data = AnimeStatusRepo.delete(id)
            # return True
            responseResult = Responses.response('success')
            return responseResult
        except Exception as e:
            print(e)
            responseResult = Responses.response('failed')
            responseResult['message'] = str(e)
            return responseResult