from locators import MainPageLocators, AuthPageLocators, AdPageLocators
from helpers import generate_email, wait_element

class TestCreateAd:

    def test_create_ad_unauthorized(self, driver):
        wait_element(driver, MainPageLocators.CREATE_AD_BUTTON).click()
        modal = wait_element(driver, AdPageLocators.AUTH_REQUIRED_MODAL)
        assert modal.is_displayed()

    def test_create_ad_authorized(self, driver):
        email = generate_email()
        wait_element(driver, MainPageLocators.LOGIN_BUTTON).click()
        wait_element(driver, AuthPageLocators.NO_ACCOUNT_BUTTON).click()
        wait_element(driver, AuthPageLocators.EMAIL_INPUT).send_keys(email)
        wait_element(driver, AuthPageLocators.PASSWORD_INPUT).send_keys("Password123")
        wait_element(driver, AuthPageLocators.REPEAT_PASSWORD_INPUT).send_keys("Password123")
        wait_element(driver, AuthPageLocators.REGISTER_BUTTON).click()
        
        wait_element(driver, MainPageLocators.CREATE_AD_BUTTON).click()
        wait_element(driver, AdPageLocators.TITLE_INPUT).send_keys("Test")
        wait_element(driver, AdPageLocators.DESCRIPTION_INPUT).send_keys("Test description")
        wait_element(driver, AdPageLocators.PRICE_INPUT).send_keys("1000")
        wait_element(driver, AdPageLocators.CATEGORY_DROPDOWN).click()
        wait_element(driver, AdPageLocators.CITY_DROPDOWN).click()
        wait_element(driver, AdPageLocators.CONDITION_RADIO).click()
        wait_element(driver, AdPageLocators.PUBLISH_BUTTON).click()

        ad = wait_element(driver, AdPageLocators.MY_ADS_BLOCK)
        assert ad.is_displayed()
        