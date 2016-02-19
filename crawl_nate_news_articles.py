#!/usr/bin/env python3
#-*- coding: utf-8 -*-

""" 네이트 뉴스 기사를 수집한다.
: Author : 김형근
: Email: gudrmsglgl@naver.com
: Date: 2016-02-19

"""

import time
import requests

def open_url_file(url_file_name):
    """URL 파일을 열어서 파일 객체를 돌려준다."""
    url_file = open(url_file_name, "r", encoding="utf-8")

    return url_file


def create_article_file(url_file_name):
    """기사 파일을 만들어 파일 객체를 돌려준다."""

    article_file_name = url_file_name.replace("_urls.", "_html.")
    article_file = open(article_file_name, "w", encoding="utf-8")

    return article_file


def get_print_url(line):
    """인쇄용 URL을 만들어 돌려준다."""

    #기사 번호(article ID) 추출하기
    #http://news.nate.com/view/20160120n47234?mid=n0301에서
    #20160120n7234만 잘라낸다.

    p = line.rfind("/")
    q = line.rfind("?")
    article_id = line[p+1:q]
    print_url = "http://news.nate.com/view/print?aid=" +article_id

    return print_url


def get_html(print_url):
    """주어진 print_url에 대한 HTML을 돌려준다."""

    user_agent = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 " + \
        "(KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
    headers = {
        "User-Agent": user_agent
    }

    response = requests.get(print_url, headers=headers)
    html = response.text

    return html


def write_html(article_file, html):
    """주어진 HTML 텍스트를 기사 파일에 쓴다."""

    article_file.write("{}\n".format(html))
    # 기사 구분자를 쓴다.
    article_file.write("@@@@@ ARTICLE DELIMITER @@@@@\n")


def pause():
    """실행을 잠시 멈춘다."""

    time.sleep(3)



def main(url_file_name):
    """네이트 뉴스 기사 수집"""

    url_file = open_url_file(url_file_name)
    article_file = create_article_file(url_file_name)

    for line in url_file:
        print_url = get_print_url(line)
        html = get_html(print_url)
        write_html(article_file, html)
        pause()

    article_file.close()
    url_file.close()

#
#main
#

main("article_urls.20160218.txt")