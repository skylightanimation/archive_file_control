from flask import request
from app import app
import sys
sys.path.append('../')
from services.animeStatusService import AnimeStatusService as AnimeStatusHandler


@app.route('/test/isExist', methods=['GET'])
def test_isExist():
    # data = request.get_json()
    ID = int('2019060539386621')
    dataAnime = AnimeStatusHandler.isExist(ID)
    print(dataAnime)
    return dataAnime

@app.route('/status/reset', methods=['POST'])
def status_reset():
    data = request.get_json()
    ID = int(data['id'])
    print(ID)
    dataAnime = AnimeStatusHandler.resetStatus(ID)
    # print(len(dataAnime))
    return dataAnime
