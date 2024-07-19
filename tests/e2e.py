from selenium import webdriver
from selenium.webdriver.common.by import By
import sys


def test_score_service(url):
    driver = webdriver.Firefox()
    driver.implicitly_wait(5)
    driver.get(url)
    score = driver.find_element(By.ID, 'score').text
    driver.quit()
    return 0 if score == '4' else -1


def main_function():
    if len(sys.argv) != 2:
        print("Usage: python test.py <url>")
        sys.exit(-1)
    sys.exit(test_score_service(sys.argv[1]))


if __name__ == "__main__":
    main_function()