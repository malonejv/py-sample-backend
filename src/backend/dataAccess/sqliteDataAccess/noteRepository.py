import datetime
from dataclasses import dataclass
from sqlite3 import Connection

from dataAccess.abstracts.noteRepository import NoteRepository
from entities.note import Note


@dataclass()
class NoteRepository(NoteRepository):
    """Note repository class"""

    _context:Connection
    
    def Insert(self, note):
        sql = "INSERT INTO notas (id, titulo, descripcion, usuarioId, fecha) VALUES(NULL, ?, ?, ?, ?);"

        try:
            fecha = datetime.date.today().strftime("%d/%m/%y")
            params = (note.Title, note.Description, note.UserId, fecha)
        
            self._context.cursor.execute(sql, params)
            self._context.db.commit()

            result = self._context.cursor.rowcount
        except Exception as ex:
            result = 0
        return result
    
    def Update(self, note):
        sql = "UPDATE notas SET titulo = ?, descripcion = ?, fecha = ? WHERE id = ?;"

        try:
            fecha = datetime.date.today().strftime("%d/%m/%y")
            params = (note.Title, note.Description, fecha, note.Id)
        
            self._context.cursor.execute(sql, params)
            self._context.db.commit()

            result = self._context.cursor.rowcount
        except Exception as ex:
            result = 0
        return result
    
    def Delete(self, note):
        sql = "DELETE FROM notas WHERE id = ?;"

        try:
            params = (note.Id,)
        
            self._context.cursor.execute(sql, params)
            self._context.db.commit()

            result = self._context.cursor.rowcount
        except Exception as ex:
            result = 0
        return result
    
    def GetById(self, id):
        sql = "SELECT n.Id, n.titulo, n.descripcion, n.usuarioId FROM notas n WHERE n.id = ?;"
        
        params = (id,)
    
        self._context.cursor.execute(sql, params)
           
        resultDb = self._context.cursor.fetchone()

        return resultDb

    def GetByUser(self, userId):
        sql = "SELECT n.Id, n.titulo, n.descripcion, n.usuarioId FROM notas n WHERE n.usuarioId = ?;"
        
        params = (userId,)
    
        self._context.cursor.execute(sql, params)
           
        resultDb = self._context.cursor.fetchall()

        return resultDb
