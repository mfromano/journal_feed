from . import *

async def retrieve_xml(url: str):
    browser = await launch()
    page = await browser.newPage()
    await page.goto(url)
    content = await page.querySelector('.tocContainer')
    text = await page.evaluate('(content) => content.textContent', content, force_expr=True)
    return text

def main(url: str):
    content = asyncio.get_event_loop().run_until_complete(retrieve_xml(url))
    print(content)