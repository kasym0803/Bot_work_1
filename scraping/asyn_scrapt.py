import httpx
from parsel import Selector
import asyncio


class Async_Scraper:
    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/119.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-GB,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive'
    }

    # class ="newsHeader_list newsShortList newsShortList-byDate outer-mobile inner-mobile swipe grid "] /a/ @ href

    URL = 'https://www.kinoafisha.info/news/triller-devida-finchera-final-korony-i-vozvraschenie-fargo-10-glavnyh-premer-v-kinoteatrah-i-na-strimingah/'
    LINK_XPATH = '//div[@class="newsHeader_list newsShortList newsShortList-byDate outer-mobile inner-mobile swipe grid"]//a/@href'
    PLUS_URL = 'https://www.kinoafisha.info/'

    async def async_gererator(self, limit):
        for page in range(1, limit + 1):
            yield page

    async def async_scrapers(self):
        urls = []
        async with httpx.AsyncClient(headers=self.HEADERS) as client:
            async for page in self.async_gererator(limit=3):
                url = await self.get_url(client=client, url=self.URL)
                urls.append(url)
        return urls

    async def get_url(self, client, url):
        response = await client.get(url)
        await self.scrap_link(html=response.text, client=client)
        return response.url

    async def scrap_link(self, html, client):
        tree = Selector(text=html)
        links = tree.xpath(self.LINK_XPATH).extract()
        return links


if __name__ == '__main__':
    scraper = Async_Scraper()
    asyncio.run(scraper.async_scrapers())

