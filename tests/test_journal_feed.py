from journal_feed import __version__
from journal_feed.src.pyppeteers import main

def test_version():
    assert __version__ == '0.1.0'

def test_pyppeteer_main():
    main('https://www.ajronline.org')