#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
import unicodedata

def has_hz(text):  #判断是否包含中文
    hz_yes = False
    for ch in text:
        if isinstance(ch, unicode):
            if unicodedata.east_asian_width(ch)!= 'Na':
                hz_yes = True
                break
        else:
            continue
    return hz_yes


if __name__=='__main__':
    while a<=len(res):



