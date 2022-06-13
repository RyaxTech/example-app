from typing import Any

from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

from myapp.container import ApplicationContainer
from myapp.infrastructure.api import todo_controller


def setup(app: FastAPI, container: ApplicationContainer) -> None:

    # Add other controllers here
    app.include_router(todo_controller.router)

    # Inject dependencies
    container.wire(
        modules=[
            todo_controller,
        ]
    )

    # Customize the openAPI documentation
    def custom_openapi() -> Any:
        if app.openapi_schema:
            return app.openapi_schema
        openapi_schema = get_openapi(
            title="My TODO app",
            # version=__version__,
            version="0.0.1",
            description="My TODO app API'",
            routes=app.routes,
        )
        openapi_schema["info"]["x-logo"] = {
            # TODO: Put your logo here!
            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a3/To_Do.svg/295px-To_Do.svg.png"
        }
        if not container.configuration.api_prefix():
            openapi_schema["servers"] = [{"url": "/"}]
        else:
            openapi_schema["servers"] = [{"url": container.configuration.api_prefix()}]
        app.openapi_schema = openapi_schema
        return app.openapi_schema

    app.openapi = custom_openapi
