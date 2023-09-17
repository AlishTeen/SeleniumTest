from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PracticeFormPage:

    def __init__(self, driver):
        self.driver = driver

    def test_fill_out_form(self, first_name, last_name, email, phone_number, gender, date_of_birth, subjects, hobbies,
                           picture, address,
                           state, city):
        self._enter_first_name(first_name)
        self._enter_last_name(last_name)
        self._enter_email(email)
        self._enter_phone_number(phone_number)
        self._select_gender(gender)
        self._enter_date_of_birth(date_of_birth)
        self._enter_subjects(subjects)
        self._select_hobbies(hobbies)
        self._upload_picture(picture)
        self._enter_address(address)
        self._select_state(state)
        self._select_city(city)
        self._submit_form()
        try:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.driver.find_element(By.CLASS_NAME, 'modal-header')))
            return True
        except:
            return False

    def _move_to_element_and_click(self, element):
        self.driver.execute_script("arguments[0].click();", element)

    def _pick_dropdown(self, element, keys):
        element.send_keys(keys)
        element.send_keys(Keys.ENTER)

    def _enter_email(self, email):
        self.driver.find_element(By.ID, "userEmail").send_keys(email)

    def _enter_phone_number(self, phone_number):
        self.driver.find_element(By.ID, "userNumber").send_keys(phone_number)

    def _enter_first_name(self, first_name):
        self.driver.find_element(By.ID, "firstName").send_keys(first_name)

    def _enter_last_name(self, last_name):
        self.driver.find_element(By.ID, "lastName").send_keys(last_name)

    def _select_gender(self, gender):
        elements = self.driver.find_elements(By.CSS_SELECTOR, '#genterWrapper > div .custom-control-label')
        for elem in elements:
            if elem.text == gender:
                self._move_to_element_and_click(elem)

    def _enter_date_of_birth(self, dob):
        self.driver.find_element(By.ID, "dateOfBirthInput").send_keys(dob)

    def _enter_subjects(self, subjects):
        self.driver.find_element(By.ID, "subjectsInput").send_keys(subjects)

    def _upload_picture(self, file_path):
        self.driver.find_element(By.ID, "uploadPicture").send_keys(file_path)

    def _select_hobbies(self, hobbies):
        elements = self.driver.find_elements(By.CSS_SELECTOR, '#hobbiesWrapper > div .custom-control-label')
        for elem in elements:
            if elem.text in hobbies:
                self._move_to_element_and_click(elem)

    def _enter_address(self, address):
        self.driver.find_element(By.ID, "currentAddress").send_keys(address)

    def _select_state(self, state):
        self._pick_dropdown(self.driver.find_element(By.ID, 'react-select-3-input'), state)

    def _select_city(self, city):
        self._pick_dropdown(self.driver.find_element(By.ID, 'react-select-4-input'), city)

    def _submit_form(self):
        submit = self.driver.find_element(By.ID, "submit")
        self._move_to_element_and_click(submit)
