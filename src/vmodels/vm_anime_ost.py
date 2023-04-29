from app import ma, Marshmallow


class AnimeOstSchema(ma.Schema):
    class Meta:
        fields = ('id_song', 'en_song', 'romaji_song', 'kanji_song', 'release_song', 'type_song', 'track_song', 'img_song', 'anime_id', 'artist_id', 'artist_en', 'artist_romaji', 'artist_kanji')
        
        
anime_ost_schema = AnimeOstSchema()
anime_osts_schema = AnimeOstSchema(many=True)