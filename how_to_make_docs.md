


##如何生成文档


## 1 首先执行md2rst.py 脚本 , 把 md  --> rst 格式的文档

```bash

cd tech_summary

python  md2rst.py

```



### 2 执行sphinx 生成 html文档

```bash

cd tech_summary

# make  html
sphinx-build   -b html  source/    build/
```