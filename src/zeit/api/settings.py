# -*- coding: utf-8 -*-
"""
    zeit.api.settings
    ~~~~~~~~~~~~~~~~~

    This module contains config classes for different build scenarios.

    Copyright: (c) 2013 by ZEIT ONLINE.
    License: BSD, see LICENSE.md for more details.
"""

import urllib2
import warnings


class Config:

    ACCESS_TIMEFRAME = 86400
    ACCESS_TIERS = dict(free=10000, pro=50000, max=100000)

    DATABASE = '/var/lib/zon-api/data.db'
    SCHEMA = '/schemas/database.sql'

    TESTING = False

    try:
        import private
        DEPARTMENT_ALPHABET = private.DEPARTMENT_ALPHABET
        KEYWORD_ALPHABET = private.KEYWORD_ALPHABET
        PRODUCT_ALPHABET = private.PRODUCT_ALPHABET
        SERIES_ALPHABET = private.SERIES_ALPHABET
    except:
        warnings.warn('No alphabet URLs are configured.')
        DEPARTMENT_ALPHABET = ''
        KEYWORD_ALPHABET = ''
        PRODUCT_ALPHABET = ''
        SERIES_ALPHABET = ''


class ProductionConfig(Config):

    DOC_URL = 'http://developer.zeit.de'
    API_URL = 'http://api.zeit.de'
    SOLR_URL = 'http://127.0.0.1:8983/solr'

    try:
        urllib2.urlopen(SOLR_URL, timeout=3)
    except:
        warnings.warn('Local Solr server seems to be unreachable.')

    try:
        import private
        RECAPTCHA_PRIVATE_KEY = private.RECAPTCHA_PRIVATE_PROD
        RECAPTCHA_PUBLIC_KEY = private.RECAPTCHA_PUBLIC_PROD
    except:
        warnings.warn('No production Recaptcha API keys found.')


class DevelopmentConfig(Config):

    DOC_URL = 'http://dev-test.zeit.de:8080'
    API_URL = 'http://api-test.zeit.de:8080'
    SOLR_URL = 'http://127.0.0.1:8983/solr'

    try:
        urllib2.urlopen(SOLR_URL, timeout=3)
    except:
        warnings.warn('Local Solr server seems to be unreachable.')

    try:
        import private
        RECAPTCHA_PRIVATE_KEY = private.RECAPTCHA_PRIVATE_DEVEL
        RECAPTCHA_PUBLIC_KEY = private.RECAPTCHA_PUBLIC_DEVEL
    except:
        warnings.warn('No development Recaptcha API keys found.')


class LocalConfig(DevelopmentConfig):

    API_PORT = 5000
    DOC_PORT = 5001
    SERVERNAME = '127.0.0.1'
    API_URL = 'http://%s:%d' % (SERVERNAME, API_PORT)
    DOC_URL = 'http://%s:%d' % (SERVERNAME, DOC_PORT)


class TestingConfig(LocalConfig):

    TESTING = True