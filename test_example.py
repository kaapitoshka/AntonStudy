import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@pytest.fixture(scope="session")
def driver(request):
	wd=webdriver.Chrome()
	request.addfinalizer(wd.quit)
	return wd
	
def test_admin_login(driver):
	driver.get("http://localhost/litecart/admin")
	driver.find_element_by_name("username").send_keys("admin")
	driver.find_element_by_name("password").send_keys("123456")
	driver.find_element_by_name("login").click()
	WebDriverWait(driver,10).until(EC.title_is("My Store"))
	print('Поставим sleep перед закрытием браузера на 5 секунд для отладки')
	time.sleep(5)
