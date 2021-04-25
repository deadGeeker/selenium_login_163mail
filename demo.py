#  自动化测试用例：登录网易邮箱，验证登录功能
#  编写用例：
#  用例编号：1
#  测试点：登录成功
#  执行步骤：输入用户账号、输入账号密码、点击登录按钮
#  预期效果：登陆成功

from selenium import webdriver


# 实例化一个chrome对象
driver = webdriver.Chrome()
# 登录网易邮箱
driver.get("https://mail.163.com")

# 定位登录框元素，整个登录框元素在iframe标签内，
# iframe标签相当于在HTML标签内嵌入一个HTML文件，
# 需要先跳转到iframe标签才能定位登录框元素
iframe = driver.find_element_by_xpath('//*[@id="loginDiv"]/iframe')
driver.switch_to.frame(iframe)

# 定位账号输入框元素
account_path = '//*[@id="account-box"]/div[2]/input'
driver.find_element_by_xpath(account_path).send_keys("123")

# 定位密码输入框元素
passwd_path = '//*[@id="login-form"]/div[1]/div[3]/div[2]/input[2]'
driver.find_element_by_xpath(passwd_path).send_keys("123")

# 定位登录按钮元素
login_path = '//*[@id="dologin"]'
driver.find_element_by_xpath(login_path).click()

# 切换出iframe框架
driver.switch_to.default_content()
