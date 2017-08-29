#project/config.py

class BaseConfig:
	"""Base Configuration"""
	DEBUG = False
	TESTING = False

class DevelopmentConfig(BaseConfig):
	"""Development Config"""
	DEBUG = True

class TestConfig(BaseConfig):
	"""Test Config"""
	DEBUG = True
	TESTING = True

class ProductionConfig(BaseConfig):
	"""Production Config"""
	DEBUG = False

