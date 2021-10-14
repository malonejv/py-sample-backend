
from abc import ABC, abstractmethod
from entities.user import User

class UserBusinessComponent(ABC):
    """User bussiness component abstract class"""
    
    @abstractmethod()
    def SignUp(self, user: User, passwordConfirm: bytes):
        """Registers a new user"""
        raise NotImplementedError
    
    
    @abstractmethod()
    def Login(self, email: str, password: str):
        """Authentics a user"""
        raise NotImplementedError
