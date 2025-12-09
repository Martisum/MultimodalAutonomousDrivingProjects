如何创建初始环境？
    conda create -n cv_proj python=3.10 -y  # 创建环境
    python -m pip install --upgrade pip  # 更新pip
    pip install torch==2.3.0 torchvision==0.18.0 torchaudio==2.3.0 --index-url https://download.pytorch.org/whl/cu121
    pip install -r requirements.txt

标准工作流程：（假设你已经本地有了库）
1、打开Github Desktop 点击上方的Fetch Origin从远程同步代码
2、使用anaconda prompt中pip install --upgrade -r requirements.txt同步环境
3、开始工作
4、结束工作
5、（如有）安装了包，则更新requirements.txt，标明版本
6、打开Github Desktop，点击Change栏目，写下summary并点击下方蓝色commit按钮提交，最后点击Fetch Origin提交远程


