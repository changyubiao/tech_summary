

[TOC]





# 保持盲目的一致是头脑简单的表现

(A Foolish Consistency Is The Hobgoblin Of Little Minds)

Guido的一个重要观点是代码被读的次数远多于被写的次数。这篇指南旨在提高代码的可读性，使浩瀚如烟的Python代码风格能保持一致。正如[PEP 20](https://www.python.org/dev/peps/pep-0020)那首《Zen of Python》的小诗里所说的：“可读性很重要(Readability counts)”。

这本风格指南是关于一致性的。同风格指南保持一致性是重要的，但是同项目保持一致性更加重要，同一个模块和一个函数保持一致性则最为重要。

然而最最重要的是：要知道何时去违反一致性，因为有时风格指南并不适用。当存有疑虑时，请自行做出最佳判断。请参考别的例子去做出最好的决定。并且不要犹豫，尽管提问。

特别的：千万不要为了遵守这篇PEP而破坏向后兼容性！

如果有以下借口，则可以忽略这份风格指南：

1. 当采用风格指南时会让代码更难读，甚至对于习惯阅读遵循这篇PEP的代码的人来说也是如此。
2. 需要和周围的代码保持一致性，但这些代码违反了指南中的风格（可是时历史原因造成的）——尽管这可能也是一个收拾别人烂摊子的机会（进入真正的极限编程状态）。
3. 若是有问题的某段代码早于引入指南的时间，那么没有必要去修改这段代码。
4. 代码需要和更旧版本的Python保持兼容，而旧版本的Python不支持风格指南所推荐的特性。





## Python风格规范



## 分号

**不要**在行尾加分号, 也不要用分号将两条命令放在同一行.

```python
import sys;import os ;

# 不要像下面一样写在一行
import sys, os
```



## 空行

顶级定义之间空两行,  方法定义之间空一行

顶级定义之间空两行, 比如函数或者类定义. 方法定义, 类定义与第一个方法之间, 都应该空一行. 

函数或方法中, 某些地方要是你觉得合适, 就空一行.



## 代码布局(Code Lay-Out)



### 缩进(Indentation)



每个缩进级别采用4个空格。

连续行所包装的元素应该要么采用Python隐式续行，即垂直对齐于圆括号、方括号和花括号，要么采用悬挂缩进(hanging indent)。采用悬挂缩进时需考虑以下两点：第一行不应该包括参数，并且在续行中需要再缩进一级以便清楚表示。

**正确**的例子:

```python
# 同开始分界符(左括号)对齐
foo = long_function_name(var_one, var_two,
                         var_three, var_four)

# 续行多缩进一级以同其他代码区别
def long_function_name(
        var_one, var_two, var_three,
        var_four):
    print(var_one)

# 悬挂缩进需要多缩进一级
foo = long_function_name(
    var_one, var_two,
    var_three, var_four)
```

错误的例子:

```python
# 采用垂直对齐时第一行不应该有参数
foo = long_function_name(var_one, var_two,
    var_three, var_four)

# 续行并没有被区分开，因此需要再缩进一级
def long_function_name(
    var_one, var_two, var_three,
    var_four):
    print(var_one)
```

对于续行来说，4空格的规则可以不遵守。



### 每行最大长度(Maximum Line Length)

将所有行都限制在79个字符长度以内。

一些团队会强烈希望行长度比79个字符更长。当代码仅仅只由一个团队维护时，可以达成一致让行长度增加到80到100字符(实际上最大行长是99字符)，注释和文档字符串仍然是以72字符换行。

Python标准库比较传统，将行长限制在79个字符以内（文档字符串/注释为72个字符）。

一种推荐的换行方式是利用Python圆括号、方括号和花括号中的隐式续行。长行可以通过在括号内换行来分成多行。应该最好加上反斜杠来区别续行。



**例外情况**： 

1. 长的导入模块语句
2. 注释里的URL





如果一个文本字符串在一行放不下, 可以使用圆括号来实现隐式行连接:


  使用括号 

```
x = ('This will build a very long long '
     'long long long long long long string')
```



在注释中，如果必要，将长的URL放在一行上。

```python
Yes:  # See details at
      # http://www.example.com/us/developer/documentation/api/content/v2.0/csv_file_name_extension_full_specification.html

No:  # See details at
     # http://www.example.com/us/developer/documentation/api/content/\
     # v2.0/csv_file_name_extension_full_specification.html
```





```python
with open('/path/to/some/file/you/want/to/read') as file_1, \
     open('/path/to/some/file/being/written', 'w') as file_2:
    file_2.write(file_1.read())
```





### 二元运算符之前还是之后换行？

(Should a line break before or after a binary operator?)



```python
# 错误的例子：运算符远离操作数
income = (gross_wages +
          taxable_interest +
          (dividends - qualified_dividends) -
          ira_deduction -
          student_loan_interest)
```



建议写法 ： 

```python
# 正确的例子：更容易匹配运算符与操作数
income = (gross_wages
          + taxable_interest
          + (dividends - qualified_dividends)
          - ira_deduction
          - student_loan_interest)
```





## 源文件编码(Source File Encoding)

Python核心发行版中的代码应该一直使用UTF-8  .  python3 用 utf8 编码 







## 模块引用(Imports)

- 
  Imports应该分行写，而不是都写在一行，例如：

  

  ```python
  # 分开写
  import os
  import sys
  
  # 不要像下面一样写在一行
  import sys, os
  ```

这样写也是可以的：

```python
from subprocess import Popen, PIPE
```

- Imports应该写在代码文件的开头，位于模块(module)注释和文档字符串(docstring)之后，模块全局变量(globals)和常量(constants)声明之前。

  Imports应该按照下面的顺序分组来写：

  1. 标准库imports
  2. 相关第三方imports  (从pypi 下载的)
  3. 本地应用/库的特定imports  (自己写的)

  不同组的imports之前用空格隔开。

- 推荐使用绝对(absolute)imports，因为这样通常更易读，在import系统没有正确配置（比如中的路径以`sys.path`结束）的情况下，也会有更好的表现（或者至少会给出错误信息）：

```python
import mypkg.sibling
from mypkg import sibling
from mypkg.sibling import example
```

- 隐式的相对imports应该**永不**使用，并且Python 3中已经被去掉了。

- 

- 当从一个包括类的模块中import一个类时，通常可以这样写：

  ```
  from myclass import MyClass
  from foo.bar.yourclass import YourClass
  ```

  如果和本地命名的拼写产生了冲突，应当直接import模块：

  ```
  import myclass
  import foo.bar.yourclass
  ```

  然后使用”myclass.MyClass”和”foo.bar.yourclass.YourClass”。

- 避免使用通配符imports(`from <module> import  *`)，因为会造成在当前命名空间出现的命名含义不清晰，给读者和许多自动化工具造成困扰。有一个可以正当使用通配符import的情形，即将一个内部接口重新发布成公共API的一部分（比如，使用备选的加速模块中的定义去覆盖纯Python实现的接口，预先无法知晓具体哪些定义将被覆盖）。







## 字符串引用(String Quotes)

在Python中表示字符串时，不管用单引号还是双引号都是一样的。但是不推荐将这两种方式看作一样并且混用。最好选择一种规则并坚持使用。当字符串中包含单引号时，采用双引号来表示字符串，反之也是一样，这样可以避免使用反斜杠，代码也更易读。

对于三引号表示的字符串，使用双引号字符来表示，这样可以和[PEP 257](https://www.python.org/dev/peps/pep-0257)的文档字符串（docstring）规则保持一致。



在同一个文件中, 保持使用字符串引号的一致性. 使用单引号`'`或者双引号`"`之一用以引用字符串, 并在同一文件中沿用. 





为多行字符串使用三重双引号`"""` 

文档字符串必须使用三重双引号`"""` 



## 文件和sockets


  除文件外, sockets或其他类似文件的对象在没有必要的情况下打开, 会有许多副作用, 例如:

1. 它们可能会消耗有限的系统资源, 如文件描述符. 如果这些资源在使用后没有及时归还系统, 那么用于处理这些对象的代码会将资源消耗殆尽.
2. 持有文件将会阻止对于文件的其他诸如移动、删除之类的操作.
3. 仅仅是从逻辑上关闭文件和sockets, 那么它们仍然可能会被其共享的程序在无意中进行读或者写操作. 只有当它们真正被关闭后, 对于它们尝试进行读或者写操作将会抛出异常, 并使得问题快速显现出来.

而且, 幻想当文件对象析构时, 文件和sockets会自动关闭, 试图将文件对象的生命周期和文件的状态绑定在一起的想法, 都是不现实的. 因为有如下原因:

1. 没有任何方法可以确保运行环境会真正的执行文件的析构. 不同的Python实现采用不同的内存管理技术, 比如延时垃圾处理机制. 延时垃圾处理机制可能会导致对象生命周期被任意无限制的延长.
2. 对于文件意外的引用,会导致对于文件的持有时间超出预期(比如对于异常的跟踪, 包含有全局变量等).



对于打开的文件 ，建议用 with 语句 。



推荐使用 [“with”语句](http://docs.python.org/reference/compound_stmts.html#the-with-statement) 以管理文件:

```
with open("hello.txt") as hello_file:
    for line in hello_file:
        print line
```

对于不支持使用”with”语句的类似文件的对象,使用 contextlib.closing():

```python
import contextlib

with contextlib.closing(urllib.urlopen("http://www.python.org/")) as front_page:
    for line in front_page:
        print line
```









## 命名



module_name, package_name, ClassName, method_name, ExceptionName, function_name, GLOBAL_VAR_NAME, instance_var_name, function_parameter_name, local_var_name.



**应该避免的名称**

> 1. 单字符名称, 除了计数器和迭代器.
> 2. 包/模块名中的连字符(-)
> 3. 双下划线开头并结尾的名称(Python保留, 例如__init__)



**命名约定**

> 1. 所谓”内部(Internal)”表示仅模块内可用, 或者, 在类内是保护或私有的.
> 2. 用单下划线(_)开头表示模块变量或函数是protected的(使用from module import *时不会包含).
> 3. 用双下划线(__)开头的实例变量或方法表示类内私有.
> 4. 将相关的类和顶级函数放在同一个模块里. 不像Java, 没必要限制一个类一个模块.
> 5. 对类名使用大写字母开头的单词(如CapWords, 即Pascal风格), 但是模块名应该用小写加下划线的方式(如lower_with_under.py). 尽管已经有很多现存的模块使用类似于CapWords.py这样的命名, 但现在已经不鼓励这样做, 因为如果模块名碰巧和类名一致, 这会让人困扰.





**Python之父Guido推荐的规范**

| Type                       | Public             | Internal                                                     |
| -------------------------- | ------------------ | ------------------------------------------------------------ |
| Modules                    | lower_with_under   | _lower_with_under                                            |
| Packages                   | lower_with_under   |                                                              |
| Classes                    | CapWords           | _CapWords                                                    |
| Exceptions                 | CapWords           |                                                              |
| Functions                  | lower_with_under() | _lower_with_under()                                          |
| Global/Class Constants     | CAPS_WITH_UNDER    | _CAPS_WITH_UNDER                                             |
| Global/Class Variables     | lower_with_under   | _lower_with_under                                            |
| Instance Variables         | lower_with_under   | _lower_with_under (protected) or __lower_with_under (private) |
| Method Names               | lower_with_under() | _lower_with_under() (protected) or __lower_with_under() (private) |
| Function/Method Parameters | lower_with_under   |                                                              |
| Local Variables            | lower_with_under   |                                                              |





## Main 函数

即使是一个打算被用作脚本的文件, 也应该是可导入的. 并且简单的导入不应该导致这个脚本的主功能(main functionality)被执行, 这是一种副作用. 主功能应该放在一个main()函数中.



在Python中, pydoc以及单元测试要求模块必须是可导入的. 

你的代码应该在执行主程序前总是检查 `if __name__ == '__main__'` , 这样当模块被导入时主程序就不会被执行.

```python
def main():
    ...
	pass
	
if __name__ == '__main__':
    main()
```

所有的顶级代码在模块导入时都会被执行. 要小心不要去调用函数, 创建对象, 或者执行那些不应该在使用pydoc时执行的操作.







## 最后 个人一些小建议 

1. 不要隐士导入包  

```python 
from sqlalchemy import * 
```

2. 命名 尽量不要和 内置的库，模块 一样 

比如下面的命名： 

```reStructuredText
math.py    operators.py    heapq.py    copy.py 
```

​	因为 你的名字如果和这些内置的一样，有时候 你想导入 自己的模块，发现导入的是 标准库的模块。 当然 这个python解释器 如何查找库的顺序 有关。








参考文档 

上面的这些 都来自 下面的 文档,几乎 没有做过改动。

[Python PEP-8编码风格指南中文版](https://alvinzhu.xyz/2017/10/07/python-pep-8/)  

[PEP-8- Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)

[Python 风格指南](https://zh-google-styleguide.readthedocs.io/en/latest/google-python-styleguide/contents/)



