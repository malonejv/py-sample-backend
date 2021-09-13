import datetime
from dataAcces.context import Context
from entites.note import Note

from abc import ABC, abstractmethod

class NoteRepository(ABC):

    @abstractmethod()
    def Insert(self, note):
        pass
    
    @abstractmethod()
    def Update(self, note):
        pass
    
    @abstractmethod()
    def Delete(self, note):
        pass
    
    @abstractmethod()
    def GetById(self, id):
        pass

    @abstractmethod()
    def GetByUser(self, userId):
        pass
