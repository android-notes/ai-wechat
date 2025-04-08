# -*- coding: utf-8 -*-
import sys  # noqa

# PATH#
from builtin import *  # noqa
from debuger import ___l, call_flow_wrapper  # noqa


def run(args):
    pass


    if args:
        pass
    ___l(1, "获取元素<s>搜索输入框</s><img src=\"app://res\\elements\\edf58636-3b8a-4587-9509-953d807f8394.png\" element=\"\"/>所属的窗口并保存到<v>微信窗口</v>", {'debug':False})
    微信窗口 = get_window_instance_by_element(ElementDescriptor('edf58636-3b8a-4587-9509-953d807f8394', "搜索输入框"))
    ___l(2, "设置窗口<v>微信窗口</v>的状态为<s>最大化</s>", {'debug':False})
    set_window_status(微信窗口, '最大化')
    ___l(3, "在输入框<s>搜索输入框</s><img src=\"app://res\\elements\\edf58636-3b8a-4587-9509-953d807f8394.png\" element=\"\"/>输入<s>文件传输助手</s>", {'debug':False})
    input_win_element(ElementDescriptor('edf58636-3b8a-4587-9509-953d807f8394', "搜索输入框"), "文件传输助手", {"clickOption":"鼠标点击","hoverOption":"鼠标悬停","clickType":"单击","mouseKey":"左键","modifierKey":"无","delay":"2","wait":"10","position":"随机","inputType":"模拟人工输入","eng":True,"append":False,"tab":False,"enter":True,"click":True,"focusTimeout":"1"})

@call_flow_wrapper("主流程")
def main(args=None):
    return run(args)


if __name__ == "__main__":
    main(run)
