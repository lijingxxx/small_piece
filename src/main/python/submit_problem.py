#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
#实例化谷歌设置
option = webdriver.ChromeOptions()
#添加谷歌登陆数据(chrome://version/的"个人资料路径")
option.add_argument('user-data-dir=/Users/chenming/Library/Application\ Support/Google/Chrome/Default')
#打开chrome
browser = webdriver.Chrome(chrome_options=option)
# browser = webdriver.Firefox()
# browser.get('http://redmine.meizu.com/projects/llq/issues/new')
browser.get('https://www.baidu.com/')

subject_value = ''
contents_value = ''
members_picker_value = ''
upload_path = '/data/upload'
files = os.listdir(upload_path)
# 填写主题
subject = browser.find_element_by_id('issue_subject')
subject.send_keys(subject_value)
# 填写步骤
contents = browser.find_element_by_class_name('wiki cke_editable cke_editable_themed cke_contents_ltr cke_show_borders')
contents.send_keys(contents_value)

if len(files) > 0:
    for file in files:
        f = os.path.join(upload_path, file)
        contents.send_keys(f)
        os.remove(f)

# 指派人
members_picker = browser.find_element_by_id('s2id_issue_assigned_to_id')
members_picker.send_keys(members_picker_value)
members_picker.send_keys(Keys.ENTER)

# search = browser.find_element_by_id('kw')
# search.send_keys('python')
# search.send_keys(Keys.ENTER)

# level = '低'
# priority = browser.find_element_by_id('s2id_issue_priority_id')
# custom = browser.find_element_by_id('s2id_issue_custom_field_values_2')
# if level == '低':
#     pass
# elif level == '普通':
#     priority.send_keys('普通')
#     priority.send_keys(Keys.Enter)
# elif level == '高':
#     priority.send_keys('高')
#     priority.send_keys(Keys.Enter)
#     custom.send_keys('严重')
#     custom.send_keys(Keys.ENTER)
# else:
#     priority.send_keys('紧急')
#     priority.send_keys(Keys.Enter)
#     custom.send_keys('阻塞')
#     custom.send_keys(Keys.ENTER)
#
# category = browser.find_element_by_id('s2id_issue_category_id')
# category.send_keys('浏览器')
# category.send_keys(Keys.DOWN)
# category.send_keys(Keys.ENTER)
#
# target_version = browser.find_element_by_id('s2id_issue_fixed_version_id')
# target_version.send_keys('7.10.0')
# target_version.send_keys(Keys.ENTER)
#
# app_version = browser.find_element_by_id('s2id_autogen62')
# app_version.send_keys(Keys.BACK_SPACE)
# app_version.send_keys('7.10.0')
# app_version.send_keys(Keys.ENTER)

#browser.quit()