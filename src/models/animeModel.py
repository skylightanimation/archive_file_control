from app import db

class Anime(db.Model):
    __tablename__ = 'anime'

    anime_id = db.Column(db.String, unique=True, primary_key=True, nullable=False,)
    anime_title_en = db.Column(db.String, nullable=False)
    anime_title_romaji = db.Column(db.String, nullable=False)
    anime_title_kanji = db.Column(db.String, nullable=False)
    anime_title_other = db.Column(db.String, nullable=False)
    anime_release = db.Column(db.String, nullable=False)
    anime_season = db.Column(db.String, nullable=False)
    anime_episodes = db.Column(db.String, nullable=False)
    anime_source = db.Column(db.String, nullable=False)
    anime_type = db.Column(db.String, nullable=False)
    anime_img_width = db.Column(db.String, nullable=False)
    anime_img_square = db.Column(db.String, nullable=False)
    anime_modify = db.Column(db.Date, nullable=False)


    # access = db.relationship('Access', backref='id_user', lazy=True)

    # def __repr__(self):
    #     return "<Name: {}>".format(self.anime_title_en, self.anime_title_romaji)