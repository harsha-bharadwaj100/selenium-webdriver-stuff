from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Set your YouTube credentials
username = "harshabharadwaj01092004@gmail.com"
password = "600600hb"

# Set the YouTube video URL and the comment you want to post
video_url = "https://www.youtube.com/watch?v=31oxj6mcsOM"
comment_text = "Cool Video"

# Initialize the WebDriver (make sure you have the appropriate driver for your browser installed)
driver = webdriver.Chrome(r'D:\python programs\selenium webdriver stuff\chromedriver-win64\chromedriver.exe')

# Open YouTube
driver.get("https://www.youtube.com/")

# Find the "Sign In" button and click it
sign_in_button = driver.find_element_by_link_text("Sign in")
sign_in_button.click()

# Enter the username and password in the login form
username_field = driver.find_element_by_id("identifierId")
username_field.send_keys(username)
username_field.send_keys(Keys.RETURN)

time.sleep(2)  # Wait for the page to load

password_field = driver.find_element_by_name("password")
password_field.send_keys(password)
password_field.send_keys(Keys.RETURN)

time.sleep(5)  # Wait for the login to complete

# Open the video URL
driver.get(video_url)

time.sleep(3)  # Wait for the video page to load

# Scroll down to the comment section
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(3)  # Wait for the page to scroll

# Find the comment box and enter your comment
comment_box = driver.find_element_by_xpath('//*[@id="simplebox-placeholder"]')
comment_box.send_keys(comment_text)

# Find the comment submit button and click it
comment_submit_button = driver.find_element_by_xpath('//*[@id="submit-button"]')
comment_submit_button.click()

time.sleep(3)  # Wait for the comment to be posted

# Close the browser
driver.quit()
