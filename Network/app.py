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
    for index, item_dict in enumerate(results):
        for key in item_dict:
            if not result.get(key):
                result.update({key: item_dict[key]})
            elif (item_dict[key] != result[key] and len(results) > index+1
                  and item_dict[key] == results[index+1][key]):
                result.update({key: results[index+1][key]})

    return result


def show_result(result):
    indent = 0
    for item in result:
        if len(item) > indent:
            indent = len(item)

    for key in result:
        if isinstance(result[key], list):
            res = ', '.join(result[key])
        elif key == const.CONTENT:
            res = result['content'].replace('\n', '')[:2000]
        else:
            res = str(result[key])
        if key == const.PUBLISH_DATE:
            res = f'\033[38;5;240m{res}\033[0;0m'
        elif key == const.TITLE:
            res = f'\033[38;5;39m{res}\033[0;0m'

        print(f'\033[38;5;220m{key:>{indent}}:\033[0;0m {res}')


def main(url):
    results = []

    extractors = [GooseExtractor, NewsExtractor, BeautifulSoupExtractor]
    for name_extractor in extractors:
        extractor = name_extractor(url)
        results.append(extractor.extract_tags())

    result = compare_result(results)
    show_result(result)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        url = 'http://www.theguardian.com/us-news/2016/jan/05/obama-gun-' \
              'control-executive-action-background-checks-licenses-gun-' \
              'shows-mental-health-funding'
        print(f'Used test url: {url}')
    else:
        url = sys.argv[1]
    main(url)
