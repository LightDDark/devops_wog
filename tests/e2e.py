from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import sys


def test_score_service(url):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(5)
    driver.get(url)
    score = int(driver.find_element(By.ID, 'score').text)
    driver.quit()
    return 0 if 0 < score <= 1000 else -1


def main_function():
    if len(sys.argv) != 2:
        print("Usage: python e2e.py <url>")
        sys.exit(-1)
    sys.exit(test_score_service(sys.argv[1]))


if __name__ == "__main__":
    main_function()
