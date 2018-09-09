import click
import os.path
import helpers
import cmd

@click.command()
@click.argument('dir', default='.')
def cli(dir):
	"""Markdone CLI"""
	root_dir = helpers.get_root(dir)

if __name__ == '__main__':
	# pylint: disable=no-value-for-parameter
	cli()