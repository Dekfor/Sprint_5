from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(),'Вход и регистрация')]")
    CREATE_AD_BUTTON = (By.XPATH, "//button[contains(text(),'Разместить объявление')]")

class AuthPageLocators:
    NO_ACCOUNT_BUTTON = (By.XPATH, "//button[contains(text(),'Нет аккаунта')]")
    EMAIL_INPUT = (By.NAME, "email")
    PASSWORD_INPUT = (By.NAME, "password")
    REPEAT_PASSWORD_INPUT = (By.XPATH, "//input[@placeholder='Повторите пароль']")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(),'Войти')]")
    REGISTER_BUTTON = (By.XPATH, "//button[contains(text(),'Создать аккаунт')]")

    ERROR_MESSAGE = (By.XPATH, "//span[contains(text(),'Ошибка')]")
    EMAIL_ERROR_INPUT = (By.XPATH, "//input[@name='email' and contains(@class,'input_span__yWPqB')]")

class ProfileLocators:
    USER_NAME = (By.XPATH, "//div[contains(@class,'user')]")
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(),'Выйти')]")

class AdPageLocators:
    TITLE_INPUT = (By.NAME, "title")
    DESCRIPTION_INPUT = (By.NAME, "description")
    PRICE_INPUT = (By.NAME, "price")

    CATEGORY_DROPDOWN = (By.NAME, "category")
    CITY_DROPDOWN = (By.NAME, "city")

    CONDITION_RADIO = (By.XPATH, "//input[@value='Новый']")
    PUBLISH_BUTTON = (By.XPATH, "//button[contains(text(),'Опубликовать')]")
    MY_ADS_BLOCK = (By.XPATH, "//div[contains(text(),'Мои объявления')]")
    AUTH_REQUIRED_MODAL = (By.XPATH, "//h1[contains(text(),'авторизуйтесь')]")