from . import *

async def retrieve_xml(url):
    browser = await launch()
    page = await browser.newPage()
    await page.goto(url)
    await page.screenshot(path='test.png')

def main():
    asyncio.get_event_loop().run_until_complete(retrieve_xml('https://www.google.com'))