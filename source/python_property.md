# python3中的特性property介绍  


[TOC]


python 中的 特性 是什么?  

与属性的区别 是什么 ? 

在python 中 属性 这个  实例方法 , 类变量 都是属性.
属性, attribute 

在python 中  数据的属性 和处理数据的方法 都可以叫做 属性.
简单来说 在一个类中, 方法是属性, 数据也是属性 .

```python

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
```

在命令行里面执行
```python
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
```
可以看出`#1` animal 中 是可以拿到 add ,sleep  bark 这些属性的.





特性: property  这个是指什么?    在不改变类接口的前提下使用
存取方法 (即读值和取值) 来修改数据的属性 .

什么意思呢? 

就是通过 obj.property  来读取一个值, 
obj.property = xxx ,来赋值 


还以上面 animal 为例: 


```python

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
        
```


这个时候 name 就是了特性了.

```
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
```
肯定有人会疑惑,写了那么多的代码, 还不如直接写成属性呢,多方便.


比如这段代码:
直接把name 变成类属性 这样做不是很好吗,多简单. 这样写古人也没有太大的问题.但是 如果给name 赋值成数字 这段程序也是没有任何问题..  这就是比较大的问题了.
```
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
```






```python
animal= Animal()
animal.name=100
property set name 
Traceback (most recent call last):
  File "<input>", line 1, in <module>
  File "<input>", line 13, in name
ValueError: expected val is str
```

 其实当name 变成了property  之后,我们就可以对name 赋值 进行控制. 防止一些非法值变成对象的属性. 
比如说name 应该是这个字符串, 不应该是数字 这个时候 就可以在   setter 的时候 进行判断,来控制 能否赋值.

要实现上述的效果, 其实也很简单 setter 对value进行判断就好了.

```
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

```


感受到 特性的魅力了吧 ,可以通过 赋值的时候 ,对 值进行校验,方式不合法的值,进入到对象的属性中.  下面 看下 如何设置只读属性, 和如何设置读写 特性.


> 假设 有这个的一个需求 , 某个 类的属性一个初始化之后 就不允许 被更改,这个 就可以用特性这个问题 , 比如一个人身高是固定, 一旦 初始化后,就不允许改掉. 

## 设置只读特性 
```python

class Frank:
    def __init__(self, height):
        self._height = height

    @property
    def height(self):
        return self._height

```



```
>>> frank = Frank(height=100)
>>> frank.height
100
>>> frank.height =150
Traceback (most recent call last):
  File "<input>", line 1, in <module>
AttributeError: can't set attribute
```
这里初始化 frank后 就不允许 就修改 这个 height 这个值了.  (实际上也是可以修改的)
重新 给 height 赋值就会报错, 报错 AttributeError ,这里 不实现 setter 就可以了.



## 设置 读写 特性 

```python

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

```


```python
>>> 
>>> frank = Frank(height=100)
>>> frank.height
100
>>> frank.height=165
>>> frank.height
165
```



> 比如对人的身高 在1米 到 2米之间 这样的限制
## 对特性的合法性进行校验

```python
    
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


```
在python console 里面测试 结果:
```python

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
```

这样 就可以 进行严格的控制, 一些特性的方法性 ,通过写setter 方法 来保证数据 准确性,防止一些非法的数据进入到实例中.




## property  是什么? 

实际是一个类 , 然后 就是一个装饰器. 让一个 方法 变成 一个特性. 
假设 某个类的实例方法 bark 被 property 修饰了后,  调用方式就会发生变化.
```
obj.bark() --> obj.bak 
```







一旦确定了 属性不是动作 , 我们需要在标准属性 和 property  之间做出选择 . 

一般来说 你如果要控制 property 的 访问过程,就要用 property . 否则用标准的属性 即可 . 


属性 和  property 的区别 在于 当property 被读取, 赋值, 删除时候, 自动会执行 某些 特定的动作.






property 是一个装饰器,



## 装饰器的两种写法 
```python

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
    
```



```
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
```






- 常见的一些例子  

1. 缓存某些值 
2. 对一些值 进行合法性校验.
3. 





### 缓存一些值

```
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
```

可以看出 第一次调用了 urlopen 从网页中读取值, 第二次就没有调用urlopen 而是直接返回content 的内容.