import undetected_chromedriver as uc
driver = uc.Chrome()
# driver.get('https://distilnetworks.com')

# from selenium import webdriver
from getpass import getpass

username = input("TS2740")
password = getpass("Werty@1234")
birth_year = input("1991")

# System.setProperty(“webdriver.chrome.driver”,path_to_browser_driver)
# WebDriver driver = new ChromeDriver()


# System.setProperty(“webdriver.chrome.driver”,path_to_browser_driver)
# WebDriver driver = new ChromeDriver()

# driver = uc.Chrome("C:\\webdriver\\chromedriver.exe")
driver.get("https://tc.algomojo.com/#/")

username_textbox = driver.find_element_by_id("act_id")
username_textbox.send_keys(username)

password_textbox  = driver.find_element_by_id("password")
password_textbox.send_keys(password)

birth_year_textbox = driver.find_element_by_id("panno")
birth_year_textbox.send_keys(birth_year)

login_button = driver.find_element_by_id("submit")
login_button.submit() 