# 上海交通大学OJ 自动AC程序
# 代码来自 ligongzzz SJTU-OJ仓库
# 仅供娱乐。

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

username = input('您的用户名：')
password = input('您的密码：')
problem_to_solve = input('您要解决哪道题：')

option = webdriver.ChromeOptions()
browser = webdriver.Chrome(options=option)

try:
    print("正在获取代码......")
    browser.get(
        'https://raw.githubusercontent.com/ligongzzz/SJTU-OJ/master/Code/Project'
        + problem_to_solve + '/Project' + problem_to_solve + '/源.cpp')
    print('代码获取成功！')
    code_to_input = browser.find_element_by_xpath('/html/body/pre').text
    print(code_to_input)

    browser.get("https://acm.sjtu.edu.cn/OnlineJudge")
    input_username = browser.find_element(By.NAME, 'username')
    input_password = browser.find_element(By.NAME, 'password')
    btn_login = browser.find_element(By.NAME, 'action')

    actions = ActionChains(browser)
    actions.send_keys_to_element(input_username, username)
    actions.send_keys_to_element(input_password, password)
    actions.click(btn_login)
    actions.perform()

    browser.get("https://acm.sjtu.edu.cn/OnlineJudge/submit")

    input_problem = browser.find_element(By.NAME, 'problem')
    input_code = browser.find_element(By.NAME, 'code')
    btn_submit = browser.find_element(
        By.XPATH, '//*[@id="wrap"]/div/form/fieldset/div[4]/button')

    actions = ActionChains(browser)
    actions.send_keys_to_element(input_problem, problem_to_solve)
    actions.send_keys_to_element(input_code, code_to_input)
    actions.click(btn_submit)
    actions.perform()

    browser.refresh()

    for _ in range(10):
        time.sleep(1)
        browser.refresh()
except:
    print('抱歉！出现错误')
finally:
    browser.close()
