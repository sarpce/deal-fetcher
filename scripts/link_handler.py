import json
import os

URL_MINDSTAR = "https://www.mindfactory.de/Highlights/MindStar"
URL_MYDEALZ_START = "https://www.mydealz.de/search?q="
URL_MYDEALZ_END = "&hide_expired=true&hide_local=true"


class LinkHandler:
    def __init__(self, gpu_names):
        self.gpu_names = gpu_names

    def get_mindstar(self):
        return URL_MINDSTAR

    def get_geizhals_links(self):
        with open(os.path.join(os.path.dirname(__file__), '..', 'data', 'links.json'), 'r') as file:
            links_data = json.load(file)

        urls = {}
        for gpu_name in self.gpu_names:
            urls[gpu_name] = links_data[gpu_name]
        return urls

    def get_mydealz_links(self):
        base_url = URL_MYDEALZ_START
        end_url = URL_MYDEALZ_END
        separator = "%20"

        urls = {}
        for gpu_name in self.gpu_names:
            formatted_name = gpu_name.replace(" ", separator)
            urls[gpu_name] = base_url + formatted_name + end_url
        return urls

    def get_all_links(self):
        links = {}
        links["mindstar"] = self.get_mindstar()
        links["geizhals"] = self.get_geizhals_links()
        links["mydealz"] = self.get_mydealz_links()
        return links
