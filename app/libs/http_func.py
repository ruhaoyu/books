"""
@file: http.py
@author: rrh
@time: 2019/1/21 1:50 PM
"""

import requests


class HTTP:
    @staticmethod
    def get(url, return_json=True):
        r = requests.get(url)
        if r.status_code != 200:
            return {} if return_json else ''
        else:
            return r.json() if return_json else r.text

