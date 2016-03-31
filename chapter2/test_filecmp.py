#!/usr/bin/env python
"""
    比较源目录和备份目录，是否保持一致，不一致则补充增量备份
    脚本要求2个目录的路径名都是一样，不一样则会创建相应的目录
"""
# coding=utf-8
__author__ = 'root'

import os, sys
import filecmp
import re
import shutil
holderlist = []
def compareme(dir1, dir2):
    """
    递归比较2个目录
    :param dir1:
    :param dir2:
    :return:
    """
    dircomp = filecmp.dircmp(dir1, dir2)
    only_in_one = dircomp.left_only  # 源目录新文件或目录
    diff_in_one = dircomp.diff_files  # 不匹配的文件, 源目录文件发生变化
    dirpath = os.path.abspath(dir1)
    [holderlist.append(os.path.abspath(os.path.join(dir1, x))) for x in only_in_one]
    [holderlist.append(os.path.abspath(os.path.join(dir1, x))) for x in diff_in_one]
    if len(dircomp.common_dirs) > 0:   # 如果有相同目录，则递归目录
        for item in dircomp.common_dirs:
            compareme(os.path.abspath(os.path.join(dir1, item)), os.path.abspath(os.path.join(dir2, item)))
        return holderlist  # 返回差异的文件和目录

def main():
    if len(sys.argv) > 2:
        dir1 = sys.argv[1]
        dir2 = sys.argv[2]
    else:
        print "Usage： ", sys.argv[0], "sourcedir backupdir"
        sys.exit()
    source_files = compareme(dir1, dir2)
    dir1 = os.path.abspath(dir1)
    if not dir2.endswith('/'): dir2=dir+'/'
    dir2 = os.path.abspath(dir2)
    destination_files = []
    createdir_bool=False
    for item in source_files:
        destination_dir = re.sub(dir1, dir2, item)  # 这里的意思是将item中和dir1中匹配的路径换成dir2 生成备份目录
        destination_files.append(destination_dir)
        if os.path.isdir(item):
            if not os.path.exists(destination_dir):
                os.mkdir(destination_dir)
                createdir_bool = True

    if createdir_bool:
        destination_files = []
        source_files = []
        source_files = compareme(dir1, dir2)
        for item in source_files:
            destination_dir = re.sub(dir1, dir2, item)
            destination_files.append(destination_dir)
        print '更新item列表: '
        print source_files
        copy_pair = zip(source_files, destination_files)
        for item in copy_pair:
            if os.path.isfile(item[0]):
                shutil.copyfile(item[0], item[1])

if __name__ == '__main__':
    main()


