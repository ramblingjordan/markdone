import os.path as path
import click

def get_root(dir):

	# If given directory contains .markdone file return it
	if (path.exists(path.abspath(path.join(dir, '.markdone')))):
		return dir
	# If given directory is root return false since no .markdown
	elif (path.abspath(dir) == path.abspath('/')):
		return False
	# Recursively climb the filesystem to root
	return get_root(path.abspath(path.join(dir, path.pardir)))