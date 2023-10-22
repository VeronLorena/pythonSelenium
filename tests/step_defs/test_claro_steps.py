from pytest_bdd import scenarios, given, then, parsers
import requests
from colorama import Fore, Back, Style

# Scenario
scenarios('../features/Claro.feature')

CLARO_URL = 'https://tienda.claro.com.ar'

@given(parsers.parse('que un usuario llama al servivio "{service_url}"'), target_fixture='call_service')
def call_service(service_url):
    endpoint = CLARO_URL + service_url
    print(Fore.BLUE+'El endpoint es: '+endpoint)
    results = requests.get(endpoint)
    print(Fore.GREEN+'La respuesta es: '+results.text)
    return results

@then(parsers.parse('obtiene de respuesta del servicio "{code:d}"'))
def verify_service_code_response(call_service, code):
    assert call_service.status_code == code
    print(Style.RESET_ALL+Back.BLUE+'Respuesta correcta!'+code)