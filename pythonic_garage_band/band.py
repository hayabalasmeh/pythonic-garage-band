
from abc import ABC,abstractmethod,abstractclassmethod, abstractstaticmethod
#Bands Class 
from typing import AbstractSet







# Abstract base or super class 
class Musician(ABC):
    def __init__(self, name):
        self.name = name

  
        @abstractmethod        
        def __str__():
                pass
        @abstractmethod    
        def __repr__():
                pass
        @abstractmethod    
        def get_instrument():
                pass
        @abstractmethod    
        def play_solo():
                pass
  

    


# Sub classes
class Guitarist(Musician):
    instrument = 'guitar'
    
    
    # instance method
    def __str__(self):
        return (f"My name is {self.name} and I play {self.__class__.instrument}")

    def __repr__(self):
        return (f'Guitarist instance. Name = {self.name}')
    
    def play_solo(self):
        return ("face melting guitar solo")

    def get_instrument(self):
        return ('guitar')
    

class Bassist(Musician):
    instrument = 'bass'
   
     
   
      # instance method
    def __str__(self):
        return (f"My name is {self.name} and I play {self.__class__.instrument}")
    
    def __repr__(self):
        return (f'Bassist instance. Name = {self.name}')
    
    #static methods
    def get_instrument(self):
        return ('bass')
    
    def play_solo(self):
        return ("bom bom buh bom")

class Drummer(Musician):
    instrument = 'drums'
   
       
      # instance method
    def __str__(self):
        return (f"My name is {self.name} and I play {self.__class__.instrument}")

    def __repr__(self):
        return (f'Drummer instance. Name = {self.name}')

    # static methods
    def play_solo(self):
        return ("rattle boom crash")

    def get_instrument(self):
        return ('drums')


class Band(Musician):
    #all_members =[]

    def __init__(self, name='no one',all_members=[]):
        self.name = name
        self.all_members = all_members
        #__class__. to access the variables
        #self.__class__.all_members.append(self)

# intance methods
    def __repr__(self):
        return f'{self.name}'
if __name__ == '__main__'  :
    dodo = Band('haya')
    nono = Band('ha')
    print(dodo.all_members)
    print('haya')
    donti = Drummer('joe')
    print(str(donti))