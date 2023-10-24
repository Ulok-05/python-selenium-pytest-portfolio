from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.ID, 'login_link')


class LoginPageLocators:
    LOGIN_FORM = (By.ID, 'login_form')
    # LOGIN_INPUT_EMAIL = (By.ID, 'id_login-username')
    # LOGIN_INPUT_PASSWORD = (By.ID, 'id_login-password')
    # LOGIN_LINK_FORGOT_PASSWORD = (By.XPATH, '//*[@id="login_form"]/p/a')
    # LOGIN_BUTTON_LOGIN = (By.NAME, 'login_submit')

    REGISTRATION_FORM = (By.ID, 'register_form')
    # REGISTRATION_INPUT_EMAIL = (By.ID, 'id_registration-email')
    # REGISTRATION_INPUT_PASSWORD = (By.ID, 'id_registration-password1')
    # REGISTRATION_INPUT_PASSWORD_AGAIN = (By.ID, 'id_registration-password2')
    # REGISTRATION_BUTTON_REG = (By.NAME, 'registration_submit')

