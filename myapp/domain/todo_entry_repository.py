from abc import ABC

from myapp.domain.todo import TodoEntry


class ITodoEntryRepository(ABC):
    def get(self, entry_id: str) -> TodoEntry:
        ...

    def add(self, entry: TodoEntry) -> None:
        ...
