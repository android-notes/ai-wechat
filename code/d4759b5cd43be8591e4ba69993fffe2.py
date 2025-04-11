# -*- coding: utf-8 -*-
import sys  # noqa

# PATH#
from builtin import *  # noqa
from debuger import ___l, call_flow_wrapper  # noqa


def run(args):
    pass


    if args:
        pass
    ___l(1, "设置<s>布尔</s>类型变量<v>是否是群</v>值为<s>False</s>", {'debug':False})
    是否是群 = False
    ___l(2, "获取<s>消息-对方名称-元素</s><img src=\"app://res\\elements\\653bc0b6-0e35-4082-a3a7-5ee70f439020.png?1744261029170\" element=\"\"/>元素并保存到对象<v>会话名称元素</v>", {'debug':False})
    会话名称元素 = get_win_element(ElementDescriptor('653bc0b6-0e35-4082-a3a7-5ee70f439020', "消息-对方名称-元素"), {"clickOption":"鼠标点击","hoverOption":"鼠标悬停","clickType":"单击","mouseKey":"左键","modifierKey":"无","delay":"0","wait":"3","position":"随机","inputType":"模拟人工输入","eng":False,"append":False,"tab":False,"enter":False,"click":True,"focusTimeout":"1"})
    ___l(3, "如果桌面元素<s>消息-群人数-元素</s><img src=\"app://res\\elements\\21567c40-8743-48e7-af51-49e855518ed6.png\" element=\"\"/><s>存在</s>则执行缩进的指令", {'debug':False})
    if win_element_exists_or_not(ElementDescriptor('21567c40-8743-48e7-af51-49e855518ed6', "消息-群人数-元素"),'存在', {"clickOption":"鼠标点击","hoverOption":"鼠标悬停","clickType":"单击","mouseKey":"左键","modifierKey":"无","delay":"0","wait":"3","position":"随机","inputType":"模拟人工输入","eng":False,"append":False,"tab":False,"enter":False,"click":True,"focusTimeout":"1"}):
        pass
        ___l(4, "设置<s>布尔</s>类型变量<v>是否是群</v>值为<s>True</s>", {'debug':False})
        是否是群 = True
    ___l(5, "获取<s>映射</s>类型全局变量<v>群消息及回复数据</v>并保存到<s>群消息及回复数据</s>", {'debug':False})
    群消息及回复数据 = global_vars.群消息及回复数据
    ___l(6, "设置<s>任意类型</s>类型变量<v>当前会话数据</v>值为<s>群消息及回复数据[会话名称元素.name]</s>", {'debug':False})
    当前会话数据 = 群消息及回复数据[会话名称元素.name]
    ___l(7, "鼠标悬停在桌面元素<s>消息-列表元素</s><img src=\"app://res\\elements\\69f09d34-59ae-4d9b-b312-95d888a866c4.png\" element=\"\"/>", {'debug':False})
    hover_win_element(ElementDescriptor('69f09d34-59ae-4d9b-b312-95d888a866c4', "消息-列表元素"), {"clickOption":"鼠标点击","hoverOption":"鼠标悬停","clickType":"单击","mouseKey":"左键","modifierKey":"无","delay":"0","wait":"3","position":"随机","inputType":"模拟人工输入","eng":False,"append":False,"tab":False,"enter":False,"click":True,"focusTimeout":"1"})
    ___l(8, "设置<s>列表</s>类型变量<v>上次获取到的消息列表</v>值为<s>MyList()</s>", {'debug':False})
    上次获取到的消息列表 = MyList()
    while ___l(9, "无限循环", {'debug':False}) and True:
        pass
        ___l(10, "在横向<s>当前</s>位置，纵向<s>当前</s>位置<s>向上</s>滚动鼠标<s>500</s>像素", {'debug':False})
        scroll_mouse(None, None, 500, '向上')
        ___l(11, "调用流程 <s><flow>获取当前消息</flow></s>并传递参数<v>群消息</v>:<s>是否是群</s> ,<v>会话名称</v>:<s>会话名称元素.name</s> ", {'debug':False})
        ___call_flow_return = call_flow("获取当前消息", {"群消息":是否是群,"会话名称":会话名称元素.name,})
        消息数据列表 = None
        if ___call_flow_return:
            pass
            消息数据列表 = ___call_flow_return.get('消息数据列表', None)
        pass
        ___l(12, "如果符合 <v>消息数据列表.length</v> <s>等于</s> <v>上次获取到的消息列表.length</v>  则执行缩进的指令", {'debug':False})
        if if_condition_true('符合全部条件',[(消息数据列表.length,'等于',上次获取到的消息列表.length)]):
            pass
            ___l(13, "退出当前循环", {'debug':False})
            break
        ___l(14, "停止当前的自动化", {'debug':False})
        exit_app()

@call_flow_wrapper("加载新消息")
def main(args=None):
    return run(args)


if __name__ == "__main__":
    main(run)
