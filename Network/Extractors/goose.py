from goose3 import Goose
from . import const


class GooseExtractor():
    def __init__(self, url):
        self.url = url

    def extract_tags(self):
        result = {}
        article = Goose().extract(self.url)
        datas = {
            const.TITLE: article.title, const.MOVIES: article.movies,
            const.LANG: article.meta_lang, const.AUTHORS: article.authors,
            const.DOMAIN: article.domain, const.IMAGE: article.top_image,
            const.PUBLISH_DATE: article.publish_datetime_utc,
            const.CONTENT: article.cleaned_text
        }
        for tag in datas:
            if datas[tag]:
                result.update({tag: datas[tag]})

        return result
