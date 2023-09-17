import pytest
import os
from practice_form_page import PracticeFormPage


@pytest.mark.smoke
def test_smoke(browser):
    form = PracticeFormPage(browser)
    assert form.test_fill_out_form(first_name="John",last_name="Doe",email="eamil.@gmail.com",phone_number="8777123456",gender="Male",date_of_birth="01 Jan 1990",subjects="Math",hobbies=["Sports", "Reading"],picture=f'{os.getcwd()}' + '/picture/test.png',address="E506",state="NCR",city="Moscow")


@pytest.mark.xfail
def test_name_fail(browser):
    form = PracticeFormPage(browser)
    assert form.test_fill_out_form(first_name="",last_name="",email="eamil.@gmail.com",phone_number="8777123456",gender="Female",date_of_birth="05 Apr 2000",subjects="Math",hobbies=["Reading"],picture=f'{os.getcwd()}' + '/picture/test.png',address="C409",state="NCR",city="Almaty")


@pytest.mark.xfail
def test_contact_fail(browser):
    form = PracticeFormPage(browser)
    assert form.test_fill_out_form(first_name="Jason",last_name="Smith",email="8777123456",phone_number="eamil.@gmail.com",gender="Male",date_of_birth="06 Apr 2000",subjects="English,Chemistry",hobbies=["Sports"],picture=f'{os.getcwd()}' + '/picture/test.png',address="DD2209",state="NCR",city="Astana")


