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