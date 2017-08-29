#project/config.py
import os
class BaseConfig:
	"""Base Configuration"""
	DEBUG = False
	TESTING = False
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	SECRET_KEY = 'my_precious'

class DevelopmentConfig(BaseConfig):
	"""Development Config"""
	DEBUG = True
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

class TestConfig(BaseConfig):
	"""Test Config"""
	DEBUG = True
	TESTING = True
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

class ProductionConfig(BaseConfig):
	"""Production Config"""
	DEBUG = False
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

