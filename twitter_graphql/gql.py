import logging.config
import sys

from .constants import log_config

logging.config.dictConfig(log_config)
logger = logging.getLogger(__name__)


def main() -> int:
    logger.debug(f'run {sys._getframe().f_code.co_name}')
    return 0


if __name__ == '__main__':
    exit(main())
