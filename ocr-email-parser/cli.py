"""
Entrypoint for click implemented, application-specific cli commands.

This module automatically loads all commands in the ./**/commands directory.

run as: python cli.py <command>
"""

import click
from click import Command
from pathlib import Path
import importlib
from itertools import chain

p = Path(".")


def load_commands():
    buf = []
    for path in chain(  # insert search paths here
        p.glob("src/**/commands/*.py")
    ):
        module = importlib.import_module(f"{'.'.join(path.parts[:-1])}.{path.stem}")
        buf.extend(
            [
                getattr(module, n)
                for n in dir(module)
                if not n.startswith("__") and isinstance(getattr(module, n), Command)
            ]
        )
    return buf


@click.group()
def cli():
    pass


def main():
    commands = load_commands()
    for command in commands:
        cli.add_command(command)
    cli()


if __name__ == "__main__":
    main()