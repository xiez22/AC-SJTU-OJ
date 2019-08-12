from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

# Hyper Parameters
SLEEP_TIME = 3

print('题目跟踪器，跟踪OJ上别人刷的题目')
username = input('您的用户名：')
password = input('您的密码：')
problem_to_solve = None

option = webdriver.ChromeOptions()
browser = webdriver.Chrome(options=option)

last_code = None

print('正在登录...')
browser.get("https://acm.sjtu.edu.cn/OnlineJudge")
input_username = browser.find_element(By.NAME, 'username')
input_password = browser.find_element(By.NAME, 'password')
btn_login = browser.find_element(By.NAME, 'action')

actions = ActionChains(browser)
actions.send_keys_to_element(input_username, username)
actions.send_keys_to_element(input_password, password)
actions.click(btn_login)
actions.perform()

print('登录成功！')

while True:
    try:
        browser.get('https://acm.sjtu.edu.cn/OnlineJudge/status#')
        while True:
            time.sleep(SLEEP_TIME)
            browser.refresh()
            print('获取最新提交编号......')
            cur_code = browser.find_element(
                By.XPATH, '//*[@id="status"]/tbody/tr[1]/td[1]/a').text
            if last_code != cur_code:
                last_code = cur_code
                user_submit: str = browser.find_element(
                    By.XPATH, '//*[@id="status"]/tbody/tr[1]/td[2]').text
                [user_id, _] = user_submit.split()
                if user_id == username:
                    print('无新的提交')
                    continue
                problem_to_solve = browser.find_element(
                    By.XPATH, '//*[@id="status"]/tbody/tr[1]/td[3]/a[1]').text
                print('找到新的提交，题号是', problem_to_solve)
                break
            else:
                print('无新的提交')

        print("正在获取代码......")
        browser.get(
            'https://raw.githubusercontent.com/ligongzzz/SJTU-OJ/master/Code/Project'
            + problem_to_solve + '/Project' + problem_to_solve + '/源.cpp')
        print('代码获取成功！')
        code_to_input = browser.find_element_by_xpath('/html/body/pre').text
        print(code_to_input)

        print('正在提交代码......')

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

        print('提交完成')

        browser.refresh()

    except:
        print('抱歉！出现错误')
