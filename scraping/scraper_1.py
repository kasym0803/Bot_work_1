# from parsel import Selector
# import requests
#
# class Animag_ru:
#     URL = 'https://animego.org/anime/uskorennyy-mir-beskonechnyy-vsplesk-2450'
#     LINK_XPATH = '//div[@class="animes-list-item media"]/div/a/@href'
#     PLUS_URL = 'https://animego.org/'
#
#     def scrapt_anim(self):
#         html = requests.get(url=self.URL).text
#         # print(html)
#         tree = Selector(text=html)
#         links = tree.xpath(self.LINK_XPATH).extract()
#         for link in links:
#             print(self.PLUS_URL + link)
#
#
# if __name__ == '__main__':
#     scraping = Animag_ru()
#     scraping.scrapt_anim()
# # //div[@class="views-row views-row-1 views-row-odd views-row-first new isotope-item"]/div/div/a/@href
#
