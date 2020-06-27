import os


class Config:
	SECRET_KEY = '040542c0dbbee13468b69f52f331b2ba'
	SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	MAIL_SERVER = 'smtp.gmail.com'
	MAIL_PORT = 587
	MAIL_USE_TLS = True
	MAIL_USERNAME = os.environ.get('USER')
	MAIL_PASSWORD = os.environ.get('PASSWORD')
	LANGUAGES = ['en', 'es']
	LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')

	