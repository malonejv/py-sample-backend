
from abc import ABC, abstractmethod


class NoteBusinessComponent(ABC):
    """Note bussiness component abstract class"""

    @abstractmethod()
    def Create(self, note):
        """Defines the treatment of a note creation"""
        raise NotImplementedError
    
    @abstractmethod()
    def Update(self, note):
        """Defines the treatment of a note updating"""
        raise NotImplementedError
    
    @abstractmethod()
    def Delete(self, note):
        """Defines the treatment of a note deletion"""
        raise NotImplementedError
    
    @abstractmethod()
    def GetById(self, id):
        """Gets a note by its id"""
        raise NotImplementedError

    @abstractmethod()
    def GetByUser(self, userId):
        """Gets a note by a user id"""
        raise NotImplementedError
