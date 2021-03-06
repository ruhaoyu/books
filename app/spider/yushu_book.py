"""
@file: yushu_book.py
@author: rrh
@time: 2019/1/21 2:29 PM
"""
from app.libs.http_func import HTTP
from flask import current_app


key_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'
isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'


class YuShuBook:
    isbn_url = isbn_url
    keyword_url = key_url

    def __init__(self):
        self.total = 0
        self.books = []

    def search_by_isbn(self, isbn):
        url = self.isbn_url.format(isbn)
        result = HTTP.get(url)
        self.__fill_single(result)

    def search_by_keyword(self, keyword, page=1):
        url = self.keyword_url.format(keyword, current_app.config['PER_PAGE'], self.calculate_start(page))
        result = HTTP.get(url)
        self.__fill_collection(result)

    def __fill_single(self, data):
        if data:
            self.total = 1
            self.books.append(data)

    def __fill_collection(self, data):
        if data:
            self.total = data['total']
            self.books = data['books']

    def calculate_start(self, page):
        return (page - 1) * current_app.config['PER_PAGE']
