from utils import logger

if __name__ == '__main__': 
    # Testa os logs
    def testDebug():
        logger.debug('Mensagem de debug')

    def testInfo(): 
        logger.info('Mensagem de informação')

    def testWarning():
        logger.warning('Mensagem de aviso')

    def testError():
        logger.error('Mensagem de erro')

    def testCritical():
        logger.critical('Mensagem crítica')

    testDebug()
    testInfo()
    testWarning()
    testError()
    testCritical()