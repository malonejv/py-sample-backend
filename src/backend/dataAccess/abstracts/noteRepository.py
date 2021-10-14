from abc import ABC, abstractmethod

class NoteRepository(ABC):
    """Note repository class"""

    @abstractmethod()
    def Insert(self, note):
        """Inserts a note in a data context"""
        raise NotImplementedError
    
    @abstractmethod()
    def Update(self, note):
        """Updates a note in a data context"""
        raise NotImplementedError
    
    @abstractmethod()
    def Delete(self, note):
        """Deletes a note from a data context"""
        raise NotImplementedError
    
    @abstractmethod()
    def GetById(self, id):
        """Gets a note from data context by its id"""
        raise NotImplementedError

    @abstractmethod()
    def GetByUser(self, userId):
        """Gets a note from data context by a user id"""
        raise NotImplementedError
