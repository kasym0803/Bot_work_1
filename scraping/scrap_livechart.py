from parsel import Selector
import requests


# //div[@class="flex p-4"]/div/a/img/@src
# //div[@class="flex p-4"]/div/a/@href

class livechart:
    URL = 'https://freelance.habr.com/tasks'
    LINK_XPATH = '//li[@class="content-list__item"]/article/div/header/div/a/@href'
    PLUS_URL = 'https://freelance.habr.com/'

    def scrapt_chart(self):
        html = requests.get(url=self.URL).text
        tree = Selector(text=html)
        links = tree.xpath(self.LINK_XPATH).extract()
        for link in links:
            print(self.PLUS_URL + link)
        return  links[:5]


if __name__ == '__main__':
    scraper = livechart()
    scraper.scrapt_chart()
