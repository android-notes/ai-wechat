# -*- coding: utf-8 -*-
import sys  # noqa

# PATH#
from builtin import *  # noqa
from debuger import ___l, call_flow_wrapper  # noqa


def run(args):
    pass


    if args:
        pass
    ___l(7, "获取和<s>左侧消息列表项元素</s><img src=\"app://res\\elements\\003c71dc-6d98-4524-ad0d-d2a2a5ede8ad.png?1744114871908\" element=\"\"/>相似的元素并保存到列表<v>左侧消息列表项元素列表</v>", {'debug':False})
    左侧消息列表项元素列表 = get_similar_win_element(ElementDescriptor('003c71dc-6d98-4524-ad0d-d2a2a5ede8ad', "左侧消息列表项元素"), {"clickOption":"鼠标点击","hoverOption":"鼠标悬停","clickType":"单击","mouseKey":"左键","modifierKey":"无","delay":"0","wait":"3","position":"随机","inputType":"模拟人工输入","eng":False,"append":False,"tab":False,"enter":False,"click":True,"focusTimeout":"1"})
    for ____rpa_gen_itr_loop_index, 左侧消息项元素 in enumerate(左侧消息列表项元素列表): # ___l(8, )
        ___l(8, "循环列表<v>左侧消息列表项元素列表</v>，当前项目保存到<v>左侧消息项元素</v>", {'debug':False})
        pass
        ___l(9, "拦截缩进的指令中的错误", {'debug':False})
        try:
            pass
            ___l(10, "获取<s>左侧消息项元素</s>的<s>子孙元素</s>并将对象保存到<v>未读消息角标元素</v>", {'debug':False})
            未读消息角标元素 = get_associated_win_element2(左侧消息项元素,'子孙元素', ElementDescriptor('b75ace00-3063-4a4e-8c89-86f38642c05b', "左侧消息列表-未读数量-子元素"), {"clickOption":"鼠标点击","hoverOption":"鼠标悬停","clickType":"单击","mouseKey":"左键","modifierKey":"无","delay":"0","wait":"0","position":"随机","inputType":"模拟人工输入","eng":False,"append":False,"tab":False,"enter":False,"click":True,"focusTimeout":"1"})
            ___l(11, "输出<s>未读消息角标元素.name</s>", {'debug':False})
            print_to_app(未读消息角标元素.name, {"renderHtml":True})
            ___l(12, "获取<s>左侧消息项元素</s>的<s>子孙元素</s>并将对象保存到<v>群_联系人名称元素</v>", {'debug':False})
            群_联系人名称元素 = get_associated_win_element2(左侧消息项元素,'子孙元素', ElementDescriptor('55e67a0f-bbc6-4717-a5b5-4366532a7e21', "左侧消息列表-群/联系人名称-子元素"), {"clickOption":"鼠标点击","hoverOption":"鼠标悬停","clickType":"单击","mouseKey":"左键","modifierKey":"无","delay":"0","wait":"3","position":"随机","inputType":"模拟人工输入","eng":False,"append":False,"tab":False,"enter":False,"click":True,"focusTimeout":"1"})
            ___l(13, "输出<s>群_联系人名称元素.name</s>", {'debug':False})
            print_to_app(群_联系人名称元素.name, {"renderHtml":True})
            set_flow_exception(None)
        except Exception as e:
            set_flow_exception(e)

@call_flow_wrapper("微信AI客服")
def main(args=None):
    return run(args)


if __name__ == "__main__":
    main(run)
