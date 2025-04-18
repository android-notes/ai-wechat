# -*- coding: utf-8 -*-
import sys  # noqa

# PATH#
from builtin import *  # noqa
from debuger import ___l, call_flow_wrapper  # noqa


def run(args):
    pass


    if args:
        pass
    ___l(1, "设置<s>文本列表</s>类型变量<v>群或者联系人白名单</v>值为<s>[\n'测试群2',\n'测试群3',\n'young',\n\n]</s>", {'debug':False})
    群或者联系人白名单 = [
'测试群2',
'测试群3',
'young',

]
    ___l(2, "执行Python代码 <s>class Message:\r\n    def __init__(self, type, nick_name, content):\r\n        self.type = type\r\n       </s>", {'debug':False})
    # Insert
    
    class Message:
        def __init__(self, type, nick_name, content):
            self.type = type
            self.nick_name = nick_name
            self.content = content
    
    
    
        def __repr__(self):
            return f"Message(type:{self.type}, nick_name:{self.nick_name}, content:{self.content})"
    
    
    class Chat:
        def __init__(self):
            self.tokens = []
            self.latest_message: list[Message] = []
    
    
        def __repr__(self):
            return f"Chat(tokens:{self.tokens}, latest_message:{self.latest_message})"
    
    ___l(3, "设置<s>映射</s>类型全局变量<v>群消息及回复数据</v>值为<s>defaultdict(Chat)</s>", {'debug':False})
    global_vars.群消息及回复数据 = defaultdict(Chat)
    while ___l(9, "无限循环", {'debug':False}) and True:
        pass
        ___l(11, "获取和<s>左侧消息列表项元素</s><img src=\"app://res\\elements\\003c71dc-6d98-4524-ad0d-d2a2a5ede8ad.png?1744114871908\" element=\"\"/>相似的元素并保存到列表<v>左侧消息列表项元素列表</v>", {'debug':False})
        左侧消息列表项元素列表 = get_similar_win_element(ElementDescriptor('003c71dc-6d98-4524-ad0d-d2a2a5ede8ad', "左侧消息列表项元素"), {"clickOption":"鼠标点击","hoverOption":"鼠标悬停","clickType":"单击","mouseKey":"左键","modifierKey":"无","delay":"0","wait":"3","position":"随机","inputType":"模拟人工输入","eng":False,"append":False,"tab":False,"enter":False,"click":True,"focusTimeout":"1"})
        for ____rpa_gen_itr_loop_index, 左侧消息项元素 in enumerate(左侧消息列表项元素列表): # ___l(12, )
            ___l(12, "循环列表<v>左侧消息列表项元素列表</v>，当前项目保存到<v>左侧消息项元素</v>", {'debug':False})
            pass
            ___l(13, "拦截缩进的指令中的错误", {'debug':False})
            try:
                pass
                ___l(14, "获取<s>左侧消息项元素</s>的<s>子孙元素</s>并将对象保存到<v>未读消息角标元素</v>", {'debug':False})
                未读消息角标元素 = get_associated_win_element2(左侧消息项元素,'子孙元素', ElementDescriptor('b75ace00-3063-4a4e-8c89-86f38642c05b', "左侧消息列表-未读数量-子孙元素"), {"clickOption":"鼠标点击","hoverOption":"鼠标悬停","clickType":"单击","mouseKey":"左键","modifierKey":"无","delay":"0","wait":"0","position":"随机","inputType":"模拟人工输入","eng":False,"append":False,"tab":False,"enter":False,"click":True,"focusTimeout":"1"})
                ___l(15, "输出<s>未读消息角标元素.name</s>", {'debug':False})
                print_to_app(未读消息角标元素.name, {"renderHtml":True})
                set_flow_exception(None, None)
            except Exception as e:
                set_flow_exception(e, traceback.format_exc())
            ___l(16, "如果拦截到错误则执行缩进的指令", {'debug':False})
            if has_exception():
                pass
                ___l(17, "继续下次循环", {'debug':False})
                continue
            ___l(18, "拦截缩进的指令中的错误", {'debug':False})
            try:
                pass
                ___l(19, "获取<s>左侧消息项元素</s>的<s>子孙元素</s>并将对象保存到<v>群_联系人名称元素</v>", {'debug':False})
                群_联系人名称元素 = get_associated_win_element2(左侧消息项元素,'子孙元素', ElementDescriptor('55e67a0f-bbc6-4717-a5b5-4366532a7e21', "左侧消息列表-群/联系人名称-子孙元素"), {"clickOption":"鼠标点击","hoverOption":"鼠标悬停","clickType":"单击","mouseKey":"左键","modifierKey":"无","delay":"0","wait":"3","position":"随机","inputType":"模拟人工输入","eng":False,"append":False,"tab":False,"enter":False,"click":True,"focusTimeout":"1"})
                ___l(20, "输出<s>群_联系人名称元素.name</s>", {'debug':False})
                print_to_app(群_联系人名称元素.name, {"renderHtml":True})
                ___l(21, "如果符合 <v>群或者联系人白名单</v> <s>不包含</s> <v>群_联系人名称元素.name</v>  则执行缩进的指令", {'debug':False})
                if if_condition_true('符合全部条件',[(群或者联系人白名单,'不包含',群_联系人名称元素.name)]):
                    pass
                    ___l(22, "继续下次循环", {'debug':False})
                    continue
                ___l(23, "点击桌面元素<s>群_联系人名称元素</s>", {'debug':False})
                click_win_element2(群_联系人名称元素 ,{"clickOption":"鼠标点击","hoverOption":"鼠标悬停","clickType":"单击","mouseKey":"左键","modifierKey":"无","delay":"0","wait":"3","position":"随机","inputType":"模拟人工输入","eng":False,"append":False,"tab":False,"enter":False,"click":True,"focusTimeout":"1"})
                ___l(24, "获取<s>消息-对方名称-元素</s><img src=\"app://res\\elements\\653bc0b6-0e35-4082-a3a7-5ee70f439020.png?1744261029170\" element=\"\"/>元素并保存到对象<v>会话名称元素</v>", {'debug':False})
                会话名称元素 = get_win_element(ElementDescriptor('653bc0b6-0e35-4082-a3a7-5ee70f439020', "消息-对方名称-元素"), {"clickOption":"鼠标点击","hoverOption":"鼠标悬停","clickType":"单击","mouseKey":"左键","modifierKey":"无","delay":"0","wait":"3","position":"随机","inputType":"模拟人工输入","eng":False,"append":False,"tab":False,"enter":False,"click":True,"focusTimeout":"1"})
                ___l(25, "输出<s>f\"当前会话名称 {会话名称元素.name}\"</s>", {'debug':False})
                print_to_app(f"当前会话名称 {会话名称元素.name}", {"renderHtml":True})
                ___l(26, "获取<s>任意类型</s>类型全局变量<v>群消息及回复数据</v>并保存到<s>群消息及回复数据</s>", {'debug':False})
                群消息及回复数据 = global_vars.群消息及回复数据
                ___l(27, "设置<s>任意类型</s>类型变量<v>当前会话数据</v>值为<s>群消息及回复数据[会话名称元素.name]</s>", {'debug':True})
                当前会话数据 = 群消息及回复数据[会话名称元素.name]
                while ___l(28, "无限循环", {'debug':False}) and True:
                    pass
                    ___l(29, "调用流程 <s><flow>加载新消息</flow></s>并传递参数<v>会话名称</v>:<s>会话名称元素.name</s> ", {'debug':False})
                    ___call_flow_return = call_flow("加载新消息", {"会话名称":会话名称元素.name,})
                    待回复消息 = None
                    完整消息 = None
                    if ___call_flow_return:
                        pass
                        待回复消息 = ___call_flow_return.get('待回复消息', None)
                        完整消息 = ___call_flow_return.get('完整消息', None)
                    pass
                    ___l(30, "如果符合 <v>待回复消息.length</v> <s>等于</s> <v>0</v>  则执行缩进的指令", {'debug':False})
                    if if_condition_true('符合全部条件',[(待回复消息.length,'等于',0)]):
                        pass
                        ___l(31, "退出当前循环", {'debug':False})
                        break
                    ___l(32, "设置<s>文本</s>类型变量<v>AI回复文本</v>值为<s>None</s>", {'debug':False})
                    AI回复文本 = None
                    ___l(33, "执行Python代码 <s>#调用AI，获取回复\r\nfilter_msg = []\r\nfor 消息 in 待回复消息:\r\n    if not 消息.get('nick_name', None) or not 消息.get('c</s>", {'debug':False})
                    # Insert
                    #调用AI，获取回复
                    filter_msg = []
                    for 消息 in 待回复消息:
                        if not 消息.get('nick_name', None) or not 消息.get('content', None):
                            continue
                        filter_msg.append({
                            'nick_name':消息['nick_name'],
                            'msg':消息['content']
                        })
                    
                    if not 当前会话数据.tokens:
                        当前会话数据.tokens = []
                    当前会话数据.tokens.append({'role': 'user', 'content': json.dumps(filter_msg)})
                    import os
                    from openai import OpenAI
                    
                    while True:
                        try:
                            client = OpenAI(
                                # 若没有配置环境变量，请用百炼API Key将下行替换为：api_key="sk-xxx",
                                api_key="sk-d0e12156c7914d31944e77c5d0b80efb", # 如何获取API Key：https://help.aliyun.com/zh/model-studio/developer-reference/get-api-key
                                base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
                            )
                            break
                        except Exception as e:
                            print_to_app(f'请求失败，正在重试 {e}')
                            time.sleep(1)
                            pass
                    
                    # 通过 messages 数组实现上下文管理
                    messages = [
                        {'role': 'user', 'content': '''你是一个微信群聊/单聊客服，请回答对方的问题。
                    对方的提问是个json数组，每一项都包含对方昵称及消息内容，例如 
                    [
                        {
                            "nick_name":"xl",
                            "msg":"小米SU7有优惠吗"
                        },
                        {
                            "nick_name":"xh",
                            "msg":"小米SU7有哪些配置"
                        }
                    ]，
                    回复内容是json格式，格式如下
                    [
                        {
                            "nick_name":"xl",
                            "replay":"有优惠"
                        }
                    ]
                    对方可能会询问多个问题，同一个人的回复请放到同一个json数组对象中，每条回复前添加序号
                    '''}
                    ]
                    messages.extend(当前会话数据.tokens)
                    print(">>>>>>4>>>>>")
                    
                    while True:
                        try:
                            completion = client.chat.completions.create(
                                model="deepseek-v3",  # 此处以 deepseek 为例，可按需更换模型名称。
                                messages=messages
                            )
                            break
                        except Exception as e:
                            print_to_app(f'请求失败，正在重试 {e}')
                            time.sleep(1)
                            pass
                    
                    
                    当前会话数据.tokens.append({'role': 'assistant', 'content': completion.choices[0].message.content})
                    
                    AI回复文本 = completion.choices[0].message.content
                    
                    ___l(34, "输出<s>AI回复文本</s>", {'debug':False})
                    print_to_app(AI回复文本, {"renderHtml":True})
                    ___l(35, "在输入框<s>消息输入框</s><img src=\"app://res\\elements\\e1b9589b-6db7-4856-88c0-ad185047629c.png?1744982148882\" element=\"\"/>输入<s>AI回复文本</s>", {'debug':False})
                    input_win_element(ElementDescriptor('e1b9589b-6db7-4856-88c0-ad185047629c', "消息输入框"), AI回复文本, {"clickOption":"鼠标点击","hoverOption":"鼠标悬停","clickType":"单击","mouseKey":"左键","modifierKey":"无","delay":"1","wait":"3","position":"随机","inputType":"模拟人工输入","eng":True,"append":False,"tab":False,"enter":True,"click":True,"focusTimeout":"1"})
                set_flow_exception(None, None)
            except Exception as e:
                set_flow_exception(e, traceback.format_exc())
            ___l(36, "如果拦截到错误则执行缩进的指令", {'debug':False})
            if has_exception():
                pass
                ___l(37, "获取拦截到的错误并保存到<v>err</v>", {'debug':False})
                err = get_flow_exception()
                ___l(38, "输出<s>err</s>", {'debug':False})
                print_to_app(err, {"renderHtml":True})

@call_flow_wrapper("微信AI客服")
def main(args=None):
    return run(args)


if __name__ == "__main__":
    main(run)
