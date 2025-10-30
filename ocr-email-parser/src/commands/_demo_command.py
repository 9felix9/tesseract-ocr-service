"""Click demo command."""
import click


@click.command()
@click.argument("demo")
def demo_command(demo: str):
    """Click demo command"""
    print(demo)
