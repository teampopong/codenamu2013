# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from datetime import datetime
from itertools import chain
import json
from pyquery import PyQuery as pq
import requests
from urllib import unquote
from urlparse import urljoin


PAGESIZE = 10
LIST_URL = "http://www.mediagaon.or.kr/jsp/sch/mnews/search.jsp"
VIEW_URL = 'http://www.mediagaon.or.kr/jsp/sch/mnews/newsView.jsp?newsId='
PAYLOAD_BASE_STR = "reQuery=&collection=mkind&searchField=Subject&sortField=DATE%2FDESC%2CRANK%2FDESC&dateRange=all&startDate=&endDate=&pageStartNumber=0&prefixQuery=&login_status=logout&dupMode=&treePrefixQuery=&providerList=&subTab=&treeCheckedNameList=&query="
PAYLOAD_BASE = {}
HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.63 Safari/537.31",
    "Content-Type": "application/x-www-form-urlencoded"
}


def get_list_page(page, query):
    offset = (page - 1) * PAGESIZE
    payload = dict(PAYLOAD_BASE, **{
        'pageStartNumber': offset,
        'query': query.encode('euc-kr')
    })
    r = requests.post(LIST_URL, data=payload, headers=HEADERS)
    p_html = pq(r.text)
    p_articles = p_html.find('.tdsty02')
    for a in p_articles:
        yield pq(a)


def init_payload():
    global PAYLOAD_BASE
    args_str = PAYLOAD_BASE_STR.split('&')
    PAYLOAD_BASE = {
        arg_str.split('=')[0]: unquote(arg_str.split('=')[1])
        for arg_str in args_str
    }


def get_articles(num_pages, query):
    return chain(*(get_list_page(page, query) for page in xrange(1, num_pages+1)))


def main():
    init_payload()
    articles = get_articles(10, '강용석')
    results = {}
    for article in articles:
        title = article.find('.title').text().strip()
        date = article.find('.sort').text().strip().split('(')[0]
        date = datetime.strptime(date, '%Y.%m.%d')
        machine_date = date.strftime('%b %d, %Y')
        display_date = '%d월 %d일' % (date.month, date.day)
        press = article.find('.view > span').text().strip()[1:-1]
        summary = article.find('td[colspan="2"]').text().strip()
        url = VIEW_URL + article.find('.mnews_kinds_not_ori_link').attr('href')
        results[machine_date] = {
            'title': title,
            'date': machine_date,
            'displaydate': display_date,
            'photourl': '',
            'caption': press,
            'body': summary,
            'readmoreurl': url
        }
    with open('static/data/kys.json', 'w') as f:
        json.dump(results.values(), f, indent=2)


if __name__ == '__main__':
    main()
