### 前言
本次项目使用pycharm和selenium包  
来实现对指定网站-网易邮箱执行自动化登录测试
  
##### 环境搭建  
1. 导入selenium包  
  + 本人的pycharm是2020版，所以直接内部点击安装
 

2. 导入浏览器驱动   
  + 我的浏览器是chrome，所以选择安装chromedriver，
  + 这边我为各位提供一个资源路径http://chromedriver.storage.googleapis.com/index.html
  + 注意，一定要安装与你的浏览器版本对应的驱动包
  + 将下载解压后的驱动放置于“..\Python\Python38\Lib”  


##### 步骤实现  
1. 打开网易邮箱网站，进入开发者选项，点中登录框元素
  + 分析：整个登录框置于iframe标签下，所以在定位具体目标元素前应该先跳转到iframe框架中
  + 这里我们可以使用driver.switch_to.frame()方法  
  
2. 定位具体元素  
  + 定位账号登录框元素   
  + 定位密码登录框元素   
  + 定位登录按钮元素  
  + 在这里我使用的是用xpath的方法去定位，我曾经想过直接使用开发者工具去copy目标元素的xpath，  
  + 但是发现有随机id的存在，所以我这边只能手工写xpath  
   
3. 退出iframe框架  
  + 记得如果不再需要定位iframe框架中的元素，应该养成习惯在末尾添加driver.switch_to.default_content()
  + 来推出框架  

