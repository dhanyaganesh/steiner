try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description' : 'My Project',
	'author' : 'My Name',
	'url' : 'URL to get it at.',
	'download_url' : 'Where to download it.',
	'author_email' : 'dhanyaganesh3@gmail.com',
	'version' : '0.1',
	'install_requires' : ['nose'],
	'packages' : ['steiner'],
	'scripts' : [],
	'name' : 'steiner'
}

setup(**config)
