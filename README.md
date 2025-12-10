# 多模态自动驾驶项目
## 按照这个办法创建初始环境
```python
    conda create -n cv_proj python=3.10 -y  # 创建环境
    python -m pip install --upgrade pip  # 更新pip
    pip install torch==2.3.0 torchvision==0.18.0 torchaudio==2.3.0 --index-url https://download.pytorch.org/whl/cu121
    pip install -r requirements.txt
```
## 本地没有库？
准备一个谷歌邮箱，负责人将会通过Github给你发送团队协作邮件，你同意协作后，就可以拥有这个工程的开发权限
如果项目崩溃，及时联系负责人回溯。或者自己找到一个正确的版本，学习一下怎么新开一个分支branch以及合并（Pull Request）

+ 注意：不要在工程目录下放置.pth这样的超大文件（500mb以上），你可以设定这些生成的文件到自己计算机的无关目录下
+ 千万不要提交超大文件，可能导致仓库被冻结，也有可能无法上传

（如果你熟练使用Git，可以直接用指令，而不用Github Desktop）
### 为了保证我们能够一起推进项目、方便合并与测试，我们需要事先约定一下简单的流程：
### 重点：标准工作流程：（假设你已经本地有了库）
+ 1、打开Github Desktop 点击上方的Fetch Origin从远程同步代码
+ 2、使用anaconda prompt中pip install --upgrade -r requirements.txt同步环境
+ 3、开始工作
+ 4、结束工作
+ 5、（如有）安装了包，则更新requirements.txt，标明版本（如果安装一个包a，还有依赖包a1 a2 a3，假如依赖是自动安装的，那就不需要标，因为我们装的时候也会自动安装依赖）
+ 6、打开Github Desktop，点击Change栏目，写下summary并点击下方蓝色commit按钮提交，最后点击Fetch Origin提交远程

+ 推荐本地安装一个vscode，方便解决代码冲突
什么是代码冲突？你更改了文件a的某一行，但是另一个人删除了你修改的这一行，你们都提交了代码，那么后提交的人会出来一个冲突
Github Desktop会识别到冲突，并阻止提交。此时弹出的窗口中，你可以通过vscode浏览到冲突，并选择到底是删除还是更改，把冲突解决就可以提交
