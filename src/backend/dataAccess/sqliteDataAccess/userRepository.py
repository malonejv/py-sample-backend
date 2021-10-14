from dataclasses import dataclass
import datetime
import hashlib
from dataAccess.abstracts.userRepository import UserRepository

@dataclass()
class UserRepository(UserRepository):
    """User repository class"""

    def Insert(self, user):
        sql = "INSERT INTO usuarios VALUES(NULL, ?, ?, ?, ?, ?);"

        try:
            #Cifrar contraseña
            hashedPass = hashlib.sha256()
            hashedPass.update(user.Password)

            fecha = datetime.date.today()
            params = (user.Name, user.LastName, user.Email, hashedPass.hexdigest(), fecha)
        
            self._context.cursor.execute(sql, params)
            self._context.db.commit()

            result = self._context.cursor.rowcount
        except Exception as ex:
            result = 0
        return result
    
    def GetByEmailPassword(self, email, password):
        sql = "SELECT id, nombres, apellidos, email FROM usuarios WHERE email = ? AND password = ?;"

        try:
            #Cifrar contraseña
            hashedPass = hashlib.sha256()
            hashedPass.update(password)

            params = (email, hashedPass.hexdigest())
        
            self._context.cursor.execute(sql, params)
            
            resultDb = self._context.cursor.fetchone()
        except Exception as ex:
            resultDb = None
        return resultDb
