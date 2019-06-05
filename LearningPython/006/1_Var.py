"""
在Python中变量本身并不存储数据, 而是存放数据的内存位置的指针
(严格来说所有编程语言都一样, 但概念上来讲C, C++的变量本身存储数据, 指针才指向内存位置)
所以Python的变量可以指向任意一种数据类型
"""

if __name__ == "__main__":

    a = 3  # 实际上内部过程是先建立一个整数常量3, 然后建立一个变量指针a, 最后使指针a指向常量3所有的内存位置

    # 如果一个变量指向的是一个可修改对象(例如列表,集合与字典), 而另一个变量指向相同的可修改对象, 那修改对象的值后
    # 由于两个变量所引用的是同一个对象, 通过它们来获取的值会同样被修改
    # 所有当传递这种可修改对象的时候要十分小心, 必要时使用Python标准库里的copy模块
    # 注意数字,字符串都是不可修改对象

    b = ['A', 'B']
    c = b
    b[0] = 'An'
    print(b)
    print(c)
