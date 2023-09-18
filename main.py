"""
Main cli or app entry point
"""

from src.further_clean_save_json import add
import click

# var=1;var=2


@click.command("add")
@click.argument("a", type=int)
@click.argument("b", type=int)
def add_cli(a, b):
    click.echo(add(a, b))


if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter
    add_cli()