# -*- coding: utf-8 -*-
import sys  # noqa

# PATH#
from builtin import *  # noqa
from debuger import ___l, call_flow_wrapper  # noqa


def run(args):
    pass


    当前消息列表 = None
    if args:
        pass
        当前消息列表 = args.get('当前消息列表', None)
    ___l(1, "设置<s>布尔</s>类型变量<v>是否是群</v>值为<s>False</s>", {'debug':False})
    是否是群 = False
    ___l(2, "如果桌面元素<s>消息-群人数-元素</s><img src=\"app://res\\elements\\21567c40-8743-48e7-af51-49e855518ed6.png\" element=\"\"/><s>存在</s>则执行缩进的指令", {'debug':False})
    if win_element_exists_or_not(ElementDescriptor('21567c40-8743-48e7-af51-49e855518ed6', "消息-群人数-元素"),'存在', {"clickOption":"鼠标点击","hoverOption":"鼠标悬停","clickType":"单击","mouseKey":"左键","modifierKey":"无","delay":"0","wait":"3","position":"随机","inputType":"模拟人工输入","eng":False,"append":False,"tab":False,"enter":False,"click":True,"focusTimeout":"1"}):
        pass
        ___l(3, "设置<s>布尔</s>类型变量<v>是否是群</v>值为<s>True</s>", {'debug':False})
        是否是群 = True
    ___l(4, "获取和<s>消息项元素</s><img src=\"app://res\\elements\\32733de9-1b5a-4c69-a3ff-f774b84d8a83.png?1744117095945\" element=\"\"/>相似的元素并保存到列表<v>消息项列表</v>", {'debug':False})
    消息项列表 = get_similar_win_element(ElementDescriptor('32733de9-1b5a-4c69-a3ff-f774b84d8a83', "消息项元素"), {"clickOption":"鼠标点击","hoverOption":"鼠标悬停","clickType":"单击","mouseKey":"左键","modifierKey":"无","delay":"0","wait":"3","position":"随机","inputType":"模拟人工输入","eng":False,"append":False,"tab":False,"enter":False,"click":True,"focusTimeout":"1"})
    for ____rpa_gen_itr_loop_index, 消息项 in enumerate(消息项列表): # ___l(5, )
        ___l(5, "循环列表<v>消息项列表</v>，当前项目保存到<v>消息项</v>", {'debug':False})
        pass
        ___l(6, "调用流程 <s>获取消息项</s>并传递参数<v>消息Item项</v>:<s>消息项</s> ", {'debug':False})
        ___call_flow_return = call_flow("获取消息项", {"消息Item项":消息项,})
        if ___call_flow_return:
            pass
        pass

@call_flow_wrapper("获取当前消息")
def main(args=None):
    return run(args)


if __name__ == "__main__":
    main(run)
