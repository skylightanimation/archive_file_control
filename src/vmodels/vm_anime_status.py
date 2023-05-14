from app import ma, Marshmallow


class AnimeStatusSchema(ma.Schema):
    class Meta:
        fields = ('id', 'anime_id', 'is_archive', 'is_folder', 'is_rename')
        
        
anime_status_schema = AnimeStatusSchema()