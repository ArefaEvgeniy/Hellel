# Создать полноценный проект для скрапинга информационых сайтов.
# Для этого необходимо создать новый проект с чистым виртуальным окружением.
# В это виртуальное окружение необходимо обязательно установить как минимум
# такие библиотеки, как: goose3, requests, bs4 и newspaper3k
# Файл запуска необходимо написать в функциональном стиле. Для каждого же
# экстрактора необходимо создать отдельный файл и описать экстрактор в виде
# класса с обязательным методом "extract_tags". В файле запуска создавать
# объект для каждого скрапинга передавая ему скрапливаемый урл и вызывая
# метод "extract_tags", который будет возвращать в виде словаря соскрапленные
# данные. В качестве ключа будут названия тэгов. Их список перечислен в
# переменной TAGS файла const.py.
# * В библиотеках goose3 и newspaper новостные тэги предопределены и они
# находятся автоматически средствами самой библиотеки, в библиотеке же
# BeautifulSoup необходимо задавать путь для нахождения каждого тэга для
# каждого интернет ресурса в отдельности. Поэтому скрапинг в коде библиотекой
# BeautifulSoup не обязателен.


import sys

from Extractors import const
from Extractors.goose import GooseExtractor
from Extractors.newspaper import NewsExtractor
from Extractors.beautiful import BeautifulSoupExtractor


def compare_result(results):
    result = {}
    ...

    return result


def show_result(result):
    ...


def main(url):
    results = []
    ...


if __name__ == "__main__":
    if len(sys.argv) == 1:
        url = 'http://www.theguardian.com/us-news/2016/jan/05/obama-gun-' \
              'control-executive-action-background-checks-licenses-gun-' \
              'shows-mental-health-funding'
        print(f'Used test url: {url}')
    else:
        url = sys.argv[1]
    main(url)
