from bs4 import BeautifulSoup
import re


class Scraper:
    def __init__(self):
        pass

    def parse_html(self, html_segment):
        return BeautifulSoup(html_segment, 'html.parser')

    def clean_price_mindstar(self, price_str):
        cleaned_price = re.sub(r'[^\d,]', '', price_str)
        euro_price = float(cleaned_price.replace(',', '.'))
        return int(euro_price)

    def clean_price_mydealz(self, price_str):
        cleaned_price = re.sub(r'[^\d,]', '', price_str)
        euro_price = float(cleaned_price.replace('.', '').replace(',', '.'))
        return int(euro_price)

    def extract_price_mindstar(self, data, keyword):
        lowest_price = None
        items = data.find_all('p', class_='ms_prodname',
                              text=lambda text: text and keyword in text.lower())

        if not items:
            return None

        for item in items:
            parent_html = str(item.find_parent())
            if not parent_html:
                continue
            parent_soup = self.parse_html(parent_html)
            price = parent_soup.find('p', class_='ms_price')
            if price:
                current_price = self.clean_price_mindstar(price.text)
                if lowest_price is None or current_price < lowest_price:
                    lowest_price = current_price
        return lowest_price

    def extract_price_geizhals(self, data, keyword):
        pass

    def extract_price_mydealz(self, data, keyword):
        lowest_price = None
        items = data.find_all('a', class_='js-thread-title',
                              text=lambda text: text and keyword in text.lower())

        if not items:
            return None

        for item in items:
            parent_html = str(item.find_parent().find_parent())
            if not parent_html:
                continue
            parent_soup = self.parse_html(parent_html)
            price_span = parent_soup.find('span', class_='thread-price')
            if price_span:
                current_price = self.clean_price_mydealz(price_span.text)
                if lowest_price is None or current_price < lowest_price:
                    lowest_price = current_price
        return lowest_price

    def get_lowest_price(self, keyword, store, html):
        keyword = keyword.lower()
        data = self.parse_html(html)
        if store == "mindstar":
            price = self.extract_price_mindstar(data, keyword)
        if store == "geizhals":
            price = self.extract_price_geizhals(data, keyword)
        if store == "mydealz":
            price = self.extract_price_mydealz(data, keyword)

        return price
