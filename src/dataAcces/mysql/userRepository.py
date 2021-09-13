import datetime
import hashlib
from dataAcces.abstracts.userRepository import UserRepository
from dataAcces.context import Context

class UserDA(UserRepository):

    def Insert(self, user):
        sql = "INSERT INTO usuarios VALUES(NULL, %s, %s, %s, %s, %s);"

        try:
            #Cifrar contraseña
            hashedPass = hashlib.sha256()
            hashedPass.update(user.Password)

            fecha = datetime.date.today()
            params = (user.Name, user.LastName, user.Email, hashedPass.hexdigest(), fecha)
        
            context = Context()

            context.Cursor.execute(sql, params)
            context.db.commit()

            result = context.Cursor.rowcount
        except Exception as ex:
            result = 0
        return result
    
    def GetByEmailPassword(self, email, password):
        sql = "SELECT id, nombres, apellidos, email FROM usuarios WHERE email = %s AND password = %s;"

        try:
            #Cifrar contraseña
            hashedPass = hashlib.sha256()
            hashedPass.update(password)

            params = (email, hashedPass.hexdigest())
        
            context = Context()

            context.Cursor.execute(sql, params)
            
            resultDb = context.Cursor.fetchone()
        except Exception as ex:
            resultDb = None
        return resultDb
