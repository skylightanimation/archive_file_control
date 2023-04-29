import sys
sys.path.append('../')
from repositories.animeOstRepository import AnimeOstRepository as AnimeOstRepo
from vmodels.vm_anime_ost import anime_osts_schema


class AnimeOstService():
    def getById(id):
        try:
            data = AnimeOstRepo.get_by_anime_id(id)
            result = anime_osts_schema.dump(data)
            return result
        except Exception as e:
            print(e)
            return False