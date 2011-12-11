# Scrapy settings for ec project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'ec'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['ec.spiders']
NEWSPIDER_MODULE = 'ec.spiders'
DEFAULT_ITEM_CLASS = 'ec.items.EcItem'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

