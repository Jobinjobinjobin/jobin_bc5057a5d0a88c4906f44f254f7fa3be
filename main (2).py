class Player:

  def play(self):
      print("The player is playing cricket.")

class Batsman (Player):

 def play(self):

   print("The batsmen is hatting.")

class Bowler (Player):

  def play(self):

    print("The bouler is bowling.")
batsman=Batsman()
bowler =Bowler()

batsman.play()

bowler.play()