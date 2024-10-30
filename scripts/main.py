import fetcher
import scraper
import link_handler

ALL_GPUS = ["RTX 4090", "RTX 4080 Super", "RTX 4080", "RTX 4070 Ti Super", "RTX 4070 Ti", "RTX 4070 Super", "RTX 4070",
            "RTX 4060 Ti 16GB", "RTX 4060 Ti 8GB", "RX 7900 XTX", "RX 7900 XT", "RX 7900 GRE", "RX 7800 XT", "RX 7700 XT"]
CHOSEN = ['RTX 4080 Super']
ALL_STORES = ['geizhals', 'mydealz', 'mindstar']
STORES = ['geizhals', 'mydealz', 'mindstar']


class Main:
    def __init__(self):
        self.fetcher = fetcher.Fetcher()
        self.link_handler = link_handler.LinkHandler(CHOSEN)
        self.links = self.link_handler.get_all_links()

        self.prices = {}

    def handle_for_mindstar(self, keywords):
        print("Fetching data from mindstar")
        html = self.fetcher.get_page_html(self.links['mindstar'])
        if html:
            scraper_instance = scraper.Scraper()
            for keyword in keywords:
                price = scraper_instance.get_lowest_price(
                    keyword, 'mindstar', html)
                if keyword not in self.prices:
                    self.prices[keyword] = []
                self.prices[keyword].append(
                    (str(price) if price else 'x', 'mindstar', self.links['mindstar']))

    def handle_for_store(self, keyword, store_name):
        print(f"Fetching data for {keyword} from {store_name}")
        html = self.fetcher.get_page_html(self.links[store_name][keyword])
        if html:
            scraper_instance = scraper.Scraper()
            price = scraper_instance.get_lowest_price(
                keyword, store_name, html)
            if keyword not in self.prices:
                self.prices[keyword] = []
            self.prices[keyword].append(
                (str(price) if price else 'x', store_name, self.links[store_name][keyword]))

    def print_prices(self):
        with open('../prices.html', 'w') as file:
            file.write('<html><head><title>Prices</title></head><body>')
            file.write('<h1>Prices</h1>')
            for keyword, entries in self.prices.items():
                file.write(f'<h2>{keyword}</h2><ul>')
                for price, store, link in entries:
                    file.write(f'<li>{store}: {
                               price} - <a href="{link}">Link</a></li>')
                file.write('</ul>')
            file.write('</body></html>')

    def run(self):
        if 'mindstar' in STORES:
            self.handle_for_mindstar(CHOSEN)
        for keyword in CHOSEN:
            for store in [s for s in STORES if s != 'mindstar']:
                self.handle_for_store(keyword, store)

        self.print_prices()


if __name__ == "__main__":
    main = Main()
    main.run()
