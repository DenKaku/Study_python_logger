
from tool.logger import logger
from tool.logger import setLogger

import datetime



# def write_log():

#     logging.basicConfig(filename='example.log', level=logging.DEBUG)
#     logging.debug('This message should go to the log file')
#     logging.info('So should this')
#     logging.warning('And this, too')
#     logging.error('And non-ASCII stuff, too, like Øresund and Malmö')


#
def test_output_log():

    logger.debug('debug===== start =====')

    for num in range(30):
        logger.debug('debug:{}'.format(str(num)))

    logger.debug('debug===== end =====')

    logger.info('info===== start =====')

    for num in range(30):
        logger.info('info:{}'.format(str(num)))

    logger.info('info===== end =====')

    # 実行ファイル名を設定したい場合
    # logger = setLogger("study_logger")
    # logger.debug('debug===== start =====')

    # for num in range(30):
    #     logger.debug('debug:{}'.format(str(num)))

    # logger.debug('debug===== end =====')

    # logger.info('info===== start =====')

    # for num in range(30):
    #     logger.info('info:{}'.format(str(num)))

    # logger.info('info===== end =====')



if __name__ == "__main__":
    # write_log()
    test_output_log()
