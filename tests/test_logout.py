from locators import MainPageLocators, AuthPageLocators, ProfileLocators
from conftest import wait_element

class TestLogout:

    def test_logout(self, driver, email):
        wait_element(driver, MainPageLocators.LOGIN_BUTTON).click()
        wait_element(driver, AuthPageLocators.NO_ACCOUNT_BUTTON).click()
        wait_element(driver, AuthPageLocators.EMAIL_INPUT).send_keys(email)
        wait_element(driver, AuthPageLocators.PASSWORD_INPUT).send_keys("Password123")
        wait_element(driver, AuthPageLocators.REPEAT_PASSWORD_INPUT).send_keys("Password123")
        wait_element(driver, AuthPageLocators.REGISTER_BUTTON).click()

        wait_element(driver, ProfileLocators.LOGOUT_BUTTON).click()
        login_button = wait_element(driver, MainPageLocators.LOGIN_BUTTON)
        assert login_button.is_displayed()