from app import ma, Marshmallow


class AnimeSchema(ma.Schema):
    class Meta:
        fields = ('artist_id', 'artist_en', 'artist_romaji', 'artist_kanji')
        
        
anime_schema = AnimeSchema()