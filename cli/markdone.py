import click
import os.path
import helpers

@click.command()
@click.argument('dir', default='.')
def cli(dir):
	"""Markdone CLI"""
	helpers.getRoot(dir)

if __name__ == '__main__':
	cli()