import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException

# Prompting the user for username and password
InstaID = 'mrobotfx' # User input for Instagram ID
InstaPass = '$22dolar' # User input for Instagram password
InstaTag = 'cristiano'  # Target Instagram account (Cristiano Ronaldo's account)

nFollowers = 2000000  # Number of followers to follow

chrome_driver_path = "./chromedriver.exe"  # Path to your chromedriver

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

CookiesText = "Consenti cookie essenziali e facoltativi"
FollowText = "Segui"

class Bot:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)
        self.driver.implicitly_wait(5)

    def login(self):
        self.driver.get("https://www.instagram.com/")

        # Accept cookies
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//button[text()='"+ CookiesText + "']").click()

        # Logging in with provided username and password
        ID = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
        ID.send_keys(InstaID)

        Pass = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
        Pass.send_keys(InstaPass)

        time.sleep(2)
        Pass.send_keys(Keys.ENTER)

    def find_followers(self):
        time.sleep(5)
        self.driver.get(f"https://www.instagram.com/{InstaTag}/followers")

    def follow(self):
        modal = self.driver.find_element(By.CSS_SELECTOR, 'button._acan._acap._acas')

        FCount = 0

        buttons = self.driver.find_elements(By.CSS_SELECTOR, 'div div button')

        for x in buttons:
            if x.text == FollowText and FCount < nFollowers:
                time.sleep(2)
                x.click()
                FCount += 1

            # Optional: Scroll down to load more followers
            # modal.send_keys(Keys.PAGE_DOWN)
            # self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)

# Instantiate the Bot and run the login, find followers, and follow actions
Bot = Bot()
Bot.login()
Bot.find_followers()
Bot.follow()
Bot.driver.quit()
