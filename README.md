# Sample Raspberry Pi Chinese Chatbot
# 树莓派中文简易聊天机器人

# 使用需求
本软件尚未在树莓派上真实运行测试，如有bug请自行解决

系统：Ubuntu or Debian
运行环境：Python3
录音软件：arecord
播放软件：mpg123

### 设置运行环境 ###
1. 直接在真实环境中运行：
```bash
pip3 install -r requirement.txt
```

2. 在虚拟环境中运行：
```bash
python3 -m virtualenv env
source env/bin/activate
pip install -r requirements.txt
```

### 运行程序 ###
1. 在真实环境中：
```bash
python3 run.py
```

2. 在虚拟环境中：
```bash
python run.py
```