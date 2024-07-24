from selenium.webdriver.common.by import By


class HeaderPageLocators:

    # логотип "Самокат"
    SCOOTER_LOGO = By.XPATH, './/a[contains(@class, "Header_LogoScooter")]'
    # логотип "Яндекс"
    YANDEX_LOGO = By.XPATH, './/a[contains(@class, "Header_LogoYandex")]'
