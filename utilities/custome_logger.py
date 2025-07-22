import logging


class Log_Maker:
    @staticmethod
    def log_gen():
        logging.basicConfig(filename=".\\logs\\movies.log",
                            format='%(asctime)s - %(levelname)s - %(name)s - %(filename)s:%(lineno)d - %(message)s',
                            datefmt='%Y-%m-%d %H:%M:%S', force=True)
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        # logger.setLevel(logging.ERROR)
        return logger
