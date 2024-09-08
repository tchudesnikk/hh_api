import pytest
from src.user_setting import UserSetting

def test_create_new_object(custom_settings_template):
    user_setting = UserSetting.create_new_object(custom_settings_template['search_query'])
    assert user_setting.search_query == 'developer Python'
    assert user_setting.top_n == 10
    assert user_setting.salary == {'salary_min': 0, 'salary_max': 0}
    assert user_setting.keywords == []
    assert user_setting.area == ''

def test_add_top_n(custom_settings_template):
    user_setting = UserSetting.create_new_object(custom_settings_template['search_query'])
    user_setting.top_n = custom_settings_template['top_n']
    assert user_setting.top_n == 50

def test_add_salary(custom_settings_template):
    user_setting = UserSetting.create_new_object(custom_settings_template['search_query'])
    user_setting.salary = custom_settings_template['salary']
    assert user_setting.salary['salary_min'] == 10000
    assert user_setting.salary['salary_max'] == 15000

def test_empty_range_salary():
    user_setting = UserSetting('Python')
    user_setting.salary = ''
    assert user_setting.salary['salary_min'] == 0
    assert user_setting.salary['salary_max'] == 0

def test_add_keyword(custom_settings_template):
    user_setting = UserSetting.create_new_object(custom_settings_template['search_query'])
    user_setting.keywords = custom_settings_template['keywords']
    assert len(user_setting.keywords) == 4
    assert user_setting.keywords[0] == 'Python'

def test_del_keywords(custom_settings_template):
    user_setting = UserSetting(custom_settings_template['search_query'])
    user_setting.keywords = custom_settings_template['keywords']
    del user_setting.keywords
    assert user_setting.keywords == []

def test_add_area(custom_settings_template):
    user_setting = UserSetting.create_new_object(custom_settings_template['search_query'])
    user_setting.area = custom_settings_template['area']
    assert user_setting.area == 'Россия'
