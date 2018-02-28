
import requests
import json
import webbrowser

#################################
######## Part 1 & Part 2 ########
#################################

class Media:

	def __init__(self, title = "No Title", author="No Author", release_year="No Release Year", url = "No URL", json=None):
		self.json = json
		if self.json != None:
			if "collectionName" in json.keys():
				self.title = json["collectionName"]
			else:
				self.title = "No Title"
			if "artistName" in json.keys():
				self.author = json["artistName"]
			else: 
				self.author = "No Author"
			if "releaseDate" in json.keys():
				self.release_year = json["releaseDate"][0:4]
			else:
				self.release_year = "No Release Year"
			if "collectionViewUrl" in json.keys():
				self.url = json["collectionViewUrl"]
			else: 
				self.url = "No URL"
		else:
			self.title = title
			self.author = author
			self.release_year = release_year
			self.url = url

	def __str__(self):
		return "{} by {} ({})".format(self.title, self.author, self.release_year)

	def __len__(self):
		return 0

class Song(Media):

	def __init__(self, title = "No Title", author="No Author", release_year="No Release Year", album = "No Album", genre = "No Genre", track_length = "No Track Length", url = "No URL", json=None):
		self.json = json
		if self.json != None:	
			if "trackName" in json.keys():
				self.title = json["trackName"]	
			else: 
				self.title = "No Title"
			if "artistName" in json.keys():
				self.author = json["artistName"]
			else: 
				self.author = "No Author"
			if "releaseDate" in json.keys():
				self.release_year = json["releaseDate"][0:4]
			else:
				self.release_year = "No Release Year"
			if "collectionName" in json.keys():
				self.album = json["collectionName"]
			else:
				self.album = "No Album"
			if "primaryGenreName" in json.keys():
				self.genre = json["primaryGenreName"]
			else:
				self.genre = "No Genre"
			if "trackTimeMillis" in json.keys():
				self.track_length = json["trackTimeMillis"]
			else:
				self.track_length = "No Track Length"
			if "trackViewUrl" in json.keys():
				self.url = json["trackViewUrl"]
			else:
				self.url = "No URL"
		else:
			super().__init__(title, author, release_year, url)
			self.album = album
			self.genre = genre
			self.track_length = track_length

	def __str__(self):
		return super().__str__() + " [{}]".format(self.genre)

	def __len__(self):
		if self.json != None:
			len_in_sec = int(self.track_length/1000)
			return len_in_sec
		else:
			return self.track_length

class Movie(Media):

	def __init__(self, title="No Title", author="No Author", release_year="No Release Year", rating = "No Rating", movie_length = "No Movie Length", url = "No URL",json=None):
		self.json = json
		if self.json != None:
			if "trackName" in json.keys():
				self.title = json["trackName"]
			else:
				self.title = "No Title"
			if "artistName" in json.keys():
				self.author = json["artistName"]
			else: 
				self.author = "No Author"
			if "releaseDate" in json.keys():
				self.release_year = json["releaseDate"][0:4]
			else:
				self.release_year = "No Release Year"
			if "contentAdvisoryRating" in json.keys():
				self.rating = json["contentAdvisoryRating"]
			else:
				self.rating = "No Rating"
			if "trackTimeMillis" in json.keys():
				self.movie_length = json["trackTimeMillis"]
			else: 
				self.movie_length = "No Movie Length"
			if "trackViewUrl" in json.keys():
				self.url = json["trackViewUrl"]
			else:
				self.url = "No URL"
		else: 		
			super().__init__(title, author, release_year, url)
			self.rating = rating
			self.movie_length = movie_length

	def __str__(self):
		return super().__str__() + " [{}]".format(self.rating)

	def __len__(self):
		if self.json != None:
			len_in_min = int(self.movie_length/60000)
			return len_in_min
		else: 
			return self.movie_length


########################
######## Part 3 ########
########################


def iTunes_search(term):
    baseurl = "https://itunes.apple.com/search"
    params_diction = {}
    params_diction["term"] = term

    iTunes_resp = requests.get(baseurl, params = params_diction)
    iTunes_resp_text = iTunes_resp.text
    iTunes_data = json.loads(iTunes_resp_text)
    
    return iTunes_data


def media_type_sorter(data):
	media_dict = {}
	song_lst = []
	movie_lst = []
	other_media_lst = []

	for d in data["results"]:
		if d["kind"] == "song":
			media_inst = Song(json=d)
			song_lst.append(media_inst)
		elif d["kind"] == "feature-movie":
			media_inst = Movie(json=d)
			movie_lst.append(media_inst)
		else:
			media_inst = Media(json=d)
			other_media_lst.append(media_inst)

	media_dict["Songs"] = song_lst
	media_dict["Movies"] = movie_lst
	media_dict["Other Media"] = other_media_lst
	
	return media_dict


def all_media_lst(term):
	search_results = iTunes_search(term)
	media_dict = media_type_sorter(search_results)
	
	song_lst = media_dict["Songs"]
	movie_lst = media_dict["Movies"]
	other_media_lst = media_dict["Other Media"]
	all_media_lst= song_lst + movie_lst + other_media_lst
	
	song_len = len(song_lst)
	movie_len = len(movie_lst)
	other_media_len = len(other_media_lst)
	
	if song_len >= 1:
		print("SONGS")
		for i in range(song_len):
			print("{} {}".format(i + 1, all_media_lst[i].__str__()))
	if movie_len >= 1:
		print("MOVIES")
		for j in range(song_len, song_len + movie_len):
			print("{} {}".format(j + 1, all_media_lst[j].__str__()))	
	if other_media_len >= 1:
		print("OTHER MEDIA")
		for k in range(song_len + movie_len, song_len + movie_len + other_media_len):
			print("{} {}".format(k + 1, all_media_lst[k].__str__()))

	return all_media_lst


########################
######## Part 4 ########
########################



def main():
	user_input = input('Enter a search term, or enter "exit" to quit:')
	if user_input != "exit":
		screen_output = all_media_lst(user_input)
		while screen_output == []:
			user_input = input('Sorry! Your search returned no results. Please try another search term:')
			screen_output = all_media_lst(user_input)
		user_input = input('Enter a number for more info, or another search term, or exit:')	
		while user_input != "exit":
				try:
					if screen_output[int(user_input) - 1].url != "No URL":
						media_url = screen_output[int(user_input) - 1].url
						print("Launching {} in web browser...".format(media_url))
						webbrowser.open_new(media_url)
						user_input = input('Enter a number for more info, or another search term, or exit:')
					else:
						user_input = input('Sorry! URL not found. Unable to launch web browser. Enter a number for more info, or another search term, or exit:')

				except:
					screen_output = all_media_lst(user_input)
					while screen_output == []:
						user_input = input('Sorry! Your search returned no results. Please try another search term:')
						screen_output = all_media_lst(user_input)
					user_input = input('Enter a number for more info, or another search term, or exit:')	

			
				
						

if __name__ == "__main__":
	main()
	
