# -*- coding: utf-8 -*-
import sys  # noqa

# PATH#
from builtin import *  # noqa
from debuger import ___l, call_flow_wrapper  # noqa


def run(args):
    pass


    消息Item项 = None
    if args:
        pass
        消息Item项 = args.get('消息Item项', None)
    ___l(1, "设置<s>映射</s>类型变量<v>消息数据</v>值为<s>Map()</s>", {'debug':False})
    消息数据 = Map()
    ___l(2, "拦截缩进的指令中的错误", {'debug':False})
    try:
        pass
        ___l(3, "获取<s>消息Item项</s>的<s>子孙元素</s>并将对象保存到<v>元素</v>", {'debug':False})
        元素 = get_associated_win_element2(消息Item项,'子孙元素', ElementDescriptor('f57e0c3b-87fb-465d-b6ce-98d2fcbeacfb', "消息-时间-子孙元素"), {"clickOption":"鼠标点击","hoverOption":"鼠标悬停","clickType":"单击","mouseKey":"左键","modifierKey":"无","delay":"0","wait":"0","position":"随机","inputType":"模拟人工输入","eng":False,"append":False,"tab":False,"enter":False,"click":True,"focusTimeout":"1"})
        ___l(4, "执行Python代码 <s>消息数据[\"type\"] = 'time'\r\n消息数据[\"time\"] = 元素.name</s>", {'debug':False})
        # Insert
        消息数据["type"] = 'time'
        消息数据["time"] = 元素.name
        
        ___l(5, "结束当前流程并返回参数<v>消息项数据</v>:<s>消息数据</s>", {'debug':False})
        return {"消息项数据":(消息数据),}
        set_flow_exception(None, None)
    except Exception as e:
        set_flow_exception(e, traceback.format_exc())
    ___l(6, "拦截缩进的指令中的错误", {'debug':False})
    try:
        pass
        ___l(7, "获取<s>消息Item项</s>的<s>子孙元素</s>并将对象保存到<v>元素</v>", {'debug':False})
        元素 = get_associated_win_element2(消息Item项,'子孙元素', ElementDescriptor('a20e44af-b11f-42eb-97f4-d06bceddb91e', "群消息-撤回-子孙元素"), {"clickOption":"鼠标点击","hoverOption":"鼠标悬停","clickType":"单击","mouseKey":"左键","modifierKey":"无","delay":"0","wait":"0","position":"随机","inputType":"模拟人工输入","eng":False,"append":False,"tab":False,"enter":False,"click":True,"focusTimeout":"1"})
        ___l(8, "如果符合 <v>元素.name</v> <s>包含</s> <v>撤回了一条消息</v>  则执行缩进的指令", {'debug':False})
        if if_condition_true('符合全部条件',[(元素.name,'包含',"撤回了一条消息")]):
            pass
            ___l(9, "执行Python代码 <s>消息数据[\"type\"] = 'revoke'</s>", {'debug':False})
            # Insert
            消息数据["type"] = 'revoke'
            
        elif ___l(10, "如果符合 <v>元素.name</v> <s>包含</s> <v>红包，请在手机上查看</v>  则执行缩进的指令", {'debug':False}) and if_condition_true('符合全部条件',[(元素.name,'包含',"红包，请在手机上查看")]):
            pass
            ___l(11, "执行Python代码 <s>消息数据[\"type\"] = 'hongbao'</s>", {'debug':False})
            # Insert
            消息数据["type"] = 'hongbao'
            
        else: # ___l(12, )
            ___l(12, "前面所有条件都不成立时执行缩进的指令", {'debug':False})
            pass
            ___l(13, "执行Python代码 <s>消息数据[\"type\"] = 'unknown'</s>", {'debug':False})
            # Insert
            消息数据["type"] = 'unknown'
            
        ___l(14, "结束当前流程并返回参数<v>消息项数据</v>:<s>消息数据</s>", {'debug':False})
        return {"消息项数据":(消息数据),}
        set_flow_exception(None, None)
    except Exception as e:
        set_flow_exception(e, traceback.format_exc())
    ___l(15, "拦截缩进的指令中的错误", {'debug':False})
    try:
        pass
        ___l(16, "获取<s>消息Item项</s>的<s>子孙元素</s>并将对象保存到<v>元素</v>", {'debug':False})
        元素 = get_associated_win_element2(消息Item项,'子孙元素', ElementDescriptor('aa255a53-5253-4c66-9f59-f04d5b7950bc', "群消息-个人群昵称-子孙元素"), {"clickOption":"鼠标点击","hoverOption":"鼠标悬停","clickType":"单击","mouseKey":"左键","modifierKey":"无","delay":"0","wait":"0","position":"随机","inputType":"模拟人工输入","eng":False,"append":False,"tab":False,"enter":False,"click":True,"focusTimeout":"1"})
        ___l(17, "执行Python代码 <s>消息数据[\"nick_name\"] = 元素.name</s>", {'debug':False})
        # Insert
        消息数据["nick_name"] = 元素.name
        set_flow_exception(None, None)
    except Exception as e:
        set_flow_exception(e, traceback.format_exc())
    ___l(18, "如果符合 <v>消息数据.get('nick_name',None)</v> <s>等于</s> <v>None</v>  则执行缩进的指令", {'debug':False})
    if if_condition_true('符合全部条件',[(消息数据.get('nick_name',None),'等于',None)]):
        pass
        ___l(19, "执行Python代码 <s>消息数据[\"type\"] = 'myself'</s>", {'debug':False})
        # Insert
        消息数据["type"] = 'myself'
        
        ___l(20, "结束当前流程并返回参数<v>消息项数据</v>:<s>消息数据</s>", {'debug':False})
        return {"消息项数据":(消息数据),}
    ___l(21, "拦截缩进的指令中的错误", {'debug':False})
    try:
        pass
        ___l(22, "获取<s>消息Item项</s>的<s>子孙元素</s>并将对象保存到<v>元素</v>", {'debug':False})
        元素 = get_associated_win_element2(消息Item项,'子孙元素', ElementDescriptor('65ff4a08-11d5-42f0-a935-5f2bb4106332', "消息-纯文本-子孙元素"), {"clickOption":"鼠标点击","hoverOption":"鼠标悬停","clickType":"单击","mouseKey":"左键","modifierKey":"无","delay":"0","wait":"0","position":"随机","inputType":"模拟人工输入","eng":False,"append":False,"tab":False,"enter":False,"click":True,"focusTimeout":"1"})
        ___l(23, "执行Python代码 <s>消息数据[\"type\"] = 'text'\r\n消息数据[\"content\"] = 元素.name</s>", {'debug':False})
        # Insert
        消息数据["type"] = 'text'
        消息数据["content"] = 元素.name
        ___l(24, "结束当前流程并返回参数<v>消息项数据</v>:<s>消息数据</s>", {'debug':False})
        return {"消息项数据":(消息数据),}
        set_flow_exception(None, None)
    except Exception as e:
        set_flow_exception(e, traceback.format_exc())
    ___l(25, "拦截缩进的指令中的错误", {'debug':False})
    try:
        pass
        ___l(26, "获取<s>消息Item项</s>的<s>子孙元素</s>并将对象保存到<v>元素</v>", {'debug':False})
        元素 = get_associated_win_element2(消息Item项,'子孙元素', ElementDescriptor('1ac4d206-1f3d-45fd-ab71-2a2ec1ae27fd', "群消息-带引用的文本-子孙元素"), {"clickOption":"鼠标点击","hoverOption":"鼠标悬停","clickType":"单击","mouseKey":"左键","modifierKey":"无","delay":"0","wait":"0","position":"随机","inputType":"模拟人工输入","eng":False,"append":False,"tab":False,"enter":False,"click":True,"focusTimeout":"1"})
        ___l(27, "执行Python代码 <s>消息数据[\"type\"] = 'text'\r\n消息数据[\"content\"] = 元素.name</s>", {'debug':False})
        # Insert
        消息数据["type"] = 'text'
        消息数据["content"] = 元素.name
        ___l(28, "获取<s>消息Item项</s>的<s>子孙元素</s>并将对象保存到<v>元素</v>", {'debug':False})
        元素 = get_associated_win_element2(消息Item项,'子孙元素', ElementDescriptor('0a34b6d3-8559-464f-b069-2cc964f50044', "群消息-被引用文本-子孙元素"), {"clickOption":"鼠标点击","hoverOption":"鼠标悬停","clickType":"单击","mouseKey":"左键","modifierKey":"无","delay":"0","wait":"0","position":"随机","inputType":"模拟人工输入","eng":False,"append":False,"tab":False,"enter":False,"click":True,"focusTimeout":"1"})
        ___l(29, "执行Python代码 <s>消息数据[\"ref\"] = 元素.name</s>", {'debug':False})
        # Insert
        消息数据["ref"] = 元素.name
        ___l(30, "结束当前流程并返回参数<v>消息项数据</v>:<s>消息数据</s>", {'debug':False})
        return {"消息项数据":(消息数据),}
        set_flow_exception(None, None)
    except Exception as e:
        set_flow_exception(e, traceback.format_exc())
    ___l(31, "执行Python代码 <s>消息数据[\"type\"] = 消息Item项.name[:20]\r\n消息数据.pop(\"content\",None)</s>", {'debug':False})
    # Insert
    消息数据["type"] = 消息Item项.name[:20]
    消息数据.pop("content",None)
    ___l(32, "结束当前流程并返回参数<v>消息项数据</v>:<s>消息数据</s>", {'debug':False})
    return {"消息项数据":(消息数据),}

@call_flow_wrapper("获取群聊消息项")
def main(args=None):
    return run(args)


if __name__ == "__main__":
    main(run)
