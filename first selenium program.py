from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = r'C:\Users\INDIA\Downloads\chromedriver.exe'
driver = webdriver.Chrome(PATH)

driver.get("https://www.techwithtim.net")
print("title = ", driver.title)
print("type", type(driver))
search = driver.find_element_by_name("s")
search.send_keys("test")
search.send_keys(Keys.RETURN)

# wait for the page to load
try:
  main = WebDriverWait(driver, 10).until(
      EC.presence_of_element_located((By.ID, "main"))
  )
  print("Page is ready!")
  print("main = ", main.text)
  print("type", type(driver))
  articles = main.find_elements_by_tag_name("article")
  for article in articles:
    header = article.find_element_by_class_name("entry-summary")
    print(header.text)
    print("-" * 20)

finally:
  driver.quit()

# driver.close() # close the current tab
# 