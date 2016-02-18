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