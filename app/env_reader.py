import dotenv

dotenv.load_dotenv()


class EnvReader:
    def __init__(self) -> None:
        self.env = dotenv.dotenv_values()

        self.host = self.env.get("HOST", "0.0.0.0")
        self.port = self.env.get("PORT", 8000)
        self.workers = self.env.get("WORKERS", 4)
        self.worker_class = self.env.get(
            "WORKER_CLASS", "uvicorn.workers.UvicornWorker"
        )
        self.timeout = self.env.get("TIMEOUT", 30)
        self.keepalive = self.env.get("KEEPALIVE", 5)


env = EnvReader()
