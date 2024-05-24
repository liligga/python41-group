import asyncio
import httpx
from parsel import Selector
from pprint import pprint


class MashinaCrawler:
    MAIN_URL = "https://m.mashina.kg/search/all/"
    BASE_URL = "https://m.mashina.kg"
    
    async def get_page(self, url: str, client: httpx.AsyncClient):
        response = await client.get(self.MAIN_URL)
        print("Status code: ", response.status_code, "url: ", url)
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
    
    async def get_links_from_all_pages(self):
        async with httpx.AsyncClient() as client:
            tasks = []
            for i in range(1, 11):
                url = f"{self.MAIN_URL}?page={i}"
                task = asyncio.create_task(
                        self.get_page(url, client)
                    )
                tasks.append(task)

            pages = await asyncio.gather(*tasks)
            all_links = []
            for page in pages:
                links = self.get_links(page)
                all_links.extend(links)
            
        return all_links[:3]
    

if __name__ == "__main__":
    crawler = MashinaCrawler()
    # page = crawler.get_page()
    # # print(page[:250])
    # # title = crawler.get_title(page)
    # # print(title)
    # links = crawler.get_links(page)
    # # pprint(links)
    asyncio.run(crawler.get_links_from_all_pages())