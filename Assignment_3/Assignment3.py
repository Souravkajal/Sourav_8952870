# Importing required libraries

# pip install selenium

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Setting up the webdriver
driver = webdriver.Chrome()

# Navigating to the YouTube.com homepage
driver.get("https://www.youtube.com/")
time.sleep(8)

# Finding the search bar and entering text for travelling

search_bar = driver.find_element("xpath","/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[2]/ytd-searchbox/form/div[1]/div[1]/input")
search_bar.send_keys("travelling")

# Submitting the search query
search_bar.send_keys(Keys.RETURN)

# Waiting for the search results page to load
time.sleep(5)

# Verifying that the search results page has loaded
assert "travelling - YouTube" in driver.title


# Selecting a travelling from the search results
travelling_link = driver.find_element("xpath","/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer[1]/div[3]/ytd-video-renderer/div[1]/ytd-thumbnail/a/yt-image/img")
travelling_link.click()


time.sleep(21)


# click on subscribe button
subscribe = driver.find_element("xpath","/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-watch-metadata/div/div[2]/div[1]/div/ytd-subscribe-button-renderer/yt-smartimation/yt-button-shape/button/yt-touch-feedback-shape/div/div[2]")
subscribe.click()

# Waiting for the cart to update
time.sleep(2)

# Clicking on signin button
signin_button= driver.find_element("xpath","/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-modal-with-title-and-button-renderer/div/ytd-button-renderer/yt-button-shape/a/yt-touch-feedback-shape/div/div[2]")
signin_button.click()
time.sleep(2)


driver.close()
