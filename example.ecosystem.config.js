module.exports = {
    apps: [
        {
            name: "proxy-checking-api",
            script: "./main.py",
            interpreter: "./.venv/bin/python",
            interpreter_args: [],
            instances: 1,
            autorestart: true,
            watch: false,
            max_memory_restart: "2G",
            env: {
                NODE_ENV: "production",
            },
        },
    ],
};

