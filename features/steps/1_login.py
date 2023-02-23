import time, os, sys
from behave import given, when, then
sys.path.append(os.path.join(os.path.dirname(__file__),'../'))

@given('I go to login page')
def i_go_to_login_page(context):
    context.helperfunc.open('https://goatocr.com/')
    context.helperfunc.maximize()

@when('I key in my email address')
def i_key_in_my_email_address(context):
    context.helperfunc.find_by_xpath('/html/body/div[1]/div/div/form/div[1]/input').send_keys('stx6@outlook.com')

@when('I key in my password')
def i_key_in_my_password(context):
    context.helperfunc.find_by_xpath('/html/body/div[1]/div/div/form/div[2]/div/input').send_keys('stx123321')

@when('I click on Log in')
def i_click_on_log_in(context):
    context.helperfunc.find_by_xpath('/html/body/div[1]/div/div/form/div[3]/button').click()

@then('I should see my landing page')
def i_should_see_my_landing_page(context):
    error = context.helperfunc.find_by_xpath('/html/body/div[1]/div/div/div/div/div[1]/div[1]/h1').text

    time.sleep(5)

    if error in "GOAT OCR":
        return True
    else:
        raise Exception('Failed')
