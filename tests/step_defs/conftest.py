import pytest
from pytest_bdd import given,parsers
from selenium import webdriver

YVYTU_HOME = "https://vientosdelaselva.com.ar/"
TIENDA_HOME = "https://tienda.claro.com.ar/"
@pytest.fixture
def browser():
    b = webdriver.Firefox()
    b.implicitly_wait(10)
    yield b
    b.quit()

@given(parsers.parse('que un usuario esta en la pagina "{web_name}"'))
def go_home_page(browser, web_name):
    if web_name == "Yvytu":
        browser.get(YVYTU_HOME)
    elif web_name == "TiendaClaro":
        browser.get(TIENDA_HOME)