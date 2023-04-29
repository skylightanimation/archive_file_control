import sys
sys.path.append('../')
from repositories.animeRepository import AnimeRepository as AnimeRepo
from vmodels.vm_anime import AnimeSchema, anime_schema


class AnimeService():
    def getById(id):
        try:
            data = AnimeRepo.get_by_id(id)
            result = anime_schema.dump(data)
            return result
        except Exception as e:
            print(e)
            return False