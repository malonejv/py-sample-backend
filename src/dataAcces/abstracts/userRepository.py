import datetime
import hashlib
from dataAcces.context import Context

from abc import ABC, abstractmethod

class UserRepository(ABC):
    @abstractmethod()
    def Insert(self, user):
        pass
    
    @abstractmethod()
    def GetByEmailPassword(self, email, password):
        pass

