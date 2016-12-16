# A Simple PortScanner



> 在轮子上造轮子


## 简介

尝试以优美的Python语法来写一个简易而顺手的端口扫描器。

## 用法

```python
python3 pscaner.py -h

Usage: python pscaner.py -t <host> -p <port>

Options:
  --version             show program's version number and exit
  -h, --help            show this help message and exit
  -t TARGET_HOST, --target=TARGET_HOST
                        specify target host(s)
  -p TARGET_PORT, --port=TARGET_PORT
                        <port ranges>: Only scan specified ports
  --thread=THREAD       specify thread count
```

默认线程是30， 若不指定端口，将扫描最常见的几十个端口

端口指定支持两种方式： 
+ 10-100
+ 100, 200, 300,


## 感谢

+ [https://github.com/OpenFireTechnologies/PortScanner](https://github.com/OpenFireTechnologies/PortScanner)
+ [https://github.com/chprice/PortScanner](https://github.com/chprice/PortScanner)

