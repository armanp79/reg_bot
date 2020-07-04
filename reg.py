from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


#starting url
s_url = "https://www.reg.uci.edu/registrar/soc/webreg.html"

response = False


# ------ Enter your own credentials here ------- 
user, passwd = "username","password"
code = "class_code"

# enter path to webdriver on your local device
PATH = "enter path here"

# -------------------------------------------------


def login():
    try:
        driver = webdriver.Chrome(PATH)
        driver.get(s_url)
        link = driver.find_element_by_link_text("Access WebReg")
        link.click()

        user_search = driver.find_element_by_name('ucinetid').send_keys(user)
        pass_search = driver.find_element_by_name('password').send_keys(passwd + Keys.RETURN)

        # now at main menu
        enroll = driver.find_element_by_xpath('/html/body/center[1]/table/tbody/tr/td/form[1]/input[4]').click()

        #add class
        click_add = driver.find_element_by_id("add").click()
        insert_code = driver.find_element_by_xpath("/html/body/center[1]/form[2]/table/tbody/tr[2]/td/table/tbody/tr[2]/td[2]/input")
        insert_code.send_keys(code + Keys.RETURN)

        #check if class was successfully added
        try:
            driver.find_element_by_class_name("studyList")
            response = True
        except:
            response = False

        
        # logout and quit driver
        driver.find_element_by_class_name('WebRegButton.WebRegLogoutButton').click()
        driver.quit()
        
        return response
    
    except:
        print('error')
        # logout and quit driver
        driver.find_element_by_class_name('WebRegButton.WebRegLogoutButton').click()
        driver.quit()


while response == False:
    start = time.time()
    response = login()
    print('time: ' + str((time.time() - start)))



