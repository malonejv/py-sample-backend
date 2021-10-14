from dataclasses import dataclass
from backend.businessLogic.abstract.noteBusinessComponent import NoteBusinessComponent
from dataAccess.abstracts.noteRepository import NoteRepository
from entities.note import Note

@dataclass()
class NoteManager(NoteBusinessComponent):
    """Note bussiness component class"""

    _repository:NoteRepository

    def Create(self, note):
        return self._repository.Insert(note)
    
    def Update(self, note):
        return self._repository.Update(note)
    
    def Delete(self, note):
        return self._repository.Delete(note)
    
    def GetById(self, id):
        record = self._repository.GetById(id)

        if(record != None):
            nota = Note(record[0],record[1],record[2],record[3])

        return nota

    def GetByUser(self, userId):
        resultDb = self._repository.GetByUser(userId)

        notas = []
        if(resultDb != None):
            for record in resultDb:
                nota = Note(record[0],record[1],record[2],record[3])
                notas.append(nota)

        return notas
