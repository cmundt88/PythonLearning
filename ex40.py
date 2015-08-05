class Song(object):

	def __init__(self, lyrics):
		self.lyrics = lyrics
		self.test_variable = "testing"
	
	def sing_me_a_song(self):
		for line in self.lyrics:
			print line

tea_cup = ["short and stout", "here is my handle", "here is my spout"]
			
happy_bday = Song(["Happy birthday to you",
					"I don't want you to get sued",
					"So I'll stop right there"])
					
bulls_on_parade = Song(["They rally around the family",
						"With pockets full of shells"])
						
numerical_song = Song([1, 2, 3, 4])
						
happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

numerical_song.sing_me_a_song()

Song(["Shut your face"]).sing_me_a_song()

Song(tea_cup).sing_me_a_song()

print happy_bday.test_variable

happy_bday.test_variable = "now changed"

print happy_bday.test_variable