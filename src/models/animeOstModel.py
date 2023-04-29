from app import db
from sqlalchemy.orm.attributes import InstrumentedAttribute
from models.animeModel import *
from models.artistModel import Artist

class AnimeOst(db.Model):
    __tablename__ = 'anime_ost'

    id_song = db.Column(db.String, unique=True, primary_key=True, nullable=False,)
    en_song = db.Column(db.String, nullable=False)
    romaji_song = db.Column(db.String, nullable=False)
    kanji_song = db.Column(db.String, nullable=False)
    release_song = db.Column(db.Date, nullable=False)
    type_song = db.Column(db.String, nullable=False)
    track_song = db.Column(db.Integer, nullable=False)
    img_song = db.Column(db.String, nullable=False)
    # artist_id = db.Column(db.String, nullable=False)
    # anime_id = db.Column(db.String, nullable=False)

    # billing_address_id = mapped_column(Integer, ForeignKey("address.id"))
    # shipping_address_id = mapped_column(Integer, ForeignKey("address.id"))

    artist_id = db.Column(db.String, db.ForeignKey(Artist.artist_id))
    # artists = db.relationship('anime_ost', backref='artist')
    # artist_anime_ost = db.relationship(Artist.artist_id, backref=db.backref('Artist'), lazy=True)
    # anime_ost_artist = db.relationship('anime_ost', backref='artist', lazy=False)
    # anime_ost_artist = db.relationship("anime_ost", foreign_keys=[artist_id])
    # anime_ost_artist = db.relationship("anime_ost", foreign_keys=[artist_id])
    # artists = db.relationship(lambda: Artist,
    #                          primaryjoin=lambda: db.and_(
    #                              AnimeOst.artist_id == Artist.artist_id,
    #                              Artist.artist_id == db.bindparam('artist_id')))
    
    anime_id = db.Column(db.String, db.ForeignKey(Anime.anime_id))
    # anime_ost = db.relationship(Anime.anime_id, backref=db.backref('Anime'), lazy=True)
    # anime_ost = db.relationship('anime_ost', backref='anime', lazy=False)
    # anime_ost = db.relationship("anime_ost", foreign_keys=[anime_id])
    
    # id_role = db.Column(db.Integer, db.ForeignKey(Role.id))
    # roleAccess = db.relationship(Role, backref=db.backref('role'), lazy=True)
    # id_app = db.Column(db.Integer, db.ForeignKey(App.id))
    # appAccess = db.relationship(App, backref=db.backref('app'), lazy=True)

    # anime_id 
    # anime_title_en = db.Column(db.String, nullable=False)
    # anime_title_romaji = db.Column(db.String, nullable=False)
    # anime_title_kanji = db.Column(db.String, nullable=False)
    # anime_title_other = db.Column(db.String, nullable=False)
    # anime_release = db.Column(db.String, nullable=False)
    # anime_season = db.Column(db.String, nullable=False)
    # anime_episodes = db.Column(db.String, nullable=False)
    # anime_source = db.Column(db.String, nullable=False)
    # anime_type = db.Column(db.String, nullable=False)
    # anime_img_width = db.Column(db.String, nullable=False)
    # anime_img_square = db.Column(db.String, nullable=False)
    # anime_modify = db.Column(db.Date, nullable=False)


    # access = db.relationship('Access', backref='id_user', lazy=True)

    # def __repr__(self):
    #     return "<Name: {}>".format(self.anime_title_en, self.anime_title_romaji)