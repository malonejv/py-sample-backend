import sqlite3
from injector import Binder, Module, provider, singleton
from backend.businessLogic.abstract.noteBusinessComponent import NoteBusinessComponent
from backend.businessLogic.abstract.userBusinessComponent import UserBusinessComponent
from backend.businessLogic.noteManager import NoteManager
from backend.businessLogic.userManager import UserManager
from backend.dataAccess.abstracts.noteRepository import NoteRepository as AbstrasctNoteRepository
from backend.dataAccess.abstracts.userRepository import UserRepository as AbstractUserRepository
from backend.dataAccess.sqliteDataAccess.noteRepository import NoteRepository
from backend.dataAccess.sqliteDataAccess.userRepository import UserRepository
from backend.infrastructure.configHelper import ConfigHelper

class BackendModule(Module):
    """Class for configure injector module"""
    
    def configure(self, binder: Binder) -> None:

        binder.bind(NoteBusinessComponent,NoteManager)
        binder.bind(UserBusinessComponent,UserManager)

        binder.bind(AbstrasctNoteRepository,NoteRepository)
        binder.bind(AbstractUserRepository,UserRepository)

        return super().configure(binder)


    @singleton
    @provider
    def provide_sqlite_connection(self, config:ConfigHelper) -> sqlite3.Connection:
      conn = sqlite3.connect(config.connectionString)
      return conn