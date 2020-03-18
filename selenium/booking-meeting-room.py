# https://stackoverflow.com/questions/38232406/selenium-in-python-selecting-an-option
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://dgoa/MBS/MBSGF01/Default.aspx?newversion=1")

ddlUseDateElement = driver.find_element_by_name("ddlUseDate")
ddlUseDateElement.send_keys("2020/4/16")
txtBeginTimeElement = driver.find_element_by_name("txtBeginTime")
txtBeginTimeElement.send_keys("1530")
txtEndTimeElement = driver.find_element_by_name("txtEndTime")
txtEndTimeElement.send_keys("1600")
ddlMeetingRoomElement = driver.find_element_by_id("ddlMeetingRoom")

driver.execute_script("showDropdown = function (element) {var event; event = document.createEvent('MouseEvents'); event.initMouseEvent('mousedown', true, true, window); element.dispatchEvent(event); }; showDropdown(arguments[0]);", ddlMeetingRoomElement)

driver.find_element_by_xpath("//select[@id='ddlMeetingRoom']/option[text()='舒壓室(規範與服務時段請見人資網站公告）(TPE02)']").click()

txtMeetingSubjectElement = driver.find_element_by_name("txtMeetingSubject")
txtMeetingSubjectElement.send_keys("1")


# driver.close()