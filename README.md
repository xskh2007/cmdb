# cmdbx
python
domo 登录：http://42.62.6.54:8001/index.html 
默认用户名admin ,密码1qaz.2wsx   默认用户名hequan,密码1qaz.2wsx   

默认admin有所有权限， hequan只能查看。


后台 登陆：http://42.62.6.54:8001/admin            可以登录后台修改hequan 的权限

github链接：https://github.com/hequan2017/cmdb


版本说明：
环境 python3.6.1 django 1.11.3   需要安装的模块为 django-suit，ansible, paramiko
服务器请yum按照  sshpass ，不然无法获取资产信息。



版本更新1.5
1 增加资产更新，分别为 添加 查看 修改 更新 删除。 可真实获取到服务器资产

版本更新1.4

1 增加命令行模式
2 增加历史命令记录


版本更新1.3

1 新增主机管理板块，采用模态对话框。
2 增加更新服务器时间板块，采用ansible-playbook ，需要安装 ansible模块。 操作的命令可以看hostinfo/ansible_api/cmd.yml文件

版本更新1.2

1 新增权限模块，采用admin自带的auth ，实现简单的权限管理。 
无添加权限的，看不见 添加板块 ，同时对权限进行判断， 无权限 打不可，显示 error界面。
2 根据权限 判断 是否为 管理员。


版本更新1.1.2 

1 修复了echarts 自适应更改大小。 
2 更换了admin，采用django-suit 界面更好看，中文化。 需要安装 django-suit 模块。 admin的 帐号密码是 admin 1qaz.2wsx http://42.62.6.54:8001/admin

版本更新1.1.1 

新增 图形化展示数据， 采用百度 echart 动态展示 数据。
