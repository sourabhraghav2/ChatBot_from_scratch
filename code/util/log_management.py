import logging



# class LogWrapper:
#     @staticmethod
#     def get_logger():
#         return Logger.get_logger('chat_bot.log')


class LogWrapper:
    @staticmethod
    def get_logger( log_file_name='chat_bot.log'):

        directory_path='../../log/'
        logging_format="%(asctime)s  %(levelname)s - %(message)s"
        log_file_path=directory_path+log_file_name
        logger = logging.getLogger('Chat_bot')
        logger.setLevel(logging.DEBUG)
        if not logger.handlers:
            # create console handler and set level to info
            handler = logging.StreamHandler()
            handler.setLevel(logging.DEBUG)
            formatter = logging.Formatter(logging_format)
            handler.setFormatter(formatter)
            logger.addHandler(handler)

            # create error file handler and set level to error
            handler = logging.FileHandler(log_file_path, "a", encoding=None, delay="true")
            handler.setLevel(logging.DEBUG)
            formatter = logging.Formatter(logging_format)
            handler.setFormatter(formatter)
            logger.addHandler(handler)

            # create debug file handler and set level to debug
            handler = logging.FileHandler(directory_path + 'error.log', "a")
            handler.setLevel(logging.ERROR)
            formatter = logging.Formatter(logging_format)
            handler.setFormatter(formatter)
            logger.addHandler(handler)

        return logger







# log= LogWrapper.get_logger('chat_bot.log')
# log.error('We have a problem')
# log.info('While this is just chatty')
# log.debug('While this is just chatty')