# from flask import render_template, request, redirect, flash, url_for
# import flask
from flask import request, Blueprint
from app import app
import sys
sys.path.append('../')
from services.projectionService import ProjectionService as ProjectionHandler



# @app.route('/testss')
# def tests():
#     dataAnime = ProjectionHandler.test()
#     print(dataAnime.anime_title_romaji)
#     return 'Hello WOrld'


# @app.route('/do', methods=['POST'])
# def doById():
#     data = request.get_json()
#     ID = int(data['id'])
#     dataAnime = ProjectionHandler.tes(ID)
#     return 'Hello WOrld'


@app.route('/create_folder', methods=['POST'])
# @REQUEST_API.route('/create_folder', methods=['POST'])
def create_folder():
    data = request.get_json()
    ID = int(data['id'])
    dataAnime = ProjectionHandler.create_anime_ost_folder(ID)
    return dataAnime


@app.route('/create_archive', methods=['POST'])
# @REQUEST_API.route('/create_archive', methods=['POST'])
def create_archive():
    data = request.get_json()
    ID = int(data['id'])
    dataAnime = ProjectionHandler.create_anime_ost_folder_archive(ID)
    return dataAnime


@app.route('/rename_song', methods=['POST'])
# @REQUEST_API.route('/rename_song', methods=['POST'])
def rename_song():
    data = request.get_json()
    ID = int(data['id'])
    dataAnime = ProjectionHandler.rename_anime_ost_file(ID)
    return dataAnime


# @app.route('/auth', methods=['POST'])  
# @token_required
# def auth(authUser): 
#     # auth = request.authorization
#     data = request.get_json()
#     salt = str(security.BlackJack._salt)
#     result = Result._result
#     resultData = Result._result['data']

#     email=data['username']
#     password=data['password']
#     id_app=data['application']