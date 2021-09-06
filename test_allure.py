import pytest
import allure
from selenium import webdriver

class TestReport():
    def test_success(self):
        """this test succeeds"""
        assert True


    def test_failure(self):
        """this test fails"""
        assert False


    def test_skip(self):
        """this test is skipped"""
        pytest.skip('for a reason!')


    def test_broken(self):
        raise Exception('oops')

@allure.feature("登录模块")
class TestAllure():

    @allure.story("用户名密码正确")
    def test_login_success(self):
        with allure.step("输入用户名"):
            print("登录成功")

    @allure.story("密码缺失")
    def test_login_fail(self):
        with allure.step("密码为空"):
            print("登录失败")

    @allure.link("http://www.baidu.com",name="百度")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_link(self):
        print("测试用例报告中添加链接")

    test_case_link ="http://www.baidu.com"
    @allure.testcase(test_case_link, name="百度用例")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_case_link(self):
        print("测试用例链接")

    # 1 是问题的id, 在运行时再传入issue的链接：--allure-link-pattern=issue:http://www.baidu.com
    @allure.issue('1',name="这是一个bug")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_issue(self):
        print("这是一个bug")

    # 添加文本信息
    def test_attach_text(self):
        allure.attach("这是一个text文本", attachment_type=allure.attachment_type.TEXT)

    # 添加图片
    def test_attach_image(self):
        source = "E:\study\Python\pycharm\pythonProject\First_time_unitest20210901\pytest\source_image\
        src=http___cdn.duitang.com_uploads_item_201202_18_20120218194349_ZHW5V.thumb.700_0.jpg&refer=http___cdn.duitang.jpg"
        allure.attach.file(source=source, name="这是一个图片",attachment_type=allure.attachment_type.JPG)

    # 添加html
    def test_attach_html(self):
        body = "<body>这是一个html body</body>"
        allure.attach(body=body, attachment_type=allure.attachment_type.HTML)



def test_baidu_search():
    driver = webdriver.chrome
    driver.get("http://www.baidu.com")



if __name__ == '__main__':
    pytest.main()
