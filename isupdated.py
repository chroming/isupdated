# -*- coding:utf-8 -*-

"""
Check if github repository release is updated.
"""

from urllib import parse
import json
import re

import requests


tag_pattern = re.compile('((?:\d*\.){0,4}\d+)')


def compare_tag(tag0, tag1):
    return True


def is_updated(github_url, current_tag):
    release = GithubReleases(github_url)
    if compare_tag(release.latest_tag, current_tag):
        return True


class GithubReleases(object):
    def __init__(self, url):
        """
        Github release object.
        :param url: The github repository url
        """
        url_path = parse.urlparse(url).path
        self.url = url

        self.base_api_url = 'https://api.github.com/repos' + (url_path
                            if url_path.endswith('releases') else url_path+'/releases')
        self.latest_response = self._get_response('/latest')
        self.latest_tag = self.latest_response.get('tag_name')

    def get_latest_dl(self, name=None, order_num=0):
        """
        Get the latest update download link.
        :param name: the file name you want to get
        :param order_num: the order number you want to get
        :return: latest download link
        """
        return self._get_download_url(self.latest_response, name, order_num)

    def _get_response(self, url_path):
        url = self.base_api_url + url_path
        return json.loads(requests.get(url).text)

    @staticmethod
    def _get_download_url(response, name=None, order_num=0):
        """
        Get the download link in response.
        :param response: Github api response json
        :param name: the file name you want to get
        :param order_num: the order number you want to get
        :return: download link
        """
        assets = response.get('assets')
        if not assets:
            return None

        if name:
            for asset in assets:
                if asset.get('name') == name:
                    return asset.get('browser_download_url')
        else:
            return assets[order_num].get('browser_download_url')
