# coding: utf-8
import appex
import os


def main():
    """
    iOS中文本文件"分享到其他应用"时自动导入Pythonista的importfile文件夹中
    :return: None
    """
    text = appex.get_text()
    if not text:
        print 'No input text found. Use this script from the share sheet in an app like Notes.'
        return
    name = os.path.basename(text)
    with open(text) as t:
        t.write(text)
    print 'SAVE %s.py to importfile OK !' % name

if __name__ == '__main__':
    main()

