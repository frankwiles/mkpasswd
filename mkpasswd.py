import click
import string
import random


def get_chars(symbols):
    all_chars = string.ascii_letters + string.digits

    if symbols:
        all_chars = all_chars + string.punctuation

    all_chars = list(all_chars)
    random.shuffle(all_chars)

    return all_chars


def generate_password(length=16, symbols=False):
    """ Generate a strong password """
    characters = get_chars(symbols)
    parts = []

    for i in range(length):
        parts.append(random.choice(characters))

    return "".join(parts)


@click.command()
@click.option("--symbols", "-s", is_flag=True)
@click.option("--length", "-l", default=16)
@click.option("--quiet", "-q", is_flag=True)
def cli(symbols, length, quiet):
    """ Make strong passwords """
    pw = generate_password(length=length, symbols=symbols)

    if quiet:
        click.secho(pw)
        return

    click.secho(f"--- Generating a strong password of length {length} ---", fg="green")
    click.secho(pw)
    click.secho("---", fg="green")
