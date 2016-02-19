#!/usr/bin/env python3
#-*- coding: utf-8 -*-

""" 네이트 경제 뉴스 기사 URL을 수집한다
: Author: 김형근
: Email: gudrmsglgl@naver.com
: Date: 2016-02-18

"""

import sys
import os.path
import time
import re
import requests

APP_NAME = os.path.basename(sys.argv[0])



def open_output_file(target_date):
    """출력 파일을 연다."""

    output_file_name = "article_urls."+target_date+".txt"
    output_file = open(output_file_name, "w", encoding="utf-8")

    return output_file


def get_html(target_date, page_num):
    """주어진 날짜와 페이지 번호에 해당하는 페이지 URL에 접근하여 HTML을 돌려준다"""

    user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) " + \
        "AppleWebKit/537.36 (KHTML, like Gecko) " + \
        "Chrome/37.0.2062.94 Safari/537.36"

    headers = {"User-Agent": user_agent}

    page_url = "http://news.nate.com/recent?cate=eco&mid=n0301&type=t&" + \
        "date=" +target_date +"&page=" +str(page_num)

    response = requests.get(page_url, headers=headers)
    html = response.text

    return html


def paging_done(html):
    """페이징이 완료되었는지를 판단"""

    done_pat = u"뉴스가 없습니다."

    if done_pat in html:
        return True

    return False


def ext_article_urls(html):
    """주어진 HTML에서 기사 URL을 추출하여 반환한다"""

    article_urls = re.findall('<a href="(.*?)"', html)
    post_article_urls= []

    for url in article_urls:
        if not url.startswith("/view/"):
            continue

        url = "http://news.nate.com"+url
        post_article_urls.append(url)

    return post_article_urls


def write_article_urls(output_file, urls):
    """기사 URL을 출력 파일에 기록한다."""

    for url in urls:
        output_file.write("{}\n".format(url))


def close_output_file(output_file):
    """출력 파일을 닫는다."""

    output_file.close()


def main(target_date):
    """네이트 경제 뉴스 기사 URL을 수집한다."""

    output_file = open_output_file(target_date)
    page_num = 1

    while True:
        html = get_html(target_date, page_num)

        if paging_done(html):
            break

        urls = ext_article_urls(html)
        write_article_urls(output_file, urls)
        page_num += 1
        time.sleep(3)

    close_output_file(output_file)

#
# main
#


main("20160218")