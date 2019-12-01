



[TOC]





# python3 中的上下文管理器



上下文管理器 是什么 

 只要 实现了   \_\_exit__  , \_\_enter__   的类 它就是上下文管理器. 它可以用来管理上下文 



实现了   \_\_exit__  , \_\_enter__    魔术 方法 的对象 可以使用 with 语句  

上下文表达式 返回一个 上下文管理器 







## 上下文管理的作用 和 目的 

上下文管理 对象 是为了存在的目的 是管理  with 语句, 而 with 语句  目的是为了 简化 tyr/ finally  这种模式  

这种 模式 保证  运行 一段代码后,  ,即便代码里面发生错误, return 语句或者调用 终止 sys.exit() , 也会执行特定的代码段, 来做一些最后的处理 , 比如 释放连接,  还原一些状态,释放资源等 . 









## 介绍   上下文管理器  协议  



 首先  要实现一个上下文管理 需要 实现两个 魔术方法    \__exit__  , \_\_enter__  , 即需要在一个类中



不管以哪种方式 退出 with 语句, 都会进行 \_\_enter__  方法里面的代码段 , 而不是 \_\_enter__ 返回对象的对象上调用 









下面 简单实现 一个 上下文管理器 

Resource 类中实现了两个魔术方法 , 同时实现了一个query  方法 



```python
# -*- coding: utf-8 -*- 

class Resource:

    def __enter__(self):
        print("connect to resource")
        return self
       

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("close resource  connection")

    def query(self):
        print("query  data ...")


with Resource() as r:
    r.query()


```



首先 Resource 实现了 这两个魔术方法 , 它就是一个上下文管理器 , 就可以使用with 这种语法 ,with 表达式后面一定要是一个 上下文管理器,才能够这样写. 





结果如下  :

![img1](https://note.youdao.com/yws/public/resource/3018b4aa1a30076e1a2fb610859b1058/xmlnote/2FA4C970BDC74C649560D4DD864DCD7A/47218)

整个代码的执行流程

可以看出 首先 执行的  _\_enter__  里面的代码段 , 后来 返回 self  , 然后执行 query  方法 , 最后 执行  _\_exit__ 魔术方法 .



这个就是最简单的上下文管理器了.



### enter 方法介绍 



你可能 会疑惑  为啥  _\_enter__  方法要返回 self ? 



这个例子中  返回 self   , 即返回 Resource 对象的实例  ,  然后通过 r.query 来调用 实例 方法 query  , 所以 这里是需要返回self  . 这里   \_\_enter__  方法 的返回值  , 

```python
with Resource() as r:pass 
```

就是这段代码as 后对应变量的值  ,  这里 命名为 r   它的值就是 self 



下面 在   \_\_enter__ 返回 frank ,之后打印r 来看一下 这个 值是什么 ? 

```python 
# -*- coding: utf-8 -*- 

class Resource:

    def __enter__(self):
        print("connect to resource")
        return "frank"
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("close resource  connection")

    def query(self):
        print("query  data ...")


with Resource() as r:
    print(f"r:{r}")

```

结果如下:

![img2](https://note.youdao.com/yws/public/resource/3018b4aa1a30076e1a2fb610859b1058/xmlnote/37C088C4D6F54993AA87EDED7A619448/47226)



现在 应该理解 为啥要 返回 self了吧 .     一般 情况下 _\_enter__  方法会返回 self  ,  当然 也可以不返回 .

如果实在不需要返回 , 也可以不返回 . 

只要   明白   只要执行 with 这种里面的 代码段 首先 是先执行 \__enter__ 方法  里面 的代码即可. 





### exit 方法介绍 



\_\_exit__ 方法 实在with 里面 代码段执行完后 , 执行的方法 ,一般就是 资源清理的代码,会写在这里, 还有一些异常处理的代码,也可以写在这里. 



注意到 上面  方法 有 三个参数 , 这三个参数 只有 with  语句报错后, 这几个参数 才会有值,  如果with 代码段里面 没有报错 那么 这个三个值 均为  None  

exc_type  异常类

exc_value 异常值

exc_tb     traceback 对象 





```python
# -*- coding: utf-8 -*- 

class Resource:

    def __enter__(self):
        print("connect to resource")
        return "frank"
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        """

        :param exc_type: 异常类
        :param exc_val: 异常值
        :param exc_tb:  traceback 对象
        :return:
        """
        print(exc_type,exc_val,exc_tb)
        print("close resource  connection")

    def query(self):
        print("query  data ...")


with Resource() as r:

    1/0
    print(f"r:{r}")
```



在with 语句 故意抛出一个异常 可以看出 这三个值 .

![img3](https://note.youdao.com/yws/public/resource/3018b4aa1a30076e1a2fb610859b1058/xmlnote/B2C67A94C4A54D808EFD893FDE90F84D/47228)



![img4](https://note.youdao.com/yws/public/resource/3018b4aa1a30076e1a2fb610859b1058/xmlnote/95A0B7F230E04CEF8922ED21B554A1C7/47231)

可以看出 程序就报错了, 并且异常被抛出来 了. 



刚刚在 \_\_exit__ 方法 里面 其实 是可以处理 这种异常的, 保证 程序可以正常执行.  

可以通过 exc_tb 是否为空  来处理这个异常, 然后 注意这个时候要返回一个True , 这里的意思是 程序 异常已经处理, 不继续抛出到主 程序了. 

```python
# -*- coding: utf-8 -*- 

class Resource:

    def __enter__(self):
        print("connect to resource")
        return "frank"
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        """

        :param exc_type: 异常类
        :param exc_val: 异常值
        :param exc_tb:  traceback 对象
        :return: True or False
        """
        if exc_tb:
            print("catch exception .  deal exception")
            return True
        print("close resource  connection")

    def query(self):
        print("query  data ...")


with Resource() as r:

    1/0
    print(f"r:{r}")

```



执行结果如下:

![img5](https://note.youdao.com/yws/public/resource/3018b4aa1a30076e1a2fb610859b1058/xmlnote/7DE3A36BF55245619B144F2D32CD0B87/47233)



这里 \_\_enter__ 方法 返回值, 决定 是否要将 异常抛出来

\_\_exit__  这个方法 用来 上下文管理器退出执行的方法, 如果 有异常,  可以在这里处理,并且返回True, 则异常就不会被抛出来, 如果返回false 异常就会被抛出来. 有主程序 处理该异常.









## 上下文管理 用法 



1 常用的示例 

- 比如数据连接 以及关闭的操作 

一般连接数据库 需要以下步骤 

 数据库连接, 管理

     1 连接数据库

     2 exectue  sql

     3 释放连接 con.close()



```python
try:
  pass
except:
  pass
finally:
  pass
```



比如 可以 像下面的的例子 

来实现一个上下文管理器 

```python 
# -*- coding: utf-8 -*-

import pymysql


class ConnText:

    def __enter__(self):
        print("begin db connection")
        self.conn = self.get_connection()
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def get_connection(self):
        conn = pymysql.connect()
        return conn

    def close(self):
        self.conn.close()
        print("close db connection")

    def query(self):
        print("query data")


with ConnText() as r:
    r.query()

```





- 文件读写  也可以用上下文管理器

   一般打开文件后 最后 都需要关闭 文件句柄, 这个时候就可以使用上下文管理了. 

```python
with open('/tmp/1.sql') as f
  pass

```







## 框架里面使用

其实在很多源码中也可以看到上下文管理器的用法 , 

比如celery  核心对象 Celery 也实现了上下文管理 器 

代码位于:

	python3.x/site-packages/celery/app/base.py



![img7](https://note.youdao.com/yws/public/resource/3018b4aa1a30076e1a2fb610859b1058/xmlnote/FB24171B981243DCB42192810B1FC1B5/47235)





在flask 框架里面 用了很多上下文管理,比如这个模块 

/python3.x/site-packages/flask/ctx.py

`RequestContext` ,  `AppContext`    这两个类 都实现了  上下文 的管理器的协议 



![img7](https://note.youdao.com/yws/public/resource/3018b4aa1a30076e1a2fb610859b1058/xmlnote/C50833846E784B9FA34F288631AE5496/47243)



## 总结 
本文简单总结了 上下文管理器的语法,使用python 这种语法 可以写代码  看起来 更优雅一些, 更加的 pythonic.  有时候要学会看源代码来学习. 

