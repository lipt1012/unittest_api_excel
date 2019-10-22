# unittest_api
基于Unittest+Request的接口自动化开源框架

----
#### 模块类的设计

`config.py`读取配置文件，包括：不同环境的配置，email相关配置

`case_log.py` 封装记录log方法，分为：debug、info、warning、error、critical

`send_email.py`封装smtplib方法，运行结果发送邮件通知

`read_excel.py`读取excel数据

`basecase.py`封装接口

`log` 日志文件

`test` 测试用例

----

