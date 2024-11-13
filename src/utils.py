import logging
import os
from dotenv import load_dotenv

load_dotenv()
ENV = os.getenv('ENV')

def init_logger():
	# Configura o logger principal
	logger = logging.getLogger('teste')
	logger.setLevel(logging.DEBUG)

	# Configura o manipulador para console
	console_handler = logging.StreamHandler()
	console_handler.setLevel(logging.DEBUG)

	# Configura o manipulador para arquivo
	# file_handler = logging.FileHandler('app.log')
	# file_handler.setLevel(logging.ERROR)

	pattern = '%(asctime)s [%(levelname)s] - %(filename)s:%(lineno)d %(funcName)s() - %(message)s'
	formatter = logging.Formatter(pattern, datefmt='%H:%M:%S')
	if ENV == 'development':
			from colored_formater import ColoredFormatter
			formatter = ColoredFormatter(pattern, datefmt='%H:%M:%S')

	console_handler.setFormatter(formatter)
	# file_handler.setFormatter(formatter)

	# Adiciona os manipuladores ao logger
	logger.addHandler(console_handler)
	# logger.addHandler(file_handler)
	return logger


logger = init_logger()