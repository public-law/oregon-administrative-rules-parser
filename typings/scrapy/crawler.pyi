"""
This type stub file was generated by pyright.
"""

import logging
from twisted.internet import defer
from scrapy import signals
from typing import Any, Optional

logger = logging.getLogger(__name__)
class Crawler(object):
    def __init__(self, spidercls, settings: Optional[Any] = ...):
        self.spidercls = ...
        self.settings = ...
        self.signals = ...
        self.stats = ...
        self.logformatter = ...
        self.extensions = ...
        self.crawling = ...
        self.spider = ...
        self.engine = ...
    
    @property
    def spiders(self):
        ...
    
    @defer.inlineCallbacks
    def crawl(self, *args, **kwargs):
        self.crawling = ...
    
    def _create_spider(self, *args, **kwargs):
        ...
    
    def _create_engine(self):
        ...
    
    @defer.inlineCallbacks
    def stop(self):
        """Starts a graceful stop of the crawler and returns a deferred that is
        fired when the crawler is stopped."""
        ...
    


class CrawlerRunner(object):
    """
    This is a convenient helper class that keeps track of, manages and runs
    crawlers inside an already setup Twisted `reactor`_.

    The CrawlerRunner object must be instantiated with a
    :class:`~scrapy.settings.Settings` object.

    This class shouldn't be needed (since Scrapy is responsible of using it
    accordingly) unless writing scripts that manually handle the crawling
    process. See :ref:`run-from-script` for an example.
    """
    crawlers = ...
    def __init__(self, settings: Optional[Any] = ...):
        self.settings = ...
        self.spider_loader = ...
        self.bootstrap_failed = ...
    
    @property
    def spiders(self):
        ...
    
    def crawl(self, crawler_or_spidercls, *args, **kwargs):
        """
        Run a crawler with the provided arguments.

        It will call the given Crawler's :meth:`~Crawler.crawl` method, while
        keeping track of it so it can be stopped later.

        If ``crawler_or_spidercls`` isn't a :class:`~scrapy.crawler.Crawler`
        instance, this method will try to create one using this parameter as
        the spider class given to it.

        Returns a deferred that is fired when the crawling is finished.

        :param crawler_or_spidercls: already created crawler, or a spider class
            or spider's name inside the project to create it
        :type crawler_or_spidercls: :class:`~scrapy.crawler.Crawler` instance,
            :class:`~scrapy.spiders.Spider` subclass or string

        :param list args: arguments to initialize the spider

        :param dict kwargs: keyword arguments to initialize the spider
        """
        ...
    
    def _crawl(self, crawler, *args, **kwargs):
        ...
    
    def create_crawler(self, crawler_or_spidercls):
        """
        Return a :class:`~scrapy.crawler.Crawler` object.

        * If ``crawler_or_spidercls`` is a Crawler, it is returned as-is.
        * If ``crawler_or_spidercls`` is a Spider subclass, a new Crawler
          is constructed for it.
        * If ``crawler_or_spidercls`` is a string, this function finds
          a spider with this name in a Scrapy project (using spider loader),
          then creates a Crawler instance for it.
        """
        ...
    
    def _create_crawler(self, spidercls):
        ...
    
    def stop(self):
        """
        Stops simultaneously all the crawling jobs taking place.

        Returns a deferred that is fired when they all have ended.
        """
        ...
    
    @defer.inlineCallbacks
    def join(self):
        """
        join()

        Returns a deferred that is fired when all managed :attr:`crawlers` have
        completed their executions.
        """
        ...
    


class CrawlerProcess(CrawlerRunner):
    """
    A class to run multiple scrapy crawlers in a process simultaneously.

    This class extends :class:`~scrapy.crawler.CrawlerRunner` by adding support
    for starting a Twisted `reactor`_ and handling shutdown signals, like the
    keyboard interrupt command Ctrl-C. It also configures top-level logging.

    This utility should be a better fit than
    :class:`~scrapy.crawler.CrawlerRunner` if you aren't running another
    Twisted `reactor`_ within your application.

    The CrawlerProcess object must be instantiated with a
    :class:`~scrapy.settings.Settings` object.

    :param install_root_handler: whether to install root logging handler
        (default: True)

    This class shouldn't be needed (since Scrapy is responsible of using it
    accordingly) unless writing scripts that manually handle the crawling
    process. See :ref:`run-from-script` for an example.
    """
    def __init__(self, settings: Optional[Any] = ..., install_root_handler: bool = ...):
        ...
    
    def _signal_shutdown(self, signum, _):
        ...
    
    def _signal_kill(self, signum, _):
        ...
    
    def start(self, stop_after_crawl: bool = ...):
        """
        This method starts a Twisted `reactor`_, adjusts its pool size to
        :setting:`REACTOR_THREADPOOL_MAXSIZE`, and installs a DNS cache based
        on :setting:`DNSCACHE_ENABLED` and :setting:`DNSCACHE_SIZE`.

        If ``stop_after_crawl`` is True, the reactor will be stopped after all
        crawlers have finished, using :meth:`join`.

        :param boolean stop_after_crawl: stop or not the reactor when all
            crawlers have finished
        """
        ...
    
    def _get_dns_resolver(self):
        ...
    
    def _graceful_stop_reactor(self):
        ...
    
    def _stop_reactor(self, _: Optional[Any] = ...):
        ...
    


def _get_spider_loader(settings):
    """ Get SpiderLoader instance from settings """
    ...

