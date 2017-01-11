# coding: utf-8
"""
iOS使用“应用内分享”传递任意文件（包括图片、文本及其他文件）时执行此脚本可将文件导入Pythonista 内。

"""
import appex
import os


def main():
    """
    iOS任意文件内容"分享到其他应用"时自动导入同路径下
    :return: None
    """
    names = appex.get_attachments()
    if not names:
        print 'No input text found. Use this script from the share sheet in an app like Notes.'
        return
    name = os.path.basename(names[0])
    with open(names[0], 'rb') as t, open(name, 'wb+') as n:
        n.write(t.read())
    print 'SAVE %s to importfile OK !' % name

if __name__ == '__main__':
    main()

