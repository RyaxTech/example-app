from dependency_injector import providers, containers

from myapp.application.todo_service import TodoService
from myapp.infrastructure.database.todo_entry_repository import (
    TodoEntryPickleRepository,
)


class ApplicationContainer(containers.DeclarativeContainer):
    configuration = providers.Configuration()

    todo_entry_repository = providers.Singleton(
        TodoEntryPickleRepository, storage_dir=configuration.storage_dir
    )

    todo_service = providers.Factory(TodoService, todo_entry_repository)
