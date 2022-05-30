from dependency_injector.wiring import Provide

from myapp.container import ApplicationContainer
from myapp.domain.todo import TodoEntry
from myapp.domain.todo_entry_repository import ITodoEntryRepository


class TodoService:
    todo_repository: ITodoEntryRepository = Provide[ApplicationContainer.todo_service]

    def add_entry(self, content: str) -> str:
        entry = TodoEntry.create_from_content(content)
        self.todo_repository.add(entry)
        return entry.id

    def add_tag(self, entry_id: str, tag: str) -> None:
        entry = self.todo_repository.get(entry_id)
        entry.set_tag(tag)
