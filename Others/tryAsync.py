# _*_ coding:utf-8 _*_
import asyncio
from threading import Thread
import time

def hello(thread_name):
    print('hello from thread {}!'.format(thread_name))

event_loop_a = asyncio.new_event_loop()
event_loop_b = asyncio.new_event_loop()

def wait():
    while True:
        time.sleep(3)
        print("wait is running ...")


def callback_a():
    asyncio.set_event_loop(event_loop_a)
    asyncio.get_event_loop().call_soon(wait)
    event_loop_a.run_forever()

def callback_b():
    asyncio.set_event_loop(event_loop_b)
    asyncio.get_event_loop().call_soon(wait)
    event_loop_b.run_forever()

thread_a = Thread(target=callback_a, daemon=True)
thread_b = Thread(target=callback_b, daemon=True)
thread_a.start()
thread_b.start()
thread_a.join()
thread_b.join()