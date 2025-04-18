# -*- coding: utf-8 -*-
import sys  # noqa

# PATH#
from builtin import *  # noqa
from debuger import ___l, call_flow_wrapper  # noqa


def run(args):
    pass


    会话名称 = None
    if args:
        pass
        会话名称 = args.get('会话名称', None)
    ___l(1, "设置<s>布尔</s>类型变量<v>是否是群</v>值为<s>False</s>", {'debug':False})
    是否是群 = False
    ___l(2, "如果桌面元素<s>消息-群人数-元素</s><img src=\"app://res\\elements\\21567c40-8743-48e7-af51-49e855518ed6.png\" element=\"\"/><s>存在</s>则执行缩进的指令", {'debug':False})
    if win_element_exists_or_not(ElementDescriptor('21567c40-8743-48e7-af51-49e855518ed6', "消息-群人数-元素"),'存在', {"clickOption":"鼠标点击","hoverOption":"鼠标悬停","clickType":"单击","mouseKey":"左键","modifierKey":"无","delay":"0","wait":"3","position":"随机","inputType":"模拟人工输入","eng":False,"append":False,"tab":False,"enter":False,"click":True,"focusTimeout":"1"}):
        pass
        ___l(3, "设置<s>布尔</s>类型变量<v>是否是群</v>值为<s>True</s>", {'debug':False})
        是否是群 = True
    ___l(4, "获取<s>映射</s>类型全局变量<v>群消息及回复数据</v>并保存到<s>群消息及回复数据</s>", {'debug':False})
    群消息及回复数据 = global_vars.群消息及回复数据
    ___l(5, "设置<s>任意类型</s>类型变量<v>当前会话数据</v>值为<s>群消息及回复数据[会话名称]</s>", {'debug':False})
    当前会话数据 = 群消息及回复数据[会话名称]
    ___l(6, "鼠标悬停在桌面元素<s>消息-列表元素</s><img src=\"app://res\\elements\\69f09d34-59ae-4d9b-b312-95d888a866c4.png\" element=\"\"/>", {'debug':False})
    hover_win_element(ElementDescriptor('69f09d34-59ae-4d9b-b312-95d888a866c4', "消息-列表元素"), {"clickOption":"鼠标点击","hoverOption":"鼠标悬停","clickType":"单击","mouseKey":"左键","modifierKey":"无","delay":"0","wait":"3","position":"随机","inputType":"模拟人工输入","eng":False,"append":False,"tab":False,"enter":False,"click":True,"focusTimeout":"1"})
    ___l(7, "设置<s>列表</s>类型变量<v>上次获取到的消息列表</v>值为<s>MyList()</s>", {'debug':False})
    上次获取到的消息列表 = MyList()
    ___l(8, "设置<s>列表</s>类型变量<v>新消息列表</v>值为<s>None</s>", {'debug':False})
    新消息列表 = None
    while ___l(9, "无限循环", {'debug':False}) and True:
        pass
        ___l(10, "在横向<s>当前</s>位置，纵向<s>当前</s>位置<s>向上</s>滚动鼠标<s>500</s>像素", {'debug':False})
        scroll_mouse(None, None, 500, '向上')
        ___l(11, "调用流程 <s><flow>获取当前消息</flow></s>并传递参数<v>群消息</v>:<s>是否是群</s> ,<v>会话名称</v>:<s>会话名称</s> ", {'debug':False})
        ___call_flow_return = call_flow("获取当前消息", {"群消息":是否是群,"会话名称":会话名称,})
        消息数据列表 = None
        if ___call_flow_return:
            pass
            消息数据列表 = ___call_flow_return.get('消息数据列表', None)
        pass
        ___l(12, "输出<s>f\"待过滤的消息数量：{len(消息数据列表)}\"</s>", {'debug':False})
        print_to_app(f"待过滤的消息数量：{len(消息数据列表)}", {"renderHtml":True})
        ___l(13, "如果符合 <v>消息数据列表.length</v> <s>等于</s> <v>上次获取到的消息列表.length</v> ，<v>消息数据列表.length</v> <s>大于</s> <v>100</v> 等任意条件则执行缩进的指令", {'debug':False})
        if if_condition_true('符合任意条件',[(消息数据列表.length,'等于',上次获取到的消息列表.length),(消息数据列表.length,'大于',100)]):
            pass
            ___l(14, "输出<s>f\"已经加载全部消息，或者超过100条: {消息数据列表.length}\"</s>", {'debug':False})
            print_to_app(f"已经加载全部消息，或者超过100条: {消息数据列表.length}", {"renderHtml":True})
            ___l(15, "设置<s>列表</s>类型变量<v>新消息列表</v>值为<s>消息数据列表</s>", {'debug':False})
            新消息列表 = 消息数据列表
        else: # ___l(16, )
            ___l(16, "前面所有条件都不成立时执行缩进的指令", {'debug':False})
            pass
            ___l(17, "如果符合 <v>len(当前会话数据.tokens)</v> <s>等于</s> <v>0</v>  则执行缩进的指令", {'debug':False})
            if if_condition_true('符合全部条件',[(len(当前会话数据.tokens),'等于',"0")]):
                pass
                ___l(18, "执行Python代码 <s># 数据未记录AI回复情况时，最后一次回复后的内容作为待回复消息\r\nprint_to_app(\"AI记录未回复过，开始查找聊天记录中最后一次回复\")\r\nfor i in range(len(消息数据列</s>", {'debug':False})
                # Insert
                # 数据未记录AI回复情况时，最后一次回复后的内容作为待回复消息
                print_to_app("AI记录未回复过，开始查找聊天记录中最后一次回复")
                for i in range(len(消息数据列表)-1, -1, -1):
                    item = 消息数据列表[i]
                    if item['type'] =='myself':
                        print_to_app(f"已找到最后一次回复，截断前{i}条消息")
                        新消息列表 = MyList(消息数据列表[i+1:])
                        break
                
            else: # ___l(19, )
                ___l(19, "前面所有条件都不成立时执行缩进的指令", {'debug':False})
                pass
                ___l(20, "执行Python代码 <s># 数据已经记录AI回复情况时，过滤掉已经回复的消息\r\nprint_to_app(\"AI记录已经回复过，开始查找待回复消息\")\r\n\r\nlast_time = None\r\n新增消息数据列表 = 消息数据</s>", {'debug':False})
                # Insert
                # 数据已经记录AI回复情况时，过滤掉已经回复的消息
                print_to_app("AI记录已经回复过，开始查找待回复消息")
                
                last_time = None
                新增消息数据列表 = 消息数据列表
                for item in 当前会话数据.latest_message:
                    if item['type'] =='time':
                        last_time = item['content'] 
                        break
                
                if last_time:
                    print_to_app(f"上次回复时间：{last_time}")
                    #1.先根据消息时间初步过滤部分消息
                    for index in range(len(新增消息数据列表)-1, -1, -1):
                        item = 新增消息数据列表[index]
                        if item['type'] =='time' and last_time == item['content'] :
                            print_to_app(f"初步过滤掉 {index+1} 条消息")
                            新增消息数据列表 = 新增消息数据列表[index+1:]
                            break
                else:
                    print_to_app(f"未找到上次回复时间")
                
                count = 0
                find = False
                for item in reversed(当前会话数据.latest_message):
                    if not item['nick_name']:
                        continue
                    if count > 5:
                        print_to_app(f"已查询超过5条记录，未找到，需要继续加载更多消息")
                        break
                    count += 1
                
                    #2.再根据上次回复的最后5条消息进行过滤
                    for index in range(len(新增消息数据列表)-1, -1, -1):
                        cur_item = 新增消息数据列表[index]
                        if cur_item['type'] == item['type'] and cur_item['content'] == item['content'] and cur_item.get('nick_name', None) == item.get('nick_name', None):
                            print_to_app(f"已找到待回复消息位置{index+1}")
                            新增消息数据列表 = 新增消息数据列表[index+1:]
                            find = True
                            break
                    if find:
                        break
                        
                if find:
                    print_to_app(f"新增待回复消息：{json.dumps(新增消息数据列表)}")
                    新消息列表 = MyList(新增消息数据列表)
        ___l(21, "如果符合 <v>新消息列表</v> <s>不等于</s> <v>None</v>  则执行缩进的指令", {'debug':False})
        if if_condition_true('符合全部条件',[(新消息列表,'不等于',None)]):
            pass
            ___l(22, "输出<s>f\"待回复消息:{json.dumps(新消息列表,ensure_ascii=False)}\"</s>", {'debug':False})
            print_to_app(f"待回复消息:{json.dumps(新消息列表,ensure_ascii=False)}", {"renderHtml":True})
            ___l(23, "结束当前流程并返回参数<v>待回复消息</v>:<s>新消息列表</s>,<v>完整消息</v>:<s>消息数据列表</s>", {'debug':False})
            return {"完整消息":(消息数据列表),"待回复消息":(新消息列表),}
        ___l(24, "设置<s>列表</s>类型变量<v>上次获取到的消息列表</v>值为<s>消息数据列表</s>", {'debug':False})
        上次获取到的消息列表 = 消息数据列表

@call_flow_wrapper("加载新消息")
def main(args=None):
    return run(args)


if __name__ == "__main__":
    main(run)
