# from app import app

import sys
sys.path.append('../')

from models.animeStatusModel import db, AnimeStatus

class AnimeStatusRepository():

    def get_all():
        result = AnimeStatus.query.filter_by().all()
        print(result)
        return result

    def get_by_id(id):
        result = AnimeStatus.query.filter_by(anime_id=id).first()
        return result

    # def insert(data):
    #     result = AnimeStatus.query.filter_by().all()
    #     print(result)
    #     return result

    # def update(id):
    #     result = AnimeStatus.query.filter_by(anime_id=id).first()
    #     return result
    
    
    def add(id):
        try:
            save = AnimeStatus(anime_id=id)
            db.session.add(save)
            db.session.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def saveIsArchive(data):
        try:
            updated = AnimeStatus.query.get(data['id'])
            updated.is_archive = data['is_archive']
            db.session.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def saveIsFolder(data):
        try:
            updated = AnimeStatus.query.get(data['id'])
            updated.is_folder = data['is_folder']
            db.session.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def saveIsRename(data):
        try:
            updated = AnimeStatus.query.get(data['id'])
            updated.is_rename = data['is_rename']
            db.session.commit()
            return True
        except Exception as e:
            print(e)
            return False

    
    def delete(id):
        try:
            remove = AnimeStatus.query.filter_by(anime_id=id).delete()
            db.session.commit()
            return True
        except Exception as e:
            print(e)
            return False