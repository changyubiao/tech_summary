python3中的特性property介绍
===========================

[TOC]

特性的引入
----------

特性和属性的区别是什么?
~~~~~~~~~~~~~~~~~~~~~~~

特性与属性的区别是什么 ?

在python 中 属性 这个 实例方法, 类变量 都是属性. 属性, attribute

在python 中 数据的属性 和处理数据的方法 都可以叫做 属性. 简单来说
在一个类中, 方法是属性, 数据也是属性 .

.. code:: python

   class Animal:
       name = 'animal'

       def bark(self):
           print('bark')
           pass

       @classmethod
       def sleep(cls):
           print('sleep')
           pass

       @staticmethod
       def add():
           print('add')

在命令行里面执行

.. code:: python

       >>> animal = Animal()
       >>> animal.add()
       add
       >>> animal.sleep()
       sleep
       >>> animal.bark()
       bark
       >>> hasattr(animal,'add') #1
       True 
       >>> hasattr(animal,'sleep')
       True
       >>> hasattr(animal,'bark')
       True

可以看出\ ``#1`` animal 中 是可以拿到 add ,sleep bark 这些属性的.

特性: property 这个是指什么? 在不改变类接口的前提下使用 存取方法
(即读值和取值) 来修改数据的属性.

什么意思呢?

就是通过 obj.property 来读取一个值, obj.property = xxx ,来赋值

还以上面 animal 为例:

.. code:: python

   class Animal:

       @property
       def name(self):
           print('property name ')
           return self._name

       @name.setter
       def name(self, val):
           print('property set name ')
           self._name = val

       @name.deleter
       def name(self):
           del self._name
           

这个时候 name 就是了特性了.

::

   >>> animal = Animal()
   >>> animal.name='dog'
   property set name 
   >>> animal.name
   property name 
   'dog'
   >>> 
   >>> animal.name='cat'
   property set name 
   >>> animal.name
   property name 
   'cat'

肯定有人会疑惑,写了那么多的代码, 还不如直接写成属性呢,多方便.

比如这段代码: 直接把name 变成类属性 这样做不是很好吗,多简单.
这样写看起来 也没有太大的问题.但是 如果给name 赋值成数字
这段程序也是不会报错. 这就是比较\ **大的问题**\ 了.

::

   >>> class Animal:
   ...     name=None
   ...     
   >>> animal = Animal()
   >>> animal.name
   >>> animal.name='frank'
   >>> animal.name
   'frank'
   >>> animal.name='chang'
   >>> animal.name
   'chang'
   >>> animal.name=250
   >>> animal
   <Animal object at 0x10622b850>
   >>> animal.name
   250
   >>> type(animal.name)
   <class 'int'>

这里给 ``animal.name`` 赋值成 250, 程序从逻辑上来说 没有问题.
但其实这样赋值是毫无意义的.

我们一般希望 不允许这样的赋值,就希望 给出 **报错或者警告** 之类的.

.. code:: python

   animal= Animal()
   animal.name=100
   property set name 
   Traceback (most recent call last):
     File "<input>", line 1, in <module>
     File "<input>", line 13, in name
   ValueError: expected val is str

其实当name 变成了property 之后,我们就可以对name 赋值 进行控制.
防止一些非法值变成对象的属性. 比如说name 应该是这个字符串, 不应该是数字
这个时候 就可以在 setter 的时候 进行判断,来控制 能否赋值.

要实现上述的效果, 其实也很简单 setter 对value进行判断就好了.

::

   class Animal:

       @property
       def name(self):
           print('property name ')
           return self._name

       @name.setter
       def name(self, val):
           print('property set name ')
           # 这里 对 value 进行判断 
           if not isinstance(val,str):
               raise  ValueError("expected val is str")
           self._name = val

感受到 特性的魅力了吧,可以通过 赋值的时候 ,对
值进行校验,方式不合法的值,进入到对象的属性中. 下面 看下
如何设置只读属性, 和如何设置读写 特性.

   假设 有这个的一个需求 , 某个 类的属性一个初始化之后 就不允许
   被更改,这个 就可以用特性这个问题 , 比如一个人身高是固定, 一旦
   初始化后,就不允许改掉.

设置只读特性
~~~~~~~~~~~~

.. code:: python

   class Frank:
       def __init__(self, height):
           self._height = height

       @property
       def height(self):
           return self._height

::

   >>> frank = Frank(height=100)
   >>> frank.height
   100
   >>> frank.height =150
   Traceback (most recent call last):
     File "<input>", line 1, in <module>
   AttributeError: can't set attribute

这里初始化 frank后 就不允许 就修改 这个 height 这个值了.
(实际上也是可以修改的) 重新 给 height 赋值就会报错, 报错 AttributeError
,这里 不实现 setter 就可以了.

设置 读写 特性
~~~~~~~~~~~~~~

.. code:: python

   class Frank:
       def __init__(self, height):
           self._height = height

       @property
       def height(self):
           return self._height

       @height.setter
       def height(self, value):
           """
           给特性赋值 
           """
           self._height = value

.. code:: python

   >>> 
   >>> frank = Frank(height=100)
   >>> frank.height
   100
   >>> frank.height=165
   >>> frank.height
   165

..

   比如对人的身高 在1米 到 2米之间 这样的限制

对特性的合法性进行校验
~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

       
   class Frank:

       def __init__(self, height):
           self.height = height  # 注意这里写法

       @property
       def height(self):
           return self._height

       @height.setter
       def height(self, value):
           """
           判断逻辑 属性的处理逻辑
           定义 了 setter 方法之后就  修改 属性 了.
           判断 属性 是否合理 ,不合理直接报错. 阻止赋值,直接抛异常

           :param value:
           :return:
           """
           if not isinstance(value, (float,int)):
               raise ValueError("高度应该是 数值类型")
           if value < 100 or value > 200:
               raise ValueError("高度范围是100cm 到 200cm")
           self._height = value

在python console 里面测试 结果:

.. code:: python

   >>> frank = Frank(100)
   >>> frank.height
   100
   >>> frank.height='aaa'
   Traceback (most recent call last):
     File "<input>", line 1, in <module>
     File "<input>", line 21, in height
   ValueError: 高度应该是 数值类型
   >>> frank.height=250
   Traceback (most recent call last):
     File "<input>", line 1, in <module>
     File "<input>", line 23, in height
   ValueError: 高度范围是100cm 到 200cm

这样 就可以 进行严格的控制, 一些特性的方法性 ,通过写setter 方法
来保证数据 准确性,防止一些非法的数据进入到实例中.

property 是什么?
----------------

实际是一个类 , 然后 就是一个装饰器. 让一个 方法 变成 一个特性. 假设
某个类的实例方法 bark 被 property 修饰了后, 调用方式就会发生变化.

.. code:: python

   obj.bark() --> obj.bak 

其实 特性 模糊了 方法 和数据 的界限.

方法 是 可调用的属性 , 而property 是 可定制化的’属性’ . 一般方法的名称
是一个动词(行为). 而特性property 应该是名词.

如果 我们 一旦确定了 属性不是动作, 我们需要在标准属性 和 property
之间做出选择 .

一般来说 你如果要控制 property 的 访问过程,就要用 property .
否则用标准的属性 即可 .

``attribute`` 属性 和 ``property`` 特性 的区别 在于 当property 被读取,
赋值, 删除时候, 自动会执行 某些 特定的动作.

peroperty 详解

特性都是类属性，但是特性管理的其实是实例属性的存取。– 摘自 fluent python

下面的例子来自 fluent python

看一下 几个例子 来说明几个 特性和属性 区别

.. code:: python

   >>> class Class:
               """
               data 数据属性和 prop 特性。
               """
   ...     data = 'the class data attr'
   ... 
   ...     @property
   ...     def prop(self):
   ...         return 'the prop value'
   ... 
   >>> 
   >>> obj= Class() 
   >>> vars(obj)
   {}
   >>> obj.data
   'the class data attr'
   >>> Class.data
   'the class data attr'
   >>> obj.data ='bar'
   >>> Class.data
   'the class data attr'

实例属性遮盖类的数据属性 , 就是说 如果 obj.data 重新 修改了 , 类的属性
不会被修改 .

下面 尝试 obj 实例的 prop 特性

.. code:: python

   >>> Class.prop
   <property object at 0x110968ef0>
   >>> obj.prop
   'the prop value'
   >>> obj.prop ='foo'
   Traceback (most recent call last):
     File "<input>", line 1, in <module>
   AttributeError: can't set attribute
   >>> obj.__dict__['prop'] ='foo'
   >>> vars(obj)
   {'data': 'bar', 'prop': 'foo'}
   >>> obj.prop  #1
   'the prop value'
   >>> Class.prop ='frank'
   >>> obj.prop
   'foo'

我尝试修改 obj.prop 会直接报错 ,这个容易理解, 因为 property 没有实现
setter 方法 . 我直接 修改 obj.__dict_\_

然后 在 ``#1`` 的地方, 发现 还是正常 调用了特性 ,而没有 属性的值.

当我改变 Class.prop 变成一个 属性的时候 .

再次 调用 ``obj.prop`` 才调用到了 实例属性.

再看一个例子 添加 特性

.. code:: python

   class Class:
       data = 'the class data attr'

       @property
       def prop(self):
           return 'the prop value'

.. code:: python

   >>> obj.data
   'bar'
   >>> Class.data
   'the class data attr'

   # 把类的data 变成 特性
   >>> Class.data = property(lambda self:'the "data" prop value')
   >>> obj.data
   'the "data" prop value'
   >>> del Class.data
   >>> obj.data
   'bar'
   >>> vars(obj)
   {'data': 'bar', 'prop': 'foo'}

改变 data 变成 特性后, obj.data 也改变了. 删除 这个特性的时候 , obj.data
又恢复了.

本节的主要观点是， obj.attr 这样的表达式不会从 obj 开始寻找 attr，而是从
obj.__class_\_ 开始，而且，仅当类中没有名为 attr 的特性时, Python 才会在
obj 实 例中寻找。这条规则 适用于 **特性** .

property 实际上 是一个类

.. code:: python

       def __init__(self, fget=None, fset=None, fdel=None, doc=None): 
           pass
           # known special case of property.__init__

完成 的要实现一个特性 需要 这 4个参数, get , set ,del , doc
这些参数.但实际上大部分情况下,只要实现 get ,set 即可.

特性的两种写法
--------------

下面 两种 写法 都是可行的.

第一种写法
~~~~~~~~~~

使用 装饰器 property 来修饰一个方法

.. code:: python

   # 方法1 
   class Animal:

       def __init__(self, name):
           self._name = name

       @property
       def name(self):
           print('property name ')
           return self._name

       @name.setter
       def name(self, val):
           print('property set name ')

           if not isinstance(val, str):
               raise ValueError("expected val is str")
           self._name = val

       @name.deleter
       def name(self):
           del self._name

第二种写法
~~~~~~~~~~

直接 实现 set get delete 方法 即可, 通过property 传入 这个参数

.. code:: python

   # 方法二 
   class Animal2:

       def __init__(self, name):
           self._name = name

       def _set_name(self, val):
           if not isinstance(val, str):
               raise ValueError("expected val is str")

           self._name = val

       def _get_name(self):
           return self._name

       def _delete_name(self):
           del self._name

       name = property(fset=_set_name, fget=_get_name,fdel= _delete_name,doc= "name 这是特性描述")


   if __name__ == '__main__':
       animal = Animal2('dog')
       

::

   >>> animal = Animal2('dog')
   >>> 
   >>> animal.name
   'dog'
   >>> animal.name
   'dog'

   >>> help(Animal2.name)
   Help on property:

       name 这是特性描述

   >>> animal.name='cat'
   >>> animal.name
   'cat'

常见的一些例子
--------------

1. 缓存某些值
2. 对一些值 进行合法性校验.

对一些值 进行合法性校验.
~~~~~~~~~~~~~~~~~~~~~~~~

对一些 特性 赋值的时候 进行 合法性的校验,前面 都有举例子.

在举一个小例子 比如 有一个货物, 有重量 和 价格 ,需要保证
这两个属性是正数 不能是 0 , 即>0 的值 .

好了 有了刚刚 代码的基础 ,下面的代码 就写好了.

基础版代码
^^^^^^^^^^

.. code:: python

   class Goods:

       def __init__(self, name, weight, price):
           """

           :param name: 商品名称
           :param weight:  重量
           :param price: 价格
           """
           self.name = name
           self.weight = weight
           self.price = price

       def __repr__(self):

           return f"{self.__class__.__name__}(name={self.name},weight={self.weight},price={self.price})"

       @property
       def weight(self):
           return self._weight

       @weight.setter
       def weight(self, value):
           if value < 0:
               raise ValueError(f"expected value > 0, but now value:{value}")

           self._weight = value

       @property
       def price(self):
           return self._price

       @price.setter
       def price(self, value):
           if value < 0:
               raise ValueError(f"expected value > 0, but now value:{value}")
           self._price = value

.. code:: python

   >>> goods = Goods('apple', 10, 30)
   ... 
   >>> goods
   Goods(name=apple,weight=10,price=30)
   >>> goods.weight
   10
   >>> goods.weight=-10
   Traceback (most recent call last):
     File "<input>", line 1, in <module>
     File "<input>", line 26, in weight
   ValueError: expected value > 0, but now value:-10
   >>> goods.price
   30
   >>> goods.price=-3
   Traceback (most recent call last):
     File "<input>", line 1, in <module>
     File "<input>", line 37, in price
   ValueError: expected value > 0, but now value:-3
   >>> goods
   Goods(name=apple,weight=10,price=30)
   >>> goods.price=20
   >>> goods
   Goods(name=apple,weight=10,price=20)

代码 可以正常的判断出来 ,这些非法值了. 这样写 有点问题是什么呢? 就是
发现 weight ,price 判断值的逻辑 几乎是一样的代码.. 都是判断是 大于 0 吗?
然而我却写了 两遍相同的代码 .

优化版代码
^^^^^^^^^^

有没有更好的解决方案呢?

是有的, 我们可以写一个 工厂函数 来返回一个property , 这实际上是两个
property 而已.

下面 就是工厂函数 ,用来生成一个 property 的.

.. code:: python

   def validate(storage_name):
       """
       用来验证 storage_name 是否合法性 , weight  , price
       :param storage_name:
       :return:
       """
       pass

       def _getter(instance):
           return instance.__dict__[storage_name]

       def _setter(instance, value):
           if value < 0:
               raise ValueError(f"expected value > 0, but now value:{value}")

           instance.__dict__[storage_name] = value

       return property(fget=_getter, fset=_setter)

货物类 就可以像 下面这样写

.. code:: python

   class Goods:
       weight = validate('weight')
       price = validate('price')

       def __init__(self, name, weight, price):
           """

           :param name: 商品名称
           :param weight:  重量
           :param price: 价格
           """
           self.name = name
           self.weight = weight
           self.price = price

       def __repr__(self):
           return f"{self.__class__.__name__}(name={self.name},weight={self.weight},price={self.price})"

这样看起来是不是 比较舒服一点了.

.. code:: python

   >>> goods = Goods('apple', 10, 30)
   >>> goods.weight
   10
   >>> goods.weight=-10
   Traceback (most recent call last):
     File "<input>", line 1, in <module>
     File "<input>", line 16, in _setter
   ValueError: expected value > 0, but now value:-10
   >>> goods
   Goods(name=apple,weight=10,price=30)
   >>> goods.price=-2
   Traceback (most recent call last):
     File "<input>", line 1, in <module>
     File "<input>", line 16, in _setter
   ValueError: expected value > 0, but now value:-2
   >>> goods
   Goods(name=apple,weight=10,price=30)

可以看出 代码 可以正常的工作了.

缓存一些值
~~~~~~~~~~

::

   >>> from urllib.request import urlopen
   ... 
   ... 
   ... class WebPage:
   ... 
   ...     def __init__(self, url):
   ...         self.url = url
   ... 
   ...         self._content = None
   ... 
   ...     @property
   ...     def content(self):
   ...         if not self._content:
   ...             print("Retrieving new page")
   ...             self._content = urlopen(self.url).read()[0:10]
   ... 
   ...         return self._content
   ...     
   >>> 
   >>> 
   >>> url = 'http://www.baidu.com'
   >>> page = WebPage(url)
   >>> 
   >>> page.content
   Retrieving new page
   b'<!DOCTYPE '
   >>> page.content
   b'<!DOCTYPE '
   >>> page.content
   b'<!DOCTYPE '

可以看出 第一次调用了 urlopen 从网页中读取值, 第二次就没有调用urlopen
而是直接返回content 的内容.

总结
----

python 的特性 算是python的 高级语法,不要因为到处都要用 这个 特性的语法
.实际上 大部分 情况是用不到这个 语法的. 如果
代码中,需要对属性进行检查就要考虑 用这样的语法了. 希望你看完 之后不要
认为这种语法非常常见, 事实上不是的. 其实 更好的做法对 属性 检查
可以使用描述符 来完成. 描述符 是一个比较大的话题,本文章 暂未提及,后续
的话,可能 会写一下 关于描述的一些用法 ,这样就 能
更好的理解python,更加深入的理解python.

参考文档
--------

-  fluent python
-  python3 面向对象编程
-  Python为什么要使用描述符？
   https://juejin.im/post/5cc4fbc0f265da0380437706

.. raw:: html

   <center>

分享快乐,留住感动. ‘2019-10-06 15:46:15’ –frank

.. raw:: html

   </center>
