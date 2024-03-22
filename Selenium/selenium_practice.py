from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize Chrome WebDriver
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

# Navigate to the website
driver.get("https://www.python.org")
# Find the ul element by class name
li_elements = driver.find_elements(By.CSS_SELECTOR,".event-widget .shrubbery .menu li")


# Iterate over each li element and print its text or perform other actions
obj={}
i=1
for li in li_elements:
    time1=li.find_element(By.TAG_NAME,"time").text
    name=li.find_element(By.TAG_NAME,"a").text
    obj.update({i :{"time": time1, "name": name}})
    i+=1
# Your automation code goes here
print(obj)
driver.quit()



