#coding=utf-8

from selenium import webdriver
import sys
reload(sys)
sys.setdefaultencoding('utf8')

def Testlogin():
    driver = webdriver.Chrome()
    driver.get('http://127.0.0.1:9980/auth/login')
    title = driver.title
    print title
    now_url = driver.current_url
    print now_url
    username = 'mowuxue1989@163.com'
    password = 'test'
    driver.find_element_by_class_name("btn_login").click()
    driver.find_element_by_name("email").send_keys(username)
    driver.find_element_by_name("password").send_keys(password)
    driver.find_element_by_id("login").click()


if __name__ == "__main__":
    Testlogin()