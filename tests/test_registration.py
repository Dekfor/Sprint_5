import pytest
from locators import MainPageLocators, AuthPageLocators, ProfileLocators
from conftest import wait_element

class TestRegistration:

    def test_registration_valid(self, driver, email):
        wait_element(driver, MainPageLocators.LOGIN_BUTTON).click()
        wait_element(driver, AuthPageLocators.NO_ACCOUNT_BUTTON).click()
        wait_element(driver, AuthPageLocators.EMAIL_INPUT).send_keys(email)
        wait_element(driver, AuthPageLocators.PASSWORD_INPUT).send_keys("Password123")
        wait_element(driver, AuthPageLocators.REPEAT_PASSWORD_INPUT).send_keys("Password123")
        wait_element(driver, AuthPageLocators.REGISTER_BUTTON).click()

        user_name = wait_element(driver, ProfileLocators.USER_NAME).text
        assert user_name == "User"

    def test_registration_invalid_email(self, driver):
        wait_element(driver, MainPageLocators.LOGIN_BUTTON).click()
        wait_element(driver, AuthPageLocators.NO_ACCOUNT_BUTTON).click()
        wait_element(driver, AuthPageLocators.EMAIL_INPUT).send_keys("invalidemail")
        wait_element(driver, AuthPageLocators.REGISTER_BUTTON).click()

        error = wait_element(driver, AuthPageLocators.ERROR_MESSAGE).text
        assert error == "Ошибка"

    def test_registration_existing_user(self, driver):
        existing_email = "test@mail.com"
        wait_element(driver, MainPageLocators.LOGIN_BUTTON).click()
        wait_element(driver, AuthPageLocators.NO_ACCOUNT_BUTTON).click()
        wait_element(driver, AuthPageLocators.EMAIL_INPUT).send_keys(existing_email)
        wait_element(driver, AuthPageLocators.PASSWORD_INPUT).send_keys("Password123")
        wait_element(driver, AuthPageLocators.REPEAT_PASSWORD_INPUT).send_keys("Password123")
        wait_element(driver, AuthPageLocators.REGISTER_BUTTON).click()

        error = wait_element(driver, AuthPageLocators.ERROR_MESSAGE).text
        assert error == "Ошибка"