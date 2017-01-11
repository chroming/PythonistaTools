# coding: utf-8
"""
iOS使用“应用内分享”传递文本时执行此脚本可将文件导入Pythonista 内。

***注意***
请使用 import_file.py 代替此脚本。此脚本仅可导入文本，import_file 可导入任意格式文件。

"""
import appex
import os


def main():
    """
    iOS中文本文件"分享到其他应用"时自动导入同路径下的importfile文件夹中
    :return: None
    """
    text = appex.get_text()
    if not text:
        print 'No input text found. Use this script from the share sheet in an app like Notes.'
        return
    name = os.path.basename(text)
    with open(text) as t, open(name, 'w+') as n:
        n.write(t.read())
    print 'SAVE %s to importfile OK !' % name

if __name__ == '__main__':
    main()

