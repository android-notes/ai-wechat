# -*- coding: utf-8 -*-
import sys  # noqa

# PATH#
from builtin import *  # noqa
from debuger import ___l, call_flow_wrapper  # noqa


def run(args):
    pass


    if args:
        pass
    ___l(1, "打开网址<s>hhrpa.com</s>，将网页对象保存到<v>web_page</v>", {'debug':False})
    web_page = open_web_page("hhrpa.com", "Google Chrome")
    ___l(2, "点击网页<v>web_page</v>中的元素<s>使用帮助</s><img src=\"app://res\\elements\\ddc28d00-9906-4273-8b99-09eb2cfcafa1.png?1744017001487\" element=\"\"/>", {'debug':False})
    click_web_element(web_page, ElementDescriptor('ddc28d00-9906-4273-8b99-09eb2cfcafa1', "使用帮助"), {"clickOption":"鼠标点击","hoverOption":"鼠标悬停","clickType":"单击","mouseKey":"左键","modifierKey":"无","delay":"0","wait":"3","position":"随机","inputType":"模拟人工输入","eng":False,"append":False,"tab":False,"enter":False,"click":True,"focusTimeout":"1"})

@call_flow_wrapper("主流程")
def main(args=None):
    return run(args)


if __name__ == "__main__":
    main(run)
