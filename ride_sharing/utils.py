# Study modules 

import sys 
sys.path.append()
from .config import PER_KM 
# yaa relative import ko issue ayo bhane afai khojera solve garne

class Location:
    LOCATIONS = []

    def add_location(self, name):
        self.LOCATIONS.append(name)
    
    def get_locations(self):
        return self.LOCATIONS
    

class BookARide:
    MIN_RATE = 30 # 2 KM 

    def get_distance(self, from_, to):
        # open csv file, compare from, to
        return 3
        

    def get_total_amount(self, from_, to):
        distance = self.get_distance()
        # MIN_RATE + PER_KM * distance 
        return 100


class Rider:
    pass 

