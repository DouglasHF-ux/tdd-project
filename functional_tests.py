from selenium import webdriver

browser = webdriver.Edge()

browser.get('http://localhost:8000')

assert 'To-Do' in browser.title

browser.quit()