
import pdb
from pprint import pprint

from langchain_core.globals import set_debug
import os
from langchain_core.callbacks import BaseCallbackHandler
from langchain_core.output_parsers import StrOutputParser
# 基础Runnable/消息/历史相关导入
from langchain_core.runnables import Runnable, RunnableLambda
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.runnables.history import RunnableWithMessageHistory

# 第二步：开启原生debug日志（保留[chain/start]/[chain/end]格式）
set_debug(False)

# 第三步：自定义回调处理器——健壮版，无报错、日志整洁

class PoisonDebug(BaseCallbackHandler):
    """自定义回调：链结束时打印详细outputs，无报错、日志整洁"""
    def __init__(self, debug: bool = True, print_all: bool = True):
        super().__init__()
        self.always_verbose = True  # 强制开启回调
        self.chain_list = [] #因为结束函数没有名字,不容易发现,所以自定义一个列表为了取得序列号,chain的开始和结束不是按顺序来的,必须通过id对应准确

        self.debug = debug #执行到链开始或者结束的时候会停止,等待键盘输入
        self.printAll = print_all #打印全部
    def on_chain_start(self, serialized, inputs, **kwargs):
        """链开始：强制触发，打印【链名称+输入详情】，与原生start日志对应"""
        try:
            # 打印带醒目标识的自定义start日志，与原生日志区分
            run_id = kwargs.get("run_id")
            name = kwargs["name"]
            # 仅添加未存在的run_id元组
            if not any(item[0] == run_id for item in self.chain_list):
                self.chain_list.append((run_id, name))

            print("self.chain_list=",self.chain_list)
            idx = next(i for i, item in enumerate(self.chain_list) if item[0] == run_id)
            print(f"🚀 【链开始[chain/start] 】  序列 :{idx}\n")
            print("🚀 ", kwargs["name"])
            print("🚀  run_id=", run_id)
            if self.printAll:print(f"🚀 【链开始[chain/start]】 - inputs=：{inputs}\n")
            if isinstance(inputs, dict):
                messages = inputs.get("messages", None)
            elif isinstance(inputs, list):
                messages = inputs
            else:
                messages = None
            # print("详细打印messages")
            pprint(messages)

            if self.printAll:print(f"🚀 【链开始[chain/start]】 - serialized ={serialized}\n")
            if self.printAll:print(f"🚀 【链开始[chain/start]】 kwargs=", kwargs)
            if self.debug:
                pdb.set_trace() #加入断点,输入c继续 ,输入n执行一行代码,输入p打印变量
        except Exception as e:
            print(f"⚠️  链开始回调异常：{str(e)}\n")
    def on_chain_end(self, outputs, **kwargs) -> None:
        # 增加异常处理+类型判断，避免非预期run对象导致报错
        try:
            run_id= kwargs.get("run_id")
            idx = next(i for i, item in enumerate(self.chain_list) if item[0] == run_id)
            name = self.chain_list[idx][1]
            print(f"🚀 【链结束[chain/end] 】  序列 :{idx}\n")
            print("🚀  run_id=", run_id)
            print("🚀 ", name)
            if self.printAll: print(f"🚀 【链结束[chain/end] 】 - outputs=：{outputs}\n")
            if isinstance(outputs, dict):
                messages = outputs.get("messages", None)
            elif isinstance(outputs, list):
                messages = outputs
            else:
                messages = None
            # print("详细打印messages")
            pprint(messages)

            if self.printAll: print(f"🚀 【链结束[chain/end] 】 kwargs=", kwargs)
            if self.debug:
                pdb.set_trace()  # 断点:输入c继续 ,输入n执行一行代码,输入p打印变量
        except Exception as e:
            # 捕获所有异常，不影响主程序运行
            print(f"⚠️  链结束回调异常：{str(e)}\n")