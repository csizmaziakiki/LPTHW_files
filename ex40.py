class Song(object):

	def __init__(self, lyrics):
		self.lyrics = lyrics

	def sing_me_a_song(self):
		for line in self.lyrics:
			print line

happy_bday = Song(["Happy birthday to you, blabla..."])
bored = Song(["Back on earth I'm nearly bored to death..."])

happy_bday.sing_me_a_song()
bored.sing_me_a_song()

