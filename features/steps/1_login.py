import time, os, sys
from behave import given, when, then, step
sys.path.append(os.path.join(os.path.dirname(__file__),'../'))

@given("I am in login page '{url}'")
def i_go_to_login_page(context, url):
    context.helperfunc.open(url)
    context.helperfunc.maximize()

@when("I key in my email address '{email}'")
def i_key_in_my_email_address(context, email):
    context.helperfunc.find_by_xpath('/html/body/div[1]/div/div/form/div[1]/input').send_keys(email)

@step("I key in my password '{password}'")
def i_key_in_my_password(context, password):
    context.helperfunc.find_by_xpath('/html/body/div[1]/div/div/form/div[2]/div/input').send_keys(password)

@step('I click on Log in')
def i_click_on_log_in(context):
    context.helperfunc.find_by_xpath('/html/body/div[1]/div/div/form/div[3]/button').click()

@then("I should see my landing page title '{title}'")
def i_should_see_my_landing_page(context, title):
    error = context.helperfunc.find_by_xpath('/html/body/div[1]/div/div/div/div/div[1]/div[1]/h1').text

    time.sleep(5)

    if error in title:
        return True
    else:
        raise Exception('Failed')
