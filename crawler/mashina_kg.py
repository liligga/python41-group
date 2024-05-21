import httpx
from parsel import Selector
from pprint import pprint


class MashinaCrawler:
    MAIN_URL = "https://m.mashina.kg/search/all/"
    BASE_URL = "https://m.mashina.kg"
    
    def get_page(self):
        response = httpx.get(self.MAIN_URL)
        print("Status code: ", response.status_code)
        return response.text

    def get_title(self, html):
        selector = Selector(text=html)
        # return selector.css("title::text").get()
        return selector.css("h1::text").get()
    
    def get_links(self, html):
        selector = Selector(text=html)
        links = selector.css("div.list-item a::attr(href)").getall()
        links = list(map(lambda x: self.BASE_URL + x, links))
        return links
    

if __name__ == "__main__":
    crawler = MashinaCrawler()
    page = crawler.get_page()
    # print(page[:250])
    # title = crawler.get_title(page)
    # print(title)
    links = crawler.get_links(page)
    # pprint(links)