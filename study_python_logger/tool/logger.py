import logging
import logging.handlers
import os

from logging import getLogger, StreamHandler, DEBUG, INFO, WARNING, ERROR, Formatter, FileHandler, basicConfig

from os.path import splitext, basename
from time import sleep

base, ext = splitext( basename(__file__) )
print(base)

#pattern 1
#時間指定の基本書き方
basicConfig(
    level=INFO,
    format='%(asctime)s - %(name)s - %(levelname)-8s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[logging.handlers.TimedRotatingFileHandler(('./logs/%s.log' % base), when = 'D')],
)
logger = getLogger(__name__)

#for test
while True:
  logger.info("hoge")
  sleep(1)

#pattern 2----------------------
# logger = getLogger(__name__)
# handler = StreamHandler()

# # logger.setLevel(DEBUG)
# # handler.setLevel(DEBUG)
# logger.setLevel(INFO)
# handler.setLevel(INFO)
# #ファイルのサイズでローテーションできないらしい。。。
# formatter = Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

#pattern 3-------------------------------------------
# # ローテーティングファイルハンドラを作成 フォーマットが上記のフォーマットに適応しないので、手動で各箇所ログを出力する時フォーマットする必要がある
# rh = logging.handlers.RotatingFileHandler(
#             'rotatingfilehandlerlog.log', # ファイル名が指定 txtでもok
#             encoding='utf-8',
#             maxBytes=100, #ファイルサイズでローテーション
#             backupCount=3
#     )
# handler.setFormatter(formatter)

# logger.addHandler(handler)
# logger.addHandler(rh)

# fh = FileHandler(filename='filehandler.log') # ファイル名が指定 txtでもok
# fh.setLevel(INFO)
# fh.setLevel(INFO)
# fh.setFormatter(formatter)
# logger.addHandler(fh)


#pattern 4---------------------------------------
# # ログの出力のモジュールがファイルに出力したい場合
# def setLogger (name):
#     logger = getLogger(name)
#     handler = StreamHandler()

#     # logger.setLevel(DEBUG)
#     # handler.setLevel(DEBUG)
#     logger.setLevel(INFO)
#     handler.setLevel(INFO)

#     #ファイルのサイズでローテーションできないらしい。。。
#     formatter = Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

#     # ローテーティングファイルハンドラを作成 フォーマットが上記のフォーマットに適応しないので、手動で各箇所ログを出力する時フォーマットする必要がある
#     rh = logging.handlers.RotatingFileHandler(
#                 'rotatingfilehandlerlog.log', # ファイル名が指定 txtでもok
#                 encoding='utf-8',
#                 maxBytes=100, #ファイルサイズでローテーション
#                 backupCount=3
#         )
#     handler.setFormatter(formatter)

#     logger.addHandler(handler)
#     logger.addHandler(rh)

#     fh = FileHandler(filename='filehandler.log') # ファイル名が指定 txtでもok
#     fh.setLevel(INFO)
#     fh.setFormatter(formatter)
#     logger.addHandler(fh)
#     return logger
