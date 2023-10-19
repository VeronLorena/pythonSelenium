from pytest_bdd import scenarios, then, parsers
from selenium.webdriver.common.by import By

scenarios('../features/Yvytu.feature')

@then(parsers.parse('el titulo principal es "{main_title}"'))
def check_main_title(browser, main_title):
    assert main_title in browser.find_element(By.CSS_SELECTOR, 'h1').text