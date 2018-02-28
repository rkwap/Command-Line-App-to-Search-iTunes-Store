import unittest
import json
import proj1_w18 as proj1

####################
###### Part 1 ######
####################

class TestMedia(unittest.TestCase):
	
	def testConstructor(self):
		m1 = proj1.Media()
		m2 = proj1.Media("1999", "Prince", 1982)

		self.assertEqual(m1.title, "No Title")
		self.assertEqual(m1.author, "No Author")
		self.assertEqual(m1.release_year, "No Release Year")
		self.assertEqual(m2.title, "1999")
		self.assertEqual(m2.author, "Prince")
		self.assertEqual(m2.release_year, 1982)
		self.assertRaises(AttributeError, lambda: m2.album)
		self.assertRaises(AttributeError, lambda: m2.genre)
		self.assertRaises(AttributeError, lambda: m2.track_length)
		self.assertRaises(AttributeError, lambda: m2.rating)
		self.assertRaises(AttributeError, lambda: m2.movie_length)

	def testStr(self):
		m2 = proj1.Media("1999", "Prince", 1982)

		self.assertEqual(m2.__str__(), "1999 by Prince (1982)")

	def testLen(self):
		m2 = proj1.Media("1999", "Prince", 1982)

		self.assertEqual(m2.__len__(), 0)

class TestSong(unittest.TestCase):
	
	def testConstructor(self):
		s1 = proj1.Song()
		s2 = proj1.Song("Havana", "Camila Cabello", 2018, "Camila", "Pop", 216)

		self.assertEqual(s1.album, "No Album")
		self.assertEqual(s1.track_length, "No Track Length")
		self.assertEqual(s2.title, "Havana")
		self.assertEqual(s2.author, "Camila Cabello")
		self.assertEqual(s2.release_year, 2018)
		self.assertEqual(s2.album, "Camila")
		self.assertEqual(s2.genre, "Pop")
		self.assertEqual(s2.track_length, 216)
		self.assertRaises(AttributeError, lambda: s2.rating)
		self.assertRaises(AttributeError, lambda: s2.movie_length)

	def testStr(self):
		s2 = proj1.Song("Havana", "Camila Cabello", 2018, "Camila", "Pop", 216)

		self.assertEqual(s2.__str__(), "Havana by Camila Cabello (2018) [Pop]")

	def testLen(self):	
		s2 = proj1.Song("Havana", "Camila Cabello", 2018, "Camila", "Pop", 216)

		self.assertEqual(s2.__len__(), 216)

class TestMovie(unittest.TestCase):

	def testConstructor(self):
		m1 = proj1.Movie()
		m2 = proj1.Movie("The Chorus", "Christophe Barratier", 2005, "PG-13", 95)

		self.assertEqual(m1.rating, "No Rating")
		self.assertEqual(m1.movie_length, "No Movie Length")
		self.assertEqual(m2.title, "The Chorus")
		self.assertEqual(m2.author, "Christophe Barratier")
		self.assertEqual(m2.release_year, 2005)
		self.assertEqual(m2.rating,"PG-13")
		self.assertEqual(m2.movie_length, 95)
		self.assertRaises(AttributeError, lambda: m2.album)
		self.assertRaises(AttributeError, lambda: m2.genre)
		self.assertRaises(AttributeError, lambda: m2.track_length)

	def testStr(self):
		m2 = proj1.Movie("The Chorus", "Christophe Barratier", 2005, "PG-13", 95)

		self.assertEqual(m2.__str__(), "The Chorus by Christophe Barratier (2005) [PG-13]")

	def testLen(self):
		m2 = proj1.Movie("The Chorus", "Christophe Barratier", 2005, "PG-13", 95)

		self.assertEqual(m2.__len__(), 95)


####################
###### Part 2 ######
####################

class TestJson(unittest.TestCase):
	
	def testMedia(self):
		f = open("sample_json.json","r")
		sample_data = json.loads(f.read())
		f.close()
		
		m = proj1.Media(json=sample_data[2])

		self.assertEqual(m.title, "Bridget Jones's Diary (Unabridged)")
		self.assertEqual(m.author, "Helen Fielding")
		self.assertEqual(m.release_year, "2012")
		self.assertEqual(m.__str__(), "Bridget Jones's Diary (Unabridged) by Helen Fielding (2012)")
		self.assertEqual(m.__len__(), 0)

	def testSong(self):
		f = open("sample_json.json","r")
		sample_data = json.loads(f.read())
		f.close()
		
		s = proj1.Song(json=sample_data[1])
		
		self.assertEqual(s.title, "Hey Jude")
		self.assertEqual(s.author, "The Beatles")
		self.assertEqual(s.release_year, "1968")
		self.assertEqual(s.album, "TheBeatles 1967-1970 (The Blue Album)")
		self.assertEqual(s.genre, "Rock")
		self.assertEqual(s.track_length, 431333)
		self.assertEqual(s.__str__(), "Hey Jude by The Beatles (1968) [Rock]")
		self.assertEqual(s.__len__(), 431)


	def testMovie(self):
		f = open("sample_json.json","r")
		sample_data = json.loads(f.read())
		f.close()
		
		m = proj1.Movie(json=sample_data[0])
		
		self.assertEqual(m.title, "Jaws")
		self.assertEqual(m.author, "Steven Spielberg")
		self.assertEqual(m.release_year, "1975")
		self.assertEqual(m.rating, "PG")
		self.assertEqual(m.movie_length, 7451455)
		self.assertEqual(m.__str__(), "Jaws by Steven Spielberg (1975) [PG]")
		self.assertEqual(m.__len__(), 124)



####################
###### Part 3 ######
####################

class TestResponses(unittest.TestCase):

	def testCommonWordsAndLessCommonWords(self):
		l1 = proj1.all_media_lst("love")
		l2 = proj1.all_media_lst("baby")
		l3 = proj1.all_media_lst("moana")
		l4 = proj1.all_media_lst("helter skelter")

		self.assertIn(len(l1), range(1,51))
		self.assertIn(len(l2), range(1,51))
		self.assertIn(len(l3), range(1,51))
		self.assertIn(len(l4), range(1,51))

	def testNonsenseQueries(self):
		l1 = proj1.all_media_lst("jsdcnkasjknck")
		l2 = proj1.all_media_lst("&^scnka&*s**$#%^&")

		self.assertEqual(l1, [])
		self.assertEqual(l2, [])

	def testBlankQuery(self):
		l1 = proj1.all_media_lst(" ")

		self.assertEqual(l1, [])




unittest.main()
