from fastapi import FastAPI
from gunicorn.app.base import BaseApplication  # type: ignore

from app.env_reader import env


class StandaloneApplication(BaseApplication):  # type: ignore
    def __init__(self, app: FastAPI, options: dict[str, str] | None = None) -> None:
        self.options = options or {}
        self.application = app
        super().__init__()  # type: ignore

    def load_config(self) -> None:
        for key, value in self.options.items():
            if key in self.cfg.settings and value is not None:  # type: ignore
                self.cfg.set(key.lower(), value)  # type: ignore

    def load(self) -> FastAPI:
        return self.application


app = FastAPI(title="Proxy Checking API")


@app.get("/")
async def root() -> dict[str, str]:
    return {"message": "API for checking proxy status"}


if __name__ == "__main__":
    options = {
        "bind": f"{env.host}:{env.port}",
        "workers": env.workers,
        "worker_class": env.worker_class,
        "timeout": env.timeout,
        "keepalive": env.keepalive,
    }
    StandaloneApplication(app, options).run()  # type: ignore
