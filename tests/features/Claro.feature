@claro
Feature: Home Claro
    Scenario: Servicio
        Given que un usuario llama al servivio "/api/contentManagement?content=Productos_destacados_spot"
        Then obtiene de respuesta del servicio "200"