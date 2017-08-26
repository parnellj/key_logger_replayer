try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'name': 'Keylogger and Replayer',
	'version': '0.1',
	'url': 'https://github.com/parnellj/key_logger_replayer',
	'download_url': 'https://github.com/parnellj/key_logger_replayer',
	'author': 'Justin Parnell',
	'author_email': 'parnell.justin@gmail.com',
	'maintainer': 'Justin Parnell',
	'maintainer_email': 'parnell.justin@gmail.com',
	'classifiers': [],
	'license': 'GNU GPL v3.0',
	'description': 'Provides minimal functionality to log and replay a sequence of keys such as in a video game.',
	'long_description': 'Provides minimal functionality to log and replay a sequence of keys such as in a video game.',
	'keywords': '',
	'install_requires': ['nose'],
	'packages': ['key_logger_replayer'],
	'scripts': []
}
	
setup(**config)
