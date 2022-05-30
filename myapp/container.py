from dependency_injector import containers, providers

from myapp.application.todo_service import TodoService



class Application
    configuration = providers.Configuration()

    todo_entry_repository = providers.Singleton(
        storage_dir=configuration.storage_dir
    )

    todo_service = providers.Factory(
        TodoService,
        todo_entry_repository
    )
