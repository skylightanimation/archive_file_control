import sqlalchemy 

import sys
sys.path.append('../')

from models.animeModel import Anime
from models.animeOstModel import db, AnimeOst
from models.artistModel import Artist

class AnimeOstRepository():

    def get_all():
        result = AnimeOst.query.filter_by().all()
        return result

    def get_by_anime_id(id):
        ID = str(id)
        result = AnimeOst.query\
            .join(Artist, AnimeOst.artist_id==Artist.artist_id)\
            .add_columns(AnimeOst.id_song, AnimeOst.en_song, AnimeOst.romaji_song, AnimeOst.kanji_song, AnimeOst.release_song, AnimeOst.type_song, AnimeOst.track_song, AnimeOst.img_song, AnimeOst.anime_id, Artist.artist_id, Artist.artist_en, Artist.artist_romaji, Artist.artist_kanji)\
            .filter(AnimeOst.anime_id == ID).all()
        return result
        
        
