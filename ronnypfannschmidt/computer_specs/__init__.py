from ._util import ensure

from . import pre_commit
from . import container_tools
from . import devpi


def main():
    ensure(
        pre_commit,
        container_tools,
        devpi,
    )
