__author__ = 'devlmj'

import importModule
import lmj_message

lmj_message.send_message.send("hello")
txt = lmj_message.receive_message.receive()
print(txt)
print("-"*50)