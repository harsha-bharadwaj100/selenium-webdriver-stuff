# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time

# PATH = r'C:\Users\INDIA\Downloads\chromedriver.exe'
# driver = webdriver.Chrome(PATH)

# # login to google
# driver.get("https://accounts.google.com/ServiceLogin?hl=en&passive=true&continue=https://www.google.com/&ec=GAZAmgQ")

# # find the email and password fields
# email = driver.find_element_by_id("Email")
# password = driver.find_element_by_id("Passwd")

# # enter the email and password
# email.send_keys("harshabharadwaj01092004@gmail.com")
# password.send_keys("600600hb")






from selenium import webdriver
print('Enter the gmailid and password')
gmailId, passWord =  map(str, "harshabharadwaj01092004@gmail.com 600600hb".split())
try:
	driver = webdriver.Chrome(r'C:\Program Files (x86)\chromedriver_win32\chromedriver.exe')
	driver.get(r'https://accounts.google.com/signin/v2/identifier?continue='+\
	'https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1'+\
	'&flowName=GlifWebSignIn&flowEntry = ServiceLogin')
	driver.implicitly_wait(15)

	loginBox = driver.find_element_by_xpath('//*[@id ="identifierId"]')
	loginBox.send_keys(gmailId)

	nextButton = driver.find_elements_by_xpath('//*[@id ="identifierNext"]')
	nextButton[0].click()

	passWordBox = driver.find_element_by_xpath(
		'//*[@id ="password"]/div[1]/div / div[1]/input')
	passWordBox.send_keys(passWord)

	nextButton = driver.find_elements_by_xpath('//*[@id ="passwordNext"]')
	nextButton[0].click()

	print('Login Successful...!!')
except:
	print('Login Failed')
