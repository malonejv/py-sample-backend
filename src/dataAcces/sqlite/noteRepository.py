import datetime
from src.dataAcces.abstracts.noteRepository import NoteRepository
from dataAcces.context import Context
from entites.note import Note

class NoteDA(NoteRepository):

    def Insert(self, note):
        sql = "INSERT INTO notas (id, titulo, descripcion, usuarioId, fecha) VALUES(NULL, ?, ?, ?, ?);"

        try:
            fecha = datetime.date.today().strftime("%d/%m/%y")
            params = (note.Title, note.Description, note.UserId, fecha)
        
            context = Context()

            context.Cursor.execute(sql, params)
            context.db.commit()

            result = context.Cursor.rowcount
        except Exception as ex:
            result = 0
        return result
    
    def Update(self, note):
        sql = "UPDATE notas SET titulo = ?, descripcion = ?, fecha = ? WHERE id = ?;"

        try:
            fecha = datetime.date.today().strftime("%d/%m/%y")
            params = (note.Title, note.Description, fecha, note.Id)
        
            context = Context()

            context.Cursor.execute(sql, params)
            context.db.commit()

            result = context.Cursor.rowcount
        except Exception as ex:
            result = 0
        return result
    
    def Delete(self, note):
        sql = "DELETE FROM notas WHERE id = ?;"

        try:
            params = (note.Id,)
        
            context = Context()

            context.Cursor.execute(sql, params)
            context.db.commit()

            result = context.Cursor.rowcount
        except Exception as ex:
            result = 0
        return result
    
    def GetById(self, id):
        sql = "SELECT n.Id, n.titulo, n.descripcion, n.usuarioId FROM notas n WHERE n.id = ?;"
        
        params = (id,)
    
        context = Context()

        context.Cursor.execute(sql, params)
           
        resultDb = context.Cursor.fetchone()

        return resultDb

    def GetByUser(self, userId):
        sql = "SELECT n.Id, n.titulo, n.descripcion, n.usuarioId FROM notas n WHERE n.usuarioId = ?;"
        
        params = (userId,)
    
        context = Context()

        context.Cursor.execute(sql, params)
           
        resultDb = context.Cursor.fetchall()

        return resultDb
