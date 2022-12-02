import requests

from bs4 import BeautifulSoup as bs
from . import const


class BeautifulSoupExtractor():
    def __init__(self, url):
        self.url = url

    def extract_tags(self):
        result = {}
        r = requests.get(self.url)
        page = bs(r.content, 'html.parser')

        try:
            title = page.find('title')
            if title:
                result.update({const.TITLE: title.string})

            authors = []
            cand_authors = page.find_all(rel="author")
            for item in cand_authors:
                authors.append(item.string)
            if authors:
                result.update({const.AUTHORS: authors})

            cand_publish_date = page.find(property="article:published_time")
            publish_date = cand_publish_date.get('content')
            if publish_date:
                result.update({const.PUBLISH_DATE: publish_date})
        except Exception:
            print('Library BeautifulSoup did not correct work.')

        return result
