import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
pytest.mark.tcid15
def test_get_text():
    driver = webdriver.Chrome()
    driver.get("http://mydemostore.local/")
    element = driver.find_element(By.CSS_SELECTOR, "h1.page-title")
    print("!!!!!!!!!!!!!")
    print(element.text)
    print("!!!!!!!!!!!!")