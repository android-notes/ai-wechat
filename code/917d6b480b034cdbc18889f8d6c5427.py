# -*- coding: utf-8 -*-
import sys  # noqa

# PATH#
from builtin import *  # noqa
from debuger import ___l, call_flow_wrapper  # noqa


def run(args):
    pass


    if args:
        pass
    ___l(1, "设置<s>文本列表</s>类型变量<v>群或者联系人白名单</v>值为<s>[\n'测试群2',\n'测试群3',\n'young',\n'郡西澜山业主群（3群）',\n'杜雅苑纯业主1群 拒绝广告',\n\n\n]</s>", {'debug':False})
    群或者联系人白名单 = [
'测试群2',
'测试群3',
'young',
'郡西澜山业主群（3群）',
'杜雅苑纯业主1群 拒绝广告',


]
    ___l(2, "执行Python代码 <s>class Message:\r\n    def __init__(self, type, nick_name, content):\r\n        self.type = type\r\n       </s>", {'debug':False})
    # Insert
    
    class Message:
        def __init__(self, type, nick_name, content):
            self.type = type
            self.nick_name = nick_name
            self.content = content
    
        def greet(self):
            pass
    
        def __repr__(self):
            return f"Message(type:{self.type}, nick_name:{self.nick_name}, content:{self.content})"
    
    
    class Chat:
        def __init__(self):
            self.tokens = []
            self.latest_message: list[Message] = []
    
        def greet(self):
            pass
    
        def __repr__(self):
            return f"Chat(tokens:{self.tokens}, latest_message:{self.latest_message})"
    
    ___l(3, "设置<s>映射</s>类型全局变量<v>群消息及回复数据</v>值为<s>defaultdict(Chat)</s>", {'debug':False})
    global_vars.群消息及回复数据 = defaultdict(Chat)
    ___l(10, "获取和<s>左侧消息列表项元素</s><img src=\"app://res\\elements\\003c71dc-6d98-4524-ad0d-d2a2a5ede8ad.png?1744114871908\" element=\"\"/>相似的元素并保存到列表<v>左侧消息列表项元素列表</v>", {'debug':False})
    左侧消息列表项元素列表 = get_similar_win_element(ElementDescriptor('003c71dc-6d98-4524-ad0d-d2a2a5ede8ad', "左侧消息列表项元素"), {"clickOption":"鼠标点击","hoverOption":"鼠标悬停","clickType":"单击","mouseKey":"左键","modifierKey":"无","delay":"0","wait":"3","position":"随机","inputType":"模拟人工输入","eng":False,"append":False,"tab":False,"enter":False,"click":True,"focusTimeout":"1"})
    for ____rpa_gen_itr_loop_index, 左侧消息项元素 in enumerate(左侧消息列表项元素列表): # ___l(11, )
        ___l(11, "循环列表<v>左侧消息列表项元素列表</v>，当前项目保存到<v>左侧消息项元素</v>", {'debug':False})
        pass
        ___l(12, "拦截缩进的指令中的错误", {'debug':False})
        try:
            pass
            ___l(13, "获取<s>左侧消息项元素</s>的<s>子孙元素</s>并将对象保存到<v>未读消息角标元素</v>", {'debug':False})
            未读消息角标元素 = get_associated_win_element2(左侧消息项元素,'子孙元素', ElementDescriptor('b75ace00-3063-4a4e-8c89-86f38642c05b', "左侧消息列表-未读数量-子孙元素"), {"clickOption":"鼠标点击","hoverOption":"鼠标悬停","clickType":"单击","mouseKey":"左键","modifierKey":"无","delay":"0","wait":"0","position":"随机","inputType":"模拟人工输入","eng":False,"append":False,"tab":False,"enter":False,"click":True,"focusTimeout":"1"})
            ___l(14, "输出<s>未读消息角标元素.name</s>", {'debug':False})
            print_to_app(未读消息角标元素.name, {"renderHtml":True})
            ___l(15, "获取<s>左侧消息项元素</s>的<s>子孙元素</s>并将对象保存到<v>群_联系人名称元素</v>", {'debug':False})
            群_联系人名称元素 = get_associated_win_element2(左侧消息项元素,'子孙元素', ElementDescriptor('55e67a0f-bbc6-4717-a5b5-4366532a7e21', "左侧消息列表-群/联系人名称-子孙元素"), {"clickOption":"鼠标点击","hoverOption":"鼠标悬停","clickType":"单击","mouseKey":"左键","modifierKey":"无","delay":"0","wait":"3","position":"随机","inputType":"模拟人工输入","eng":False,"append":False,"tab":False,"enter":False,"click":True,"focusTimeout":"1"})
            ___l(16, "输出<s>群_联系人名称元素.name</s>", {'debug':False})
            print_to_app(群_联系人名称元素.name, {"renderHtml":True})
            ___l(17, "如果符合 <v>群或者联系人白名单</v> <s>不包含</s> <v>群_联系人名称元素.name</v>  则执行缩进的指令", {'debug':False})
            if if_condition_true('符合全部条件',[(群或者联系人白名单,'不包含',群_联系人名称元素.name)]):
                pass
                ___l(18, "继续下次循环", {'debug':False})
                continue
            ___l(19, "点击桌面元素<s>群_联系人名称元素</s>", {'debug':False})
            click_win_element2(群_联系人名称元素 ,{"clickOption":"鼠标点击","hoverOption":"鼠标悬停","clickType":"单击","mouseKey":"左键","modifierKey":"无","delay":"0","wait":"3","position":"随机","inputType":"模拟人工输入","eng":False,"append":False,"tab":False,"enter":False,"click":True,"focusTimeout":"1"})
            ___l(20, "调用流程 <s><flow>加载新消息</flow></s>", {'debug':False})
            ___call_flow_return = call_flow("加载新消息", {})
            if ___call_flow_return:
                pass
            pass
            set_flow_exception(None)
        except Exception as e:
            set_flow_exception(e)

@call_flow_wrapper("微信AI客服")
def main(args=None):
    return run(args)


if __name__ == "__main__":
    main(run)
