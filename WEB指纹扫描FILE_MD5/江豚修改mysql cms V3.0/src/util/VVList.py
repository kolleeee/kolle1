#!/usr/bin/env python
#-*- coding: UTF-8 -*-
###################################################
# 将当前目录加入系统环境
import os
import sys
skyeyepath = os.path.realpath((os.path.dirname(__file__)) + "/../")
if not skyeyepath in sys.path:
    sys.path.append(skyeyepath)


class VVList(object):
    def __init__(self):
        # 初始化类
        self.urllist = []
        self.maxurlcount = 10000

    def clear(self):   # 清空list列表
        try:
            while len(self.urllist) > 0:
                del self.urllist[0]
        except:
            pass

    def add(self, data):
        try:
            if len(self.urllist) >= self.maxurlcount:
                print "[VVList] Full %d, can't be added any more." % self.maxurlcount
                return 0
            try:
                if self.urllist.index(data) >= 0:
                    pass
            except:
                self.urllist.append(data)  # 添加数据
        except:
            print "[VVList] Add Exception"

    def find(self, data):
        # 查询数据是否存在,-1 不存在
        try:
            return self.urllist.index(data)
        except:
            pass
        return -1

    def erase(self, data):
        try:
            n = self.find(data)
            if n >= 0:
                del self.urllist[n]
        except:
            pass

    def isfull(self):
        try:
            return len(self.urllist) >= self.maxurlcount
        except:
            pass
        return False

    def getitemcount(self):
        try:
            return len(self.urllist)
        except:
            pass
        return 0

    def getitem(self, n):
        try:
            return self.urllist[n]
        except:
            pass


if __name__=='__main__':
    ll = VVList()
    ll.add('aaaaa')
    ll.add('aaaa2a')
    ll.add('aaaa2a22')
    ll.add('aaaaa')
    ll.erase('aaaa')
    ll.erase('aaaaa')
    ll.clear()

