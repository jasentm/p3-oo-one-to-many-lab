
PET_TYPES = ['dog', 'cat', 'rodent', 'bird', 'reptile', 'exotic']

class Pet:
    PET_TYPES = ['dog', 'cat', 'rodent', 'bird', 'reptile', 'exotic']

    all = []

    def __init__(self, name, pet_type, owner=None):
        self.name = name
        self.pet_type = pet_type
        self._owner = owner
        Pet.add_to_pets(self)

    @property
    def pet_type(self):
        return self._pet_type
    
    @pet_type.setter
    def pet_type(self, pet_type):
        if pet_type in PET_TYPES:
            self._pet_type = pet_type 
        else:
            raise Exception("Pet type must be in approved list of pet types")
        
    @property
    def owner(self):
        return self._owner
    
    @owner.setter
    def owner(self, value):
        if not isinstance (value, Owner):
            raise Exception('Owner must be an instance of Owner class.')
        self._owner = value
        
    @classmethod
    def add_to_pets(cls, pet):
        cls.all.append(pet)
class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]
    
    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("Pet must be instance of Pet class.")
        pet.owner = self

    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda x: x.name)
    

