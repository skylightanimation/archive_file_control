# from app import app

import sys
sys.path.append('../')

from models.animeModel import db, Anime

class AnimeRepository():

    def get_all():
        result = Anime.query.filter_by().all()
        print(result)
        return result

    def get_by_id(id):
        result = Anime.query.filter_by(anime_id=id).first()
        return result

    # def search_by_name(name):
    #     print(name)
    #     try:
    #         result = Anime.query.filter_by(is_deleted=False, Anime.anime_title_romaji.like(name)).all()
    #         return result
    #     except Exception as e:
    #         return e