# from parsel import Selector
# import requests
#
# class Animag_ru:
#     URL = 'https://animag.ru/news/po-ranobe-ore-wa-subete-o-parry-suru-gyaku-kanchigai-no-sekai-saikyou-wa-boukensha-ni-naritai'
#     LINK_XPATH = '//div[@class="view-content isotope"]/div/div/div/a/@href'
#     PLUS_URL = 'https://animag.ru/news/'
#
#     def scrapt_anim(self):
#         html = requests.get(url=self.URL).text
#         # print(html)
#         tree = Selector(text=html)
#         # print(tree)
#         links = tree.xpath(self.LINK_XPATH).extract()
#         # print(links)
#         for link in links:
#             print(self.PLUS_URL + link)
#
#
# if __name__ == '__main__':
#     scraping = Animag_ru()
#     scraping.scrapt_anim()
#
#
