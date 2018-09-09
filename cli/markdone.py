import click
import os.path
import helpers

@click.command()
@click.argument('dir', default='.')
def cli(dir):
	"""Markdone CLI"""
	helpers.get_root(dir)

if __name__ == '__main__':
	# pylint: disable=no-value-for-parameter
	cli()