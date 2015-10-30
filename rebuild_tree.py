# -*- coding: utf-8 -*-

from lxml import etree
from bs4 import BeautifulSoup,Comment

FILE =r"""data/txt_1574.xml"""
#FILE =r"""data/txt_0628.xml"""


XMLcontent = etree.parse(FILE)


def scandown(element, level=0):
    for i, element in enumerate(element):
        indent = "--" * level
        info = "{} {} {}".format(indent, i, element.tag)
        if element.tag in ('type',):
            info = "{} **{}**".format(info, element.text)
        print(info)
        if len(element):
            scandown(element, level+1)


def sanitize_html_content(element):
    soup = BeautifulSoup(element.text, 'lxml')
    for comment in soup.findAll(text=lambda text:isinstance(text, Comment)):
        comment.extract()
    for element in soup('style'):
        element.extract()
    return soup


def builddown(element, level=0, prev_div_type=None):
    for i, element in enumerate(element):
        indent = "--" * level
        info = "{} {} {} ".format(indent, i, element.tag)
        if element.tag == "division":
            cur_div_type = element[1].text
            info = "{} **{}**".format(info, cur_div_type)
            if cur_div_type != prev_div_type:
                if prev_div_type == "ARTICLE":
                    level -= 1
                else:
                    level += 1
            prev_div_type = cur_div_type
        if element.tag == "htmlContent":
            content = sanitize_html_content(element)
            info += content('body')[0].text[0:50]


        print(info)
        if len(element):
            builddown(element, level, prev_div_type)


#scandown(XMLcontent.getroot())
builddown(XMLcontent.getroot())

print('---')

