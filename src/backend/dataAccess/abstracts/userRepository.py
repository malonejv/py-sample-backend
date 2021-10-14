from abc import ABC, abstractmethod

class UserRepository(ABC):
    """User reporitory class"""

    @abstractmethod()
    def Insert(self, user):
        """Inserts a user in a data context"""

        raise NotImplementedError
    
    @abstractmethod()
    def GetByEmailPassword(self, email, password):
        """Gets a user from data context by his email and password"""
        
        raise NotImplementedError

