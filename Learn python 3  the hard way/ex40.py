class song:
    name = "song class" #Class variable
    def __init__(self,lyrics): #parametrized constructor
        self.lyrics = lyrics   #instance variable

    def sing_a_song(self): #instance method
        for a in self.lyrics:
            print(a)

happy = ["hey","happy_bday1","happy_bday2"]
happy_bday = song(happy)
print(happy_bday.name)
sad = ["hey","sad_song1","sad_song2"]
sad_song = song(sad)

happy_bday.sing_a_song()
sad_song.sing_a_song()
song.name = "satya"
print(sad_song.name)

print(happy_bday.lyrics)
