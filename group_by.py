#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""

:Author: 김형근
:Email: gudrmsglgl@naver.com
:Date: 2016-02-10
"""


import collections
import sys
import os.path
import operator
import itertools

APP_NAME = os.path.basename(sys.argv[0])

def groupby_print_data(data, col_num):
    """주어진 열 번호와 기준으로 자료를 정렬하여 출력한다."""

    groups = []
    uniq_keys = []
    data.sort(key=operator.itemgetter(col_num))
    print("data:"+str(data))
    for k, g in itertools.groupby(data, operator.itemgetter(col_num)):
        groups.append(list(g))
        uniq_keys.append(k)


    for ukey, group in zip (uniq_keys, groups):
        print("{} \t {}".format(ukey, len(group)))
        for member in group:
            print("\t".join(member))

def get_col_num(en_col_names, col_name):
    """영문 컬럼명에서 원하고자 하는 컬럼명의 인덱스 값을 찾는다."""
    if col_name.upper() not in en_col_names:
        raise ValueError("Invalid column name: {}".format(col_name))

    return en_col_names[col_name.upper()]


def read_input_file(input_file_name):
    """데이터를 입력받아 읽고 한글, 영문 인덱스 값을 저장한 후 데이터를 따로 저장"""
    en_headers = {}
    ko_headers = {}
    data = []

    with open(input_file_name, "r", encoding="utf-8") as input_file:
        for line_num, line in enumerate(input_file,1):
            line = line.strip()

            if line_num ==1:
                for idx, headers in enumerate(line.split("\t")):
                    ko_headers[headers] = idx
                continue

            if line_num ==2:
                for idx, headers in enumerate(line.split("\t")):
                    en_headers[headers] = idx
                continue

            line_data = line.split("\t")
            data.append(line_data)


    return ko_headers, en_headers, data


def main(input_file_name, col_name):
    """정형 텍스트 파일의 내용을 읽어서 주어진 열을 기준으로 그루핑한다."""

    ko_col_names, en_col_names, data = read_input_file(input_file_name)
    col_num = get_col_num(en_col_names, col_name)
    groupby_print_data(data, col_num)

#
#main
#

if __name__ =="__main__":
    if len(sys.argv) < 3:
        print("usage: {} <input_file_name> <column-name>".format(APP_NAME),
              file=sys.stderr)
        sys.exit(1)

    main(sys.argv[1], sys.argv[2])