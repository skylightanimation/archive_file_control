import os

class Package():
	_data = {}
	_data['name'] = 'FileGen'
	_data['version'] = '1.0.0'
	_data['release'] = '2023-03-12'
	_data['author'] = 'Ar'

class Config():
	_db = {}
	_db['uname'] = 'root'
	_db['pswd'] = ''
	_db['host'] = 'localhost'
	_db['port'] = '3306'
	_db['db'] = 'raitostproject_ff_db'

class Security():
	_data = {}
	_data['salt'] = 'fly me to the moon'
	_data['secret_key'] = 'Hall0W0rld'
	_data['archive_password'] = 'raitOST#Project'


class API():
	_auth = "http://localhost:5000/auth"
	_auth_content = {"username":"","password":"","application":""}
	_auth_header = {"x-access-tokens":"", "Content-Type":"application/json"}
	_login = "http://localhost:5000/login"
	_login_header = ""
 
class Response():
	_contentType = {"Content-Type":"application/json"}
	_successResponse = dict(status="200",message="success",data=[])
	_failedResponse = dict(status="401",message="failed",)
	_notfoundResponse = dict(status="404",message="not found")
	_errorResponse = dict(status="503",message="")


class Path:
	_master  = r'D:\Python\fileGenerator_BackEnd\data\master'
	_master_component  = r'D:\Python\fileGenerator_BackEnd\data\master\components'
	_process = r'D:\Python\fileGenerator_BackEnd\data\process'
	_result  = r'D:\Python\fileGenerator_BackEnd\data\results'
	_archive = r'D:\BLOG\OSTProject\__Archive'
 
 
class Master:
    _embeddedFileRedirectPage = {}
    _embeddedFileRedirectPage['pack'] = 'visit our blog!!! [Anime-Sunset].html'
    _embeddedFileRedirectPage['single'] = 'RaitOST.html'
    _brand = 'RaitOST'
    _type_string = ['anime', 'artist', 'song']
    
class Thirdparty:
    _tool = {}
    _tool['archive'] = r'C:\Program Files\7-Zip\7z.exe'