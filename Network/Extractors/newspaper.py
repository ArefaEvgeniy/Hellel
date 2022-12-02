from newspaper import Article
from . import const


class NewsExtractor():
    def __init__(self, url):
        self.url = url

    def extract_tags(self):
        result = {}
        article = Article(self.url)
        article.download()
        article.parse()
        datas = {
            const.TITLE: article.title, const.MOVIES: article.movies,
            const.LANG: article.meta_lang, const.AUTHORS: article.authors,
            const.IMAGE: article.top_image,
            const.PUBLISH_DATE: article.publish_date,
            const.CONTENT: article.text
        }
        for tag in datas:
            if datas[tag]:
                result.update({tag: datas[tag]})

        return result
