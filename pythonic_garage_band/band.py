
from abc import ABC,abstractmethod,abstractclassmethod, abstractstaticmethod
#Bands Class 
from typing import AbstractSet







# Abstract base or super class 
class Musician(ABC):

   

    def __init__(self, name):

        self.name = name
        #self.__class__.members.append(self) #it will return all the inheritances classes as the value returning fron str
       # abstract methods to define what this method should do and it will implemented in the inheritant instances not in the class and Abstract classes are not intended to be instantiated meaning we can't make instances from it
       # in case we do implementation meaning returning values it will be overidden
       # in case we didn't added to the inherited class and we call it on that class it won't work 
        @abstractmethod        
        def __str__():
                pass
        @abstractmethod    
        def __repr__():
                pass
        @abstractstaticmethod    
        def get_instrument():
                pass
        @abstractstaticmethod    
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
    
    @staticmethod
    def play_solo():
        return ("face melting guitar solo")
    @staticmethod
    def get_instrument():
        return ('guitar')
    

class Bassist(Musician):
    instrument = 'bass'
     
   
      # instance method
    def __str__(self):
        return (f"My name is {self.name} and I play {self.__class__.instrument}")
    
    def __repr__(self):
        return (f'Bassist instance. Name = {self.name}')
    
    #static methods
    @staticmethod
    def get_instrument():
        return ('bass')
    @staticmethod
    def play_solo():
        return ("bom bom buh bom")




class Drummer(Musician):
    instrument = 'drums'
   
       
      # instance method
    def __str__(self):
        return (f"My name is {self.name} and I play {self.__class__.instrument}")

    def __repr__(self):
        return (f'Drummer instance. Name = {self.name}')

    # static methods
    @staticmethod
    def play_solo():
        return ("rattle boom crash")
    @staticmethod
    def get_instrument():
        return ('drums')


class Band(Musician):
    instances =[] 
#accesing this attrib is done using the __class__ before it inside dunder init or using cls inside the class method

    def __init__(self, name='',members =[]):
        self.name = name
        self.members = members
        #__class__. to access the variables
        self.__class__.instances.append(self) #it will add the represent value of all the objects or instances 


    #instance method
    def play_solos(self):
        ordered_solos=[]
        for ele in self.members:
            result = ele.play_solo()
            ordered_solos.append(result)
        return ordered_solos



    @classmethod
    #as to check how many instances has been created by this class we made it as class method to run using the class but #it can be accessed using instances or class or to empty them using both instance and class
    # how to make it count the instances by placing them inside the dunder and append the self for represent or the self.name if wanted to printed 
     
    def to_list(cls):
        return cls.instances

    
    def __str__(self):
        
        return (f"Our Band name is {self.name}")

    def __repr__(self):

        return (f"Band instance. Name = {self.name}")



if __name__ == '__main__'  :
    dodo = Musician('music')
    nono = Band('ha')
    
    print('haya')
    donti = Drummer('joe')
    #print(str(donti))
    pont = Band( 'yahia',[Drummer('had'),Guitarist('mad')])
    print(pont)
    pont.instances = []
    print(pont.instances)
    #print(Band.instances)