from locators import MainPageLocators, AuthPageLocators, ProfileLocators
from helpers import generate_email, wait_element

class TestLogin:

    def test_login(self, driver):
        email = generate_email()
        wait_element(driver, MainPageLocators.LOGIN_BUTTON).click()
        wait_element(driver, AuthPageLocators.NO_ACCOUNT_BUTTON).click()
        wait_element(driver, AuthPageLocators.EMAIL_INPUT).send_keys(email)
        wait_element(driver, AuthPageLocators.PASSWORD_INPUT).send_keys("Password123")
        wait_element(driver, AuthPageLocators.REPEAT_PASSWORD_INPUT).send_keys("Password123")
        wait_element(driver, AuthPageLocators.REGISTER_BUTTON).click()
        wait_element(driver, MainPageLocators.LOGIN_BUTTON).click()
        wait_element(driver, AuthPageLocators.EMAIL_INPUT).send_keys(email)
        wait_element(driver, AuthPageLocators.PASSWORD_INPUT).send_keys("Password123")
        wait_element(driver, AuthPageLocators.LOGIN_BUTTON).click()

        user_name = wait_element(driver, ProfileLocators.USER_NAME).text
        assert user_name == "User"
        