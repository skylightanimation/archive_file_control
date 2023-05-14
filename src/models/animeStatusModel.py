from app import db
from models.animeModel import *

class AnimeStatus(db.Model):
    __tablename__ = 'anime_status'
    id = db.Column(db.Integer, unique=True, primary_key=True, nullable=False)
    # anime_id = db.Column(db.String, nullable=False)
    anime_id = db.Column(db.String, db.ForeignKey(Anime.anime_id))
    is_folder = db.Column(db.Boolean, nullable=False, default=True)
    is_rename = db.Column(db.Boolean, nullable=False, default=False)
    is_archive = db.Column(db.Boolean, nullable=False, default=False)
