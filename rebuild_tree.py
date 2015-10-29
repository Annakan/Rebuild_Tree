# -*- coding: utf-8 -*-

from lxml import etree


FILE =r"""data/txt_1574.xml"""
#FILE =r"""data/txt_0628.xml"""


content = etree.parse(FILE)


def scandown(element, level=0):
    for i, element in enumerate(element):
        indent = "--" * level
        info = "{} {} {}".format(indent, i, element.tag)
        if element.tag in ('type',):
            info = "{} **{}**".format(info, element.text)
        print(info)
        if len(element):
            scandown(element, level+1)


def builddown(element, level=0, current_division_type=None):
    for i, element in enumerate(element):
        if element.tag == "division":
            if element[1].text != current_division_type:
                if current_division_type == "ARTICLE":
                    level -= 1
                else:
                    level += 1
            current_division_type = element[1].text
        indent = "--" * level
        info = "{} {} {}".format(indent, i, element.tag)
        if element.tag in ('type',):
            info = "{} **{}**".format(info, element.text)
        print(info)
        if len(element):
            builddown(element, level, current_division_type)


#scandown(content.getroot())
builddown(content.getroot())

print('---')

