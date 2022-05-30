import pickle
from dataclasses import dataclass
from pathlib import Path

from myapp.domain.todo import TodoEntry
from myapp.domain.todo_entry_repository import ITodoEntryRepository


class TodoEntryNotFound(Exception):
    pass


@dataclass
class TodoEntryPickleRepository(ITodoEntryRepository):
    storage_dir: str

    def get(self, entry_id: str) -> TodoEntry:
        try:
            entry: TodoEntry
            with open(Path(self.storage_dir) / entry_id) as entry_file:
                entry = pickle.load(entry_file)
            return entry
        except Exception:
            raise TodoEntryNotFound()

    def add(self, entry: TodoEntry) -> None:
        with open(Path(self.storage_dir) / entry.id) as entry_file:
            pickle.dump(entry, entry_file)
