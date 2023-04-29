from app import ma, Marshmallow


class AnimeSchema(ma.Schema):
    class Meta:
        fields = ('anime_id', 'anime_title_en', 'anime_title_romaji', 'anime_title_kanji', 'anime_title_other', 'anime_release', 'anime_season', 'anime_episodes', 'anime_source', 'anime_type', 'anime_img_width', 'anime_img_square', 'anime_modify')
        
        
anime_schema = AnimeSchema()