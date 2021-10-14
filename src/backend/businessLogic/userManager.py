from dataclasses import dataclass
import re
from dataAccess.abstracts.userRepository import UserRepository
from businessLogic.abstract.userBusinessComponent import UserBusinessComponent
from businessLogic.validationException import ValidationException
from entities.user import User

@dataclass()
class UserManager(UserBusinessComponent):
    """User bussiness component class"""
    
    _repository:UserRepository

    def SignUp(self, user: User, passwordConfirm: bytes, userRepository:UserRepository):
        self._repository = userRepository
        
        self.__checkValidEmail(user.Email)
        self.__checkPasswordConfirm(user.Password,passwordConfirm)
        
        return self._repository.Insert(user)

    def Login(self, email: str, password: str):
        resultDb = self._repository.GetByEmailPassword(email, password)

        if(resultDb != None):
            return User(resultDb[1],resultDb[2],resultDb[3],id=resultDb[0])
        else:
            return None

    def __checkPasswordConfirm(self, password: bytes, passwordConfirm: bytes):
        """Validates a password with its confimation"""

        if(password != passwordConfirm):
            raise ValidationException("Debe ingresar una contraseña que coincida con el campo de confirmación.", field="Password")

    def __checkValidEmail(self, email: str):
        """Validates an email address"""

        regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
        
        if(not re.search(regex, email)):
            raise ValidationException("Debe ingresar un email válido.", field="Email")
