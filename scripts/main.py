import fetcher
import scraper
import link_handler
import json


class Main:
    def __init__(self):
        self.read_choices()
        self.fetcher = fetcher.Fetcher()
        self.link_handler = link_handler.LinkHandler(self.chosen_gpus)
        self.links = self.link_handler.get_all_links()

        self.prices = {}

    def read_choices(self):
        with open('../data/config.json', 'r') as file:
            choices = json.load(file)

        chosen_gpus = [
            gpu for gpu, selected in choices['gpus'].items() if selected.lower() == 'yes']
        chosen_stores = [store for store, selected in choices['stores'].items(
        ) if selected.lower() == 'yes']
        self.chosen_gpus = chosen_gpus
        self.chosen_stores = chosen_stores

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
        if 'mindstar' in self.chosen_stores:
            self.handle_for_mindstar(self.chosen_gpus)
        for keyword in self.chosen_gpus:
            for store in [s for s in self.chosen_stores if s != 'mindstar']:
                self.handle_for_store(keyword, store)

        self.print_prices()


if __name__ == "__main__":
    main = Main()
    main.run()
