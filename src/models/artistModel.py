from app import db
from models.animeOstModel import *

class Artist(db.Model):
    __tablename__ = 'artist'

    artist_id = db.Column(db.String, unique=True, primary_key=True, nullable=False)
    artist_en = db.Column(db.String, nullable=False)
    artist_romaji = db.Column(db.String, nullable=False)
    artist_kanji = db.Column(db.String, nullable=False)
    # artists = db.relationship(lambda: Artist,
    #                          primaryjoin=lambda: db.and_(
    #                              AnimeOst.artist_id == Artist.artist_id,
    #                              Artist.artist_id == db.bindparam('artist_id')))