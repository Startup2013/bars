from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time

def lookForSomething(keyword, town_list):
        browser = webdriver.Firefox() # Get local session of firefox
        browser.get("https://accounts.google.com/ServiceLogin?service=adwords&continue=https://adwords.google.com/um/gaiaauth?apt%3DNone%26ltmpl%3Dsignin&hl=en_US&ltmpl=signin&passive=86400&skipvpage=true&sacu=1&sarp=1") # Load page

        my_email = browser.find_element_by_id("Email")
        my_email.send_keys("chanzzada@gmail.com")
        my_pass = browser.find_element_by_id("Passwd")
        pass_var = "lampedziukaizeris1982"
        my_pass.send_keys(pass_var + Keys.RETURN)
        #assert "Campaign Management" in browser.title
        time.sleep(10) # Let the page load, will be added to the API
        browser.get("https://adwords.google.com/ko/KeywordPlanner/Home?__c=4102253188&__u=4436042908&__o=cues")
        time.sleep(5)
        browser.find_element_by_id("gwt-debug-splash-panel-find-keywords-selection-input").click()

        #END OF MAIN CONNECTION

        browser.find_element_by_xpath("//textarea[@id='gwt-debug-keywords-text-area']").send_keys(keyword)
        browser.find_element_by_id("gwt-debug-location-pill-display-text-div").click()
        browser.find_element_by_link_text("Remove all").click()
        browser.find_element_by_id("gwt-debug-geo-search-box").send_keys(town_list)
        time.sleep(2)
        browser.find_element_by_link_text(town_list + ", England, United Kingdom").click()
        browser.find_element_by_id("gwt-debug-splash-panel-form").click()
        browser.find_element_by_css_selector("div.spCQB > #gwt-debug-search-button > div.goog-button-base-outer-box.goog-inline-block > div.goog-button-base-inner-box.goog-inline-block > div.goog-button-base-pos > div.goog-button-base-content > #gwt-debug-search-button-content").click()
        time.sleep(3)
        table = browser.find_element_by_css_selector("table.spMEC")
        #elem.get_attribute("innerHTML")
        #print "Inner HTML\n"
        #print table.get_attribute("innerHTML")
        time.sleep(3)

        #toSave = "<html><head></head><body>" + str(table.get_attribute("outerHTML").encode('utf-8')) + "</body></html>"
        print str(table.get_attribute("outerHTML").encode('utf-8'))

        #f = open('C:/Users/HAL/Desktop/'+ town_list +'.html','w')
        #f.write(str(toSave))
        #f.close()
        #saveToCSV(town_list)



#lookForSomething("Cash 4 Clothes", "London")