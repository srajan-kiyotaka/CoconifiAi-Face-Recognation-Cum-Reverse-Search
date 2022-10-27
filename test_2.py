gotUrl = QtCore.pyqtSignal(str)
filePath = "/mnt/Images/test.png"

browser = webdriver.Firefox()
browser.get('http://www.google.hr/imghp')

# Click "Search by image" icon
elem = browser.find_element_by_class_name('gsst_a')
elem.click()

# Switch from "Paste image URL" to "Upload an image"
browser.execute_script("google.qb.ti(true);return false")

# Set the path of the local file and submit
elem = browser.find_element_by_id("qbfile")
elem.send_keys(filePath)

# Get the resulting URL and make sure it's displayed in English
browser.get(browser.current_url+"&hl=en")
try:
    # If there are multiple image sizes, we want the URL for the "All sizes" page
    elem = browser.find_element_by_link_text("All sizes")
    elem.click()
    gotUrl.emit(browser.current_url)
except:
    gotUrl.emit(browser.current_url)
browser.quit()