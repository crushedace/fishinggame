#import library
import random


# create die class
class Die():
 # create die faces
 def __init__(self, faces):
    self._faces = faces
 def get_faces(self):
    return self._faces
 # create die roll
 def roll_die(self):
    return random.randint(1,self._faces)