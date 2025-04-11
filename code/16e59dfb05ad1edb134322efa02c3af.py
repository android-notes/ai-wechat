# -*- coding: utf-8 -*-
import sys  # noqa

# PATH#
from builtin import *  # noqa
from debuger import ___l, call_flow_wrapper  # noqa


def run(args):
    pass


    群消息 = None
    会话名称 = None
    if args:
        pass
        群消息 = args.get('群消息', None)
        会话名称 = args.get('会话名称', None)
    ___l(1, "设置<s>列表</s>类型变量<v>消息列表数据</v>值为<s>MyList()</s>", {'debug':False})
    消息列表数据 = MyList()
    ___l(2, "获取和<s>消息项元素</s><img src=\"app://res\\elements\\32733de9-1b5a-4c69-a3ff-f774b84d8a83.png?1744117095945\" element=\"\"/>相似的元素并保存到列表<v>消息项列表</v>", {'debug':False})
    消息项列表 = get_similar_win_element(ElementDescriptor('32733de9-1b5a-4c69-a3ff-f774b84d8a83', "消息项元素"), {"clickOption":"鼠标点击","hoverOption":"鼠标悬停","clickType":"单击","mouseKey":"左键","modifierKey":"无","delay":"0","wait":"3","position":"随机","inputType":"模拟人工输入","eng":False,"append":False,"tab":False,"enter":False,"click":True,"focusTimeout":"1"})
    for ____rpa_gen_itr_loop_index, 消息项 in enumerate(消息项列表): # ___l(3, )
        ___l(3, "循环列表<v>消息项列表</v>，当前项目保存到<v>消息项</v>", {'debug':False})
        pass
        ___l(4, "如果符合 <v>群消息</v> <s>等于</s> <v>True</v>  则执行缩进的指令", {'debug':False})
        if if_condition_true('符合全部条件',[(群消息,'等于',True)]):
            pass
            ___l(5, "调用流程 <s><flow>获取群聊消息项</flow></s>并传递参数<v>消息Item项</v>:<s>消息项</s> ", {'debug':False})
            ___call_flow_return = call_flow("获取群聊消息项", {"消息Item项":消息项,})
            消息项数据 = None
            if ___call_flow_return:
                pass
                消息项数据 = ___call_flow_return.get('消息项数据', None)
            pass
        else: # ___l(6, )
            ___l(6, "前面所有条件都不成立时执行缩进的指令", {'debug':False})
            pass
            ___l(7, "调用流程 <s><flow>获取消息项</flow></s>并传递参数<v>消息Item项</v>:<s>消息项</s> ,<v>对方名称</v>:<s>会话名称</s> ", {'debug':False})
            ___call_flow_return = call_flow("获取消息项", {"消息Item项":消息项,"对方名称":会话名称,})
            消息项数据 = None
            if ___call_flow_return:
                pass
                消息项数据 = ___call_flow_return.get('消息项数据', None)
            pass
        ___l(8, "在列表<v>消息列表数据</v><s>尾部</s>添加数据<s>消息项数据</s>", {'debug':False})
        add_to_list(消息列表数据, 消息项数据, len(消息列表数据))
        ___l(9, "输出<s>消息项数据</s>", {'debug':False})
        print_to_app(消息项数据, {"renderHtml":True})
    ___l(10, "结束当前流程并返回参数<v>消息数据列表</v>:<s>消息列表数据</s>", {'debug':False})
    return {"消息数据列表":(消息列表数据),}

@call_flow_wrapper("获取当前消息")
def main(args=None):
    return run(args)


if __name__ == "__main__":
    main(run)
