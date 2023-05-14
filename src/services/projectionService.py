import jsons
import sys
sys.path.append('../')
from services.animeService import AnimeService
from services.animeOstService import AnimeOstService
from services.folderService import FolderService as DS
from services.folderNameService import FolderNameService as DNS
from services.archiveService import ArchiveService
from services.fileService import FileService
from services.animeStatusService import AnimeStatusService as AnimeStatusHandler

from systems.response import Responses
from systems.master import Master



class ProjectionService():

	# def requestHeader(self, url):
	# 	headers = request.Request._header
	# 	html = requests.get(url, headers=headers)
	# 	return html

	def create_anime_folder(id):
		getData = AnimeService.getById(id)
		name = getData['anime_title_romaji']  
		# print(getData['anime_title_romaji'])
		action = DS().createDirectoryByName(name)
  
		return action

	# remove foler basic
	# def remove_anime_folder(id):
	# 	getData = AnimeService.getById(id)
	# 	name = getData['anime_title_romaji']  
	# 	# print(getData['anime_title_romaji'])
	# 	path = DS().useDirecotry(name)
	# 	action = DS().removeDirecotry(name)
	# 	return action

	def remove_anime_folder(id):
		try:
			getData = AnimeService.getById(id)
			name = getData['anime_title_romaji']  
			# print(getData['anime_title_romaji'])
			path = DS().useDirecotry(name)
			action = DS().removeDirecotry(path)
			AnimeStatusHandler.resetStatus(id)   
			responseResult = Responses.response('success')
   
			return jsons.dumps(responseResult), Responses._content_type
			# return responseResult
		except Exception as e:
			print(e)
			responseResult = Responses.response('failed')
			responseResult['message'] = str(e)
			return jsons.dumps(responseResult), Responses._content_type
			# return responseResult  
     


	def create_anime_ost_folder(id):
		try:      
			getAnime = AnimeService.getById(id)
			name = getAnime['anime_title_romaji']
			createAnimeFolder = DS().createDirectoryByName(name)	
			path = DS().useDirecotry(name)
	
			getOst = AnimeOstService.getById(id)
			for row in getOst:
				artist_romaji = row['artist_romaji']
				romaji_song = row['romaji_song']
				type_song = row['type_song']
				track_song = row['track_song']
				type =''
				if type_song == 'OP / Opening':
					type = 'OP'
				elif type_song == 'ED / Ending':
					type = 'ED'
				anime = DNS().convert("anime", name)
				artist = DNS().convert("artist", artist_romaji)
				song = DNS().convert("song", romaji_song)
				# print(anime)
				# print(artist)
				# print(song)
				
				code = type+str(track_song)
				songFolder = code+'__'+artist_romaji+' - '+romaji_song+"_-_"+anime+"_"+code+"_"+artist+song
    
				action = DS().createDirectoryByPath(path, songFolder)    
				pathDestination = path+'\\'+songFolder
				DS().copyFromComponent(Master.single, pathDestination)
    
				# DS().copyFromComponent(Master.single, pathDestination)
    
			# for row in getOst:
			# 	artist_romaji = row['artist_romaji']
			# 	romaji_song = row['romaji_song']
			# 	type_song = row['type_song']
			# 	track_song = row['track_song']
			# 	type =''
			# 	if type_song == 'OP / Opening':
			# 		type = 'OP'
			# 	elif type_song == 'ED / Ending':
			# 		type = 'ED'
	
			# 	code = type+str(track_song)
			# 	songFolder = code+'_'+artist_romaji+' - '+romaji_song 
			# 	pathDestination = path+'\\'+songFolder
    
			AnimeStatusHandler().statusControl(id, 'is_folder')

			responseResult = Responses.response('success')
			return jsons.dumps(responseResult), Responses._content_type
			# return responseResult
		except Exception as e:
			print(e)
			responseResult = Responses.response('failed')
			responseResult['message'] = str(e)
			return jsons.dumps(responseResult), Responses._content_type
			# return responseResult  


	def create_anime_ost_folder_archive(id):
		try:
			getAnime = AnimeService.getById(id)
			name = getAnime['anime_title_romaji']
			# print(name)
   
			path = DS().useDirecotry(name)
			# print(path)
   
			directores = DS().readDirectory(path)
			archiveAction = ArchiveService().doArchive(path, directores)
			# print("archiveAction : "+archiveAction)
			AnimeStatusHandler().statusControl(id, 'is_archive')   
			responseResult = Responses.response('success')
			return responseResult
			# archive(pathResult, pathDirection)
		except Exception as e:
			print(e)
			responseResult = Responses.response('failed')
			responseResult['message'] = str(e)
			return responseResult  


	def rename_anime_ost_file(id):
		try:
			# print('flag 2 ')
			getAnime = AnimeService.getById(id)
			name = getAnime['anime_title_romaji']
			# print(name)
   
			path = DS().useDirecotry(name)
			# print(path)
   
			directores = DS().readDirectory(path)
   
			FileService().rename_batch(directores, path)
			AnimeStatusHandler().statusControl(id, 'is_rename')
			responseResult = Responses.response('success')
			return responseResult
   
			# archiveAction = ArchiveService().doArchive(name, path, directores)
			# print(archiveAction)
			# archive(pathResult, pathDirection)
		except Exception as e:
			print(e)
			responseResult = Responses.response('failed')
			responseResult['message'] = str(e)
			return responseResult  




	def getOstAnime(id):
		getData = AnimeOstService.getById(id)
		
		return getData