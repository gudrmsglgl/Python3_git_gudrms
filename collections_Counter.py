#!/usr/bin/env python3
#-*- coding: utf-8 -*-

""" 텍스트 파일을 읽어서 자료의 갯수를 카운트한다.
:Author : 김형근
:Email : gudrmsglgl@naver.com
:Date : 2016-02-09

"""

import sys
import os.path
import collections

APP_NAME = os.path.basename(sys.argv[0])

def count_print_data(data, col_num):
    """주어진 열 번호와 정렬 방향을 기준으로 자료를 정렬하여 출력한다."""

    col_counter = collections.Counter()

    for row in data:
        col_val = row[col_num]
        col_counter[col_val] += 1
        #col_counter[('a', 5), ('b', 2), ('c', 3)......]
    for col_val, count in col_counter.most_common():
        print("{} /t count{}".format(col_val, count))


def get_col_num(en_col_names, col_name):
    """주어진 컬럼 속성의 이름을 키로 하여 컬럼속에 col_num을 구한다."""
    if col_name.upper() not in en_col_names:
        raise ValueError("Invalid column name: {}".format(col_name))

    return en_col_names[col_name.upper()]

def read_data(input_file_name):
    """주어진 파일을 열고 컬럼 속성값을 숫자로 저장하고, 나머지는 데이터로 저장한다."""
    en_headers ={}
    co_headers ={}
    data =[]

    with open(input_file_name, "r", encoding="utf-8") as input_file:
        for line_num, line in enumerate(input_file,1):

            line = line.strip()
            if line_num ==1:
                for idx, headers in enumerate(line.split("\t")):
                    co_headers[headers] = idx
                continue

            if line_num == 2:
                for idx, headers in enumerate(line.split("\t")):
                    en_headers[headers] = idx
                continue

            line_data = line.split("\t")
            data.append(line_data)

    return co_headers, en_headers, data

def main(input_file_name, col_name):
    """정형 텍스트 파일의 내용을 읽어서 주어진 열을 기준으로 행을 계수한다."""

    ko_col_names, en_col_names, data = read_data(input_file_name)
    col_num = get_col_num(en_col_names, col_name)
    count_print_data(data, col_num)

#
#main
#

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("usage: {} <input_file_name> <column_name>".format(APP_NAME),
              file=sys.stderr)
        sys.exit(1)

    main(sys.argv[1], sys.argv[2])