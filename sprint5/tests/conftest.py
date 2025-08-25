import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from generation_log_pas import LoginPasswordGenerator
from data import Credential
from curl import *
from locators import Locators

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def start_from_login_page(driver): #вход на сайт по кнопке Войти
    login_page = login_site
    driver.get(login_page)

    driver.find_element(*Locators.field_email).send_keys(Credential.email)
    driver.find_element(*Locators.field_password).send_keys(Credential.password)
    driver.find_element(*Locators.button_entrance).click()

    return driver

@pytest.fixture
def start_from_main_page(driver): #вход на сайт через личный кабинет
    main_page = main_site
    driver.get(main_page)

    driver.find_element(*Locators.button_personal_area).click()
    driver.find_element(*Locators.button_entrance).click()

    driver.find_element(*Locators.field_email).send_keys(Credential.email)
    driver.find_element(*Locators.field_password).send_keys(Credential.password)
    driver.find_element(*Locators.button_entrance).click()

    return driver

@pytest.fixture
def start_from_register_page(driver): #вход на сайт через кнопку регистрации
    register_page = register_site
    driver.get(register_page)

    driver.find_element(*Locators.inscription_button_entrance).click()

    driver.find_element(*Locators.field_email).send_keys(Credential.email)
    driver.find_element(*Locators.field_password).send_keys(Credential.password)
    driver.find_element(*Locators.button_entrance).click()

    return driver

@pytest.fixture
def start_from_recovery_page(driver): #вход на сайт со страницы восстановления пароля
    login_page = login_site
    driver.get(login_page)

    driver.find_element(*Locators.button_restore_password).click() 
    WebDriverWait(driver, 6).until(EC.visibility_of_element_located(Locators.inscription_button_entrance))
    driver.find_element(*Locators.inscription_button_entrance).click()

    driver.find_element(*Locators.field_email).send_keys(Credential.email)
    driver.find_element(*Locators.field_password).send_keys(Credential.password)
    driver.find_element(*Locators.button_entrance).click()

    return driver
  
