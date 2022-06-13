from abc import ABC
from typing import Optional

from myapp.domain.todo import TodoEntry


class ITodoEntryRepository(ABC):
    def get(self, entry_id: str) -> TodoEntry:
        ...

    def add(self, entry: TodoEntry) -> None:
        ...

    def get_all(self, search: Optional[str]) -> list[TodoEntry]:
        ...
