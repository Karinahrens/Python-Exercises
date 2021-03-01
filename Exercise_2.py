# Exercise 2
# Define a class called Songs, it will show the lyrics of a song. Its __init__() method should take
# lyrics. Lyrics is a list. Inside your class create a method called sing_me_a_song that prints
# each element of lyrics on his own line. Test your code with examples.

# creating class songs:
class Songs:
    def __init__(self, lyrics):
        self.lyrics = lyrics
"""creating function that will write each element in a new line """

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

# examples and print
rock_you = Songs(["Buddy, you're a boy, make a big noise,", "Playing in the street, gonna be a big man someday, ", "You got mud on your face, you big disgrace, ", "Kicking your can all over the place, singin"])
print(rock_you.sing_me_a_song())

we_will = Songs(["We will, we will rock you", "We will, we will rock you"])
print(we_will.sing_me_a_song())
