BLACK = '\x1b[30m'
RED = '\x1b[31m'
GREEN = '\x1b[32m'
YELLOW = '\x1b[33m'
BLUE = '\x1b[34m'
MAGENTA = '\x1b[35m'
CYAN = '\x1b[36m'
WHITE = '\x1b[37m'
BOLD = '\x1b[1m'
RESET = '\x1b[0m'

log_config = {
    "version": 1,
    "formatters": {
        "simple": {
            "format": "%(asctime)s.%(msecs)03d %(levelname)s: %(message)s"
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "simple",
            "stream": "ext://sys.stdout"
        },
        "file": {
            "class": "logging.FileHandler",
            "level": "DEBUG",
            "formatter": "simple",
            "filename": "debug.log",
            "encoding": "utf8",
            "mode": "a"
        }
    },
    "loggers": {
        "myLogger": {
            "level": "DEBUG",
            "handlers": [
                "console"
            ],
            "propagate": "no"
        }
    },
    "root": {
        "level": "DEBUG",
        "handlers": [
            "console",
            "file"
        ]
    }
}
