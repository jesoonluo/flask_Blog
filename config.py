class Config(object):
	pass


class ProdConfig(Config):
	pass


class DevConfig(Config):
	DEBUG = True
	SQLALCHEMY_ECHO = True
	SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:mysql@localhost:3306/test'
