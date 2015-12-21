# -*- coding: utf-8 -*-

"""
Copyright (c) 2015 HQM <qiminis0801@gmail.com>

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
'Software'), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

from CodeConvert import CodeConvert as cc


def utf8_test(obj):
    print '>>> 转化为 utf8 编码'
    utf = cc.Convert2Utf8_test(obj)
    print '>>>', utf, '<==>', repr(obj), '\n'


def unicode_test(obj):
    print '>>> 转化为 unicode 编码'
    uni = cc.Convert2Unicode_test(obj)
    print '>>>', uni, '<==>', repr(obj), '\n'


def _Convert2Utf8():

    # u 内含 gbk 编码字串, 先encode('latin1')为gbk编码，再decode('gbk')为unicode编码，再encode('utf8')为utf8编码
    utf8_test(u'\xd7\xee\xba\xf3\xd2\xbb\xb8\xf6\xce\xca\xcc\xe2')
    utf8_test(u'\\xd7\\xee\\xba\\xf3\\xd2\\xbb\\xb8\\xf6\\xce\\xca\\xcc\\xe2')

    # u 内含 utf8 编码字串, 直接encode('latin1')为utf8编码
    utf8_test(u'\xe6\x9c\x80\xe5\x90\x8e\xe4\xb8\x80\xe4\xb8\xaa\xe9\x97\xae\xe9\xa2\x98')
    utf8_test(u'\\xe6\\x9c\\x80\\xe5\\x90\\x8e\\xe4\\xb8\\x80\\xe4\\xb8\\xaa\\xe9\\x97\\xae\\xe9\\xa2\\x98')

    utf8_test(u'error\xe6\x9c\x80\xe5\x90\x8e\xe4\xb8\x80\xe4\xb8\xaa\xe9\x97\xae\xe9\xa2\x98')

    # unicode 编码字串, 直接encode('utf8')为utf8编码
    utf8_test(u'\u6700\u540e\u4e00\u4e2a\u95ee\u9898')
    utf8_test(u'\\u6700\\u540e\\u4e00\\u4e2a\\u95ee\\u9898')

    # gbk 编码字串, 先encode('latin1')为gbk编码，再decode('gbk')为unicode编码，再encode('utf8')为utf8编码
    utf8_test('\xd7\xee\xba\xf3\xd2\xbb\xb8\xf6\xce\xca\xcc\xe2')
    utf8_test('\\xd7\\xee\\xba\\xf3\\xd2\\xbb\\xb8\\xf6\\xce\\xca\\xcc\\xe2')

    # utf8 编码字串, 直接return
    utf8_test('\xe6\x9c\x80\xe5\x90\x8e\xe4\xb8\x80\xe4\xb8\xaa\xe9\x97\xae\xe9\xa2\x98')
    utf8_test('\\xe6\\x9c\\x80\\xe5\\x90\\x8e\\xe4\\xb8\\x80\\xe4\\xb8\\xaa\\xe9\\x97\\xae\\xe9\\xa2\\x98')

    # 无 u 的 unicode 编码字串, 先decode('raw_unicode_escape')为unicode编码, 再encode('utf8')为utf8编码
    utf8_test('\u6700\u540e\u4e00\u4e2a\u95ee\u9898')
    utf8_test('\\u6700\\u540e\\u4e00\\u4e2a\\u95ee\\u9898')

    # utf8 编码汉字
    utf8_test('最后一个问题')

    # unicode 编码汉字
    utf8_test(u'最后一个问题')

    # utf8 编码英文
    utf8_test('The last question')

    # unicode 编码英文
    utf8_test(u'The last question')

    # 全角
    utf8_test('￥全角￥')
    utf8_test(u'￥全角￥')

    # 半角
    utf8_test('¥半角¥')
    utf8_test(u'¥半角¥')

    # emoji
    utf8_test(u'🌴  新生°')
    utf8_test('\\U0001f334  \\u65b0\\u751f\xb0')


def _Convert2Unicode():

    # u 内含 gbk 编码字串, 先encode('latin1')为gbk编码，再decode('gbk')为unicode编码
    unicode_test(u'\xd7\xee\xba\xf3\xd2\xbb\xb8\xf6\xce\xca\xcc\xe2')
    unicode_test(u'\\xd7\\xee\\xba\\xf3\\xd2\\xbb\\xb8\\xf6\\xce\\xca\\xcc\\xe2')

    # u 内含 utf8 编码字串, 直接encode('latin1')为utf8编码, 再decode('utf8')为unicode编码
    unicode_test(u'\xe6\x9c\x80\xe5\x90\x8e\xe4\xb8\x80\xe4\xb8\xaa\xe9\x97\xae\xe9\xa2\x98')
    unicode_test(u'\\xe6\\x9c\\x80\\xe5\\x90\\x8e\\xe4\\xb8\\x80\\xe4\\xb8\\xaa\\xe9\\x97\\xae\\xe9\\xa2\\x98')

    unicode_test(u'error\xe6\x9c\x80\xe5\x90\x8e\xe4\xb8\x80\xe4\xb8\xaa\xe9\x97\xae\xe9\xa2\x98')

    # unicode 编码字串, 直接return
    unicode_test(u'\u6700\u540e\u4e00\u4e2a\u95ee\u9898')
    unicode_test(u'\\u6700\\u540e\\u4e00\\u4e2a\\u95ee\\u9898')

    # gbk 编码字串, 直接decode('gbk')为unicode编码
    unicode_test('\xd7\xee\xba\xf3\xd2\xbb\xb8\xf6\xce\xca\xcc\xe2')
    unicode_test('\\xd7\\xee\\xba\\xf3\\xd2\\xbb\\xb8\\xf6\\xce\\xca\\xcc\\xe2')

    # utf8 编码字串, 直接decode('utf8')为unicode编码
    unicode_test('\xe6\x9c\x80\xe5\x90\x8e\xe4\xb8\x80\xe4\xb8\xaa\xe9\x97\xae\xe9\xa2\x98')
    unicode_test('\\xe6\\x9c\\x80\\xe5\\x90\\x8e\\xe4\\xb8\\x80\\xe4\\xb8\\xaa\\xe9\\x97\\xae\\xe9\\xa2\\x98')

    # 无 u 的 unicode 编码字串, 直接decode('raw_unicode_escape')为unicode编码
    unicode_test('\u6700\u540e\u4e00\u4e2a\u95ee\u9898')
    unicode_test('\\u6700\\u540e\\u4e00\\u4e2a\\u95ee\\u9898')

    # utf8 编码汉字
    unicode_test('最后一个问题')

    # unicode 编码汉字
    unicode_test(u'最后一个问题')

    # utf8 编码英文
    unicode_test('The last question')

    # unicode 编码英文
    unicode_test(u'The last question')

    # 全角
    unicode_test('￥全角￥')
    unicode_test(u'￥全角￥')

    # 半角
    unicode_test('¥半角¥')
    unicode_test(u'¥半角¥')

    # emoji
    unicode_test(u'🌴  新生°')
    unicode_test('\\U0001f334  \\u65b0\\u751f\xb0')

    # \ 开头
    # unicode_test('\·*媛媛。')
    # unicode_test(u'\·*媛媛。')
    # unicode_test('\\\xb7*\\u5a9b\\u5a9b\\u3002')


def main():
    _Convert2Utf8()
    _Convert2Unicode()

if __name__ == '__main__':
    main()
