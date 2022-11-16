#operator overloading

class Vault:
    def __init__(self,galleons=0,sickels=0,knuts=0):
        self.galleons=galleons
        self.sickels=sickels
        self.knuts=knuts

    def __str__(self):
        return f"{self.galleons} Galleons,{self.sickels} Sickels,{self.knuts} Knuts"

    def __add__(self, other):
        galleons=self.galleons+other.galleons
        sickels=self.sickels+other.sickels
        knuts=self.knuts+other.knuts
        return Vault(galleons,sickels,knuts)

potter=Vault(50,100,20)
print(potter)

weasely=Vault(20,25,100)
print(weasely)

#before adding add to class:

# galleons=potter.galleons+weasely.galleons
# sickels=potter.sickels+weasely.sickels
# knuts=potter.knuts+weasely.knuts
# total=Vault(galleons,sickels,knuts)

total =potter+weasely
print(total)
