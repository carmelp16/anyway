import os
import sys
from .new_news_check import is_new_flash_news
# from .news_flash_crawl import ynet_news_flash_crawl
from ..mda_twitter.mda_twitter import mda_twitter
from .beautiful_soup_news_flash_parse import beautiful_soup_news_flash_parse
# from sys import exit
# import time


def scrap_flash_news(site_name, maps_key):
    """
    init scraping for a site
    :param site_name: name of the site to scrap
    :param maps_key: google maps key path
    """
    if site_name == 'ynet':
        rss_link = 'https://www.ynet.co.il/Integration/StoryRss1854.xml'
        if is_new_flash_news(rss_link, site_name):
            # ynet_news_flash_crawl(rss_link, maps_key)
            beautiful_soup_news_flash_parse(rss_link, site_name, maps_key)
    if site_name == 'walla':
        rss_link = 'https://news.walla.co.il/breaking'
        if is_new_flash_news(rss_link, site_name):
            beautiful_soup_news_flash_parse(rss_link, site_name, maps_key)
    if site_name == 'twitter':
        mda_twitter()


def main(google_maps_key):
    """
    main function for beginning of the news flash process
    :param google_maps_key_path: path to google maps key
    """
    sys.path.append(os.path.dirname(os.path.realpath(__file__)))
    scrap_flash_news('ynet', google_maps_key)
    scrap_flash_news('walla', google_maps_key)
    scrap_flash_news('twitter', google_maps_key)
