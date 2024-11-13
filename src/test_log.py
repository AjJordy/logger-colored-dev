import logging
import colorama 

colorama.init()

# Define uma classe personalizada para aplicar cores ao formatter
class ColoredFormatter(logging.Formatter):
    # Define as cores para cada nível de log
    COLORS = {
        logging.DEBUG: colorama.Fore.BLUE,
        logging.INFO: colorama.Fore.GREEN,
        logging.WARNING: colorama.Fore.YELLOW,
        logging.ERROR: colorama.Fore.RED,
        logging.CRITICAL: colorama.Fore.MAGENTA
    }
    
    def format(self, record):
        # Aplica a cor de acordo com o nível do log
        color = self.COLORS.get(record.levelno, colorama.Fore.WHITE)
        message = super().format(record)
        return f"{color}{message}{colorama.Style.RESET_ALL}"


# Configura o logger principal
logger = logging.getLogger('eonix')
logger.setLevel(logging.DEBUG)

# Configura o manipulador para console
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

# Configura o manipulador para arquivo
# file_handler = logging.FileHandler('app.log')
# file_handler.setLevel(logging.ERROR)

# Define o formatador
formatter = ColoredFormatter(
    '%(asctime)s [%(levelname)s] - %(filename)s:%(lineno)d %(funcName)s() - %(message)s',  
    datefmt='%H:%M:%S'
)
console_handler.setFormatter(formatter)
# file_handler.setFormatter(formatter)

# Adiciona os manipuladores ao logger
logger.addHandler(console_handler)
# logger.addHandler(file_handler)

# Testa os logs
def testeDebug():
    logger.debug('Mensagem de debug')


def testeInfo(): 
    logger.info('Mensagem de informação')

logger.warning('Mensagem de aviso')
logger.error('Mensagem de erro')
logger.critical('Mensagem crítica')

testeDebug()
testeInfo()