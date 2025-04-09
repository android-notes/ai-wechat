# -*- coding: utf-8 -*-
import sys  # noqa

# PATH#
from builtin import *  # noqa
from debuger import ___l, call_flow_wrapper  # noqa


def run(args):
    pass


    if args:
        pass
    ___l(1, "设置<s>布尔</s>类型变量<v>是否是群</v>值为<s>True</s>", {'debug':False})
    是否是群 = True
    ___l(2, "调用流程 <s><flow>获取当前消息</flow></s>并传递参数<v>群消息</v>:<s>是否是群</s> ", {'debug':False})
    ___call_flow_return = call_flow("获取当前消息", {"群消息":是否是群,})
    消息数据列表 = None
    if ___call_flow_return:
        pass
        消息数据列表 = ___call_flow_return.get('消息数据列表', None)
    pass

@call_flow_wrapper("测试")
def main(args=None):
    return run(args)


if __name__ == "__main__":
    main(run)
