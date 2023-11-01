'''
Unit 2: Challenge 2.2

Implement a class called Player that represents a cricket player. The Player class should have a method called play() which prints "The player is playing cricket. Derive two classes, Batsman and Bowler, from the Player class. Override the play() method in each derived class to print "The batsman is batting" and "The bowler is bowling", respectively. Write a program to create objects of both the Batsman and Bowler classes and call the play() method for each object.
'''
#base class
class Player:
    def play(self):
        print("The player is playing Cricket.")

#derived class Batsman
class Batsman(Player):
    def play(self):
        print("The batsman is batting.")


#derived class Bowler
class Bowler(Player):
    def play(self):
        print("The bowler is bowling.")

#Creating objects
bman=Batsman()
bow=Bowler()
for p in (bman,bow):
    p.play()