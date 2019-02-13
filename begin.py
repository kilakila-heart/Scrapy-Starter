#--*coding:utf-8
from scrapy import cmdline
import logging




logger = logging.getLogger()
logger.setLevel(logging.INFO)  # Log等级总开关



logging.info("开始执行爬虫")
cmdline.execute("scrapy crawl metro".split())