from selenium.webdriver.common.by import By

class Locators:
    entrance_on_the_main = (By.XPATH, './/button[text()='Войти в аккаунт']') #кнопка Войти в акк
    logo = (By.XPATH, './/header/nav/div') #logotype
    button_exit = (By.XPATH, './/button[contains(text(), 'Выход')]') #надпись Выход
    inscription_profile = (By.XPATH, './/a[@href="/account/profile"]') #надпись Профиль
    inscription_bread = (By.XPATH, './/span[contains(text(), 'Булки')]') #надпись Булки
    inscription_sause = (By.XPATH, './/span[contains(text(), 'Соусы')]') #надпись Соусы
    inscription_login = (By.CLASS_NAME, 'Auth_link__1f0lj') #надпись Зарегистрироваться
    button_personal_area = (By.XPATH, './/p[contains(text(), 'Личный кабинет')]') #кнопка личный кабинет
    inscription_fillings = (By.XPATH, './/span[contains(text(), 'Начинки')]') #надпись Начинки
    active_section = (By.XPATH, './/div[contains(@class, 'tab_tab_type_current')]') #активный раздел Начинки
    inscription_error_account = (By.XPATH, './/p[contains(text(), 'Такой пользователь уже существует')]') #надпись Такой пользователь уже существует
    inscription_error_password = (By.XPATH, './/div[contains(@class, 'input_status_error')]') #надпись некорректный пароль
    button_restore_password = (By.XPATH, './/a[@href="/forgot-password"]') #кнопка восстановить пароль
    inscription_button_entrance = (By.XPATH, './/a[@href="/login"]') #надпись войти
    button_entrance = (By.XPATH, './/button[contains(text(), 'Войти')]') #кнопка войти
    button_arrange_order = (By.XPATH, './/button[contains(text(), 'Оформить заказ')]') #кнопка оформить заказ
    button_login = (By.XPATH, './/button[contains(text(), 'Зарегистрироваться')]') #кнопка Зарегистрироваться
    button_constaction = (By.XPATH, './/a[@href='/']') #кнопка Конструктор
    field_name = (By.XPATH, './/div[label[contains(text(), 'Имя')]]//input') #Поле Имя
    field_email = (By.XPATH, './/div[label[contains(text(), 'Email')]]//input') #Поле Email
    field_password = (By.XPATH, './/div[label[contains(text(), 'Пароль')]]//input') #Поле Пароль