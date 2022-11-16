import random
class Hat:
    def __init__(self):
        self.houses=["Gryffindor","Slytherin","RavenClaw","HufflePuff"]

    def sort(self,name):
        print(f"{name} is in {random.choice(self.houses)}")



hat=Hat()
hat.sort("harry")

#using class method

import random
class Hat:
    houses=["Gryffindor","Slytherin","RavenClaw","HufflePuff"]
    @classmethod
    def sort(cls,name):
        print(f"{name} is in {random.choice(cls.houses)}")



Hat.sort("Harry")