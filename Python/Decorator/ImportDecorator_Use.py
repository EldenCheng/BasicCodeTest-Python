# -*- coding:gbk -*-
'''
ʾ��9: װ����������������ֲ𹫹��ൽ����py�ļ���
ͬʱ��ʾ�˶�һ������Ӧ�ö��װ����
'''

from Python.Decorator.ImportDecorator_Define import *


class Example:
    @LockHelper(MyLocker, "���β���")
    def myfunc(self):
        print("��װ�εķ���������")

    @LockHelper(MyLocker, "���β���")
    @LockHelper(LockeRex, "���β���")
    def myfunc2(self, a, b):
        print(" myfunc2() called.")
        return a + b


if __name__ == "__main__":
    a = Example()
    a.myfunc()
    print(a.myfunc())
    print(MyLocker.get_counter())
    # print(a.myfunc2(1, 2))
    # print(a.myfunc2(3, 4))
