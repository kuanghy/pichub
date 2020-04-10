#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) Huoty, All rights reserved
# Author: Huoty <sudohuoty@163.com>
# CreateTime: 2020-04-10 15:49:35

import hashlib
import datetime
import shutil
from pathlib import Path
from argparse import ArgumentParser


picbed_uri = "https://raw.githubusercontent.com/kuanghy/pichub/master/"


def file_md5(path):
    return hashlib.md5(open(path, 'rb').read()).hexdigest()


def import_img(path):
    path = Path(path)
    if not path.exists():
        print("Warning: '%s' not exists" % path)
        return
    today = datetime.date.today()
    content_md5 = file_md5(path)
    new_file_name = content_md5 + path.suffix
    dest_dir = Path(today.strftime('%Y')) / Path(today.strftime('%m'))
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest = dest_dir / Path(new_file_name)
    shutil.copy2(path, dest)
    print("copy '{}' to '{}'".format(path, dest))
    print("remote access url: ", picbed_uri + str(dest))


def main():
    parser = ArgumentParser()
    parser.add_argument("imgs", nargs="+")
    args = parser.parse_args()
    for path in args.imgs:
        import_img(path)


if __name__ == "__main__":
    main()
