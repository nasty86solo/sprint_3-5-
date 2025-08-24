import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from curl import *
from data import Credential
from generation_log_pas import LoginPasswordGenerator

@pytest.mark.usefixtures("register_new_account")
#регистрация нового пользователя
class TestCheckNewRegister:
    def test_registration(self):
        driver, email, password = self.register_new_account()

        driver.find_element(*Locators.field_email).send_keys(email)
        driver.find_element(*Locators.field_password).send_keys(password)
        driver.find_element(*Locators.button_entrance).click()

        WebDriverWait(driver, 10).until(EC.url_to_be(main_site))

        assert driver.current_url == main_site

@pytest.mark.usefixtures("start_from_main_page")
#повторная регистрация
class TestCheckingCreationExistingAccount:
    def test_existing_ecount(self, start_from_main_page):
        driver = start_from_main_page

        driver.find_element(*Locators.inscription_login).click()
        driver.find_element(*Locators.field_name).send_keys(Credential.name)
        driver.find_element(*Locators.field_email).send_keys(Credential.email)
        driver. find_element(*Locators.field_password).send_keys(Credential.password)

        driver. find_element(*Locators.button_login).click()

        assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.inscription_error_account))

@pytest.mark.usefixtures("start_from_main_not_login")
# попытка регистрации без имени
class TestCheckRegisterNoName:
    def test_registration_no_name(self, start_from_main_not_login):
        driver = start_from_main_not_login

        driver.find_element(*Locators.inscription_login).click()

        generator = LoginPasswordGenerator()
        email, password = generator.generate()

        driver.find_element(*Locators.field_email).send_keys(email)
        driver.find_element(*Locators.field_password).send_keys(password)

        driver.find_element(*Locators.button_login).click()

        assert driver.current_url == register_site

@pytest.mark.usefixtures("start_from_main_not_login")
class TestCheckingErrorPassword:
#попытка регистрации при неккоректном пароле
    def test_error_password(self, start_from_main_not_login):
        driver = start_from_main_not_login

        driver.find_element(*Locators.inscription_login).click()
        driver.find_element(*Locators.field_name).send_keys(Credential.name)
        driver.find_element(*Locators. field_email).send_keys(Credential.email)
        driver. find_element(*Locators.field_password).send_keys(Credential.password)

        driver.find_element(*Locators.button_login).click()

        assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.inscription_error_password))

@pytest.mark.usefixtures("start_from_main_not_login")
class TestCheckingErrorPassword:
#попытка регистрации без пароля
    def test_no_password(self, start_from_main_not_login):
        driver = start_from_main_not_login

        email = 'NSoloveva28FS147@yandex.ru'

        driver.find_element(*Locators.inscription_login).click()
        driver.find_element(*Locators.field_name).send_keys(Credential.name)
        driver. find_element(*Locators.field_email).send_keys(email)
        driver.find_element(*Locators.button_login).click()

        assert driver.current_url == register_site