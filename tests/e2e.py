from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()


def test_score_service(url):
    driver.implicitly_wait(5)
    driver.get(url)
    score = driver.find_element(By.ID, 'score').text
    return 0 if score == '4' else -1


def main_function():
    return test_score_service()