#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
:Author: 김형근
:Email: gudrmsglgl@naver.com
:Date: 2016-02-07
"""

import sys
import os.path

APP_NAME = os.path.basename(sys.argv[0])


def read_data(input_file_name):

    ko_headers = {}
    en_headers = {}
    data = []

    with open(input_file_name, "r", encoding="utf-8") as input_file:
        for line_num, line in enumerate(input_file, 1):
            line = line.strip()

            if line_num == 1:
                for idx, header in enumerate(line.split("\t")):
                    ko_headers[header] = idx
                continue

            if line_num == 2:
                for idx, header in enumerate(line.split("\t")):
                    en_headers[header] = idx
                continue

            line_data = line.split("\t")
            data.append(line_data)

    return ko_headers, en_headers, data


def get_col_num(en_col_names, col_name):
    """주어진 헤더에 대한 열 번호를 구한다."""

    if col_name.upper() not in en_col_names:
        raise ValueError("Invalid column name:{}".format(col_name))

    return en_col_names[col_name.upper()]


def print_data(data, col_num, col_val):
    """주어진 열 번호와 값이 일치하는 행을 출력한다."""

    for row in data:
        if row[col_num] == col_val:
            print("\t".join(row))


def main(input_file_name, col_name, col_val):
    """정형 텍스트 파일의 내용을 읽어서 조건에 맞는 행을 출력한다."""
    #한글 컬럼 명을 저장한다.
    #영어 컬럼 명을 저장한다.
    #그 외 데이터를 읽는다.
    #입력된 컬럼명에 따른 값을 읽는다
    #읽은 값을 한줄로 출력한다.

    ko_col_names, en_col_names, data = read_data(input_file_name)

    col_num = get_col_num(en_col_names, col_name)
    print_data(data, col_num, col_val)

#
#main
#

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("usage: {} <input-file-name> <column-name>"
            "<column-value>".format(APP_NAME), file=sys.stderr)
        sys.exit(1)

    main(sys.argv[1], sys.argv[2], sys.argv[3])
