from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains

# Enter the path of the file "geckodriver.exe"
driver = webdriver.Firefox(executable_path='')


# Enter your data
usr = ""
pwd = ""

driver.get('https://www.messenger.com/')
print("Opened messenger")
sleep(1)

username_box = driver.find_element_by_id('email')
username_box.send_keys(usr)
print("Email Id entered")
sleep(1)


password_box = driver.find_element_by_id('pass')
password_box.send_keys(pwd)
print("Password entered")
sleep(1)

login_box = driver.find_element_by_id('loginbutton')
login_box.click()
sleep(1)
print('Log in button pressed')

# Getting the list with the users that you have talked.
contacts_area = driver.find_element_by_tag_name("ul").find_elements_by_tag_name("li")

for contact in contacts_area:
    text = contact.text
# Enter the name of the person or the team that you want to send a message
    if "" in text:
        wanted_contact = contact
        # Clicking on the conversation with the user that you wanted to send a message
        wanted_contact.click()
        break;
print('Contact found')

# Clicking on the text area of the conversation in order to write your message.
text_area = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/span/div[2]/div[2]/div[2]/div/div[4]").click()
actions = ActionChains(driver)
# Enter the message that you want to send
actions.send_keys('')
actions.perform()
print('Message has been written')

# Searching the "Enter" button of messenger and clicking it
enter_button = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/span/div[2]/div[2]/div[2]/div/a')
actions = ActionChains(driver)
actions.move_to_element(enter_button)
actions.click()
actions.perform()
print('Enter clicked')

print("Done")

