import time, os, sys
from behave import given, when, then, step
from selenium.webdriver.common.keys import Keys
sys.path.append(os.path.join(os.path.dirname(__file__),'../'))

@given('I am in landing page')
def i_am_in_landing_page(context):
    context.helperfunc.open('https://goatocr.com/home')

@when('I click on my username')
def i_click_on_my_username(context):
    context.helperfunc.find_by_xpath('/html/body/div[1]/div/div/div/div/div[1]/div[2]').click()

@step('I click on Edit Profile')
def i_click_on_edit_profile(context):
    context.helperfunc.find_by_xpath('/html/body/div[1]/div/div/div/div/div[1]/div[2]/div[2]/button[2]').click()

@then('I should see Edit Profile')
def i_should_see_edit_profile(context):
    error = context.helperfunc.find_by_xpath('/html/body/div[1]/div/div[2]/div/div[1]/div').text

    time.sleep(5)

    if error in "Edit Profile":
        return True
    else:
        raise Exception('Failed')

@when("I update my username '{username}'")
def i_update_my_username(context, username):
    username_field = context.helperfunc.find_by_xpath(
        '/html/body/div[1]/div/div[2]/div/div[2]/div/form/div[2]/label/input')
    username_field.send_keys(Keys.CONTROL + "a")
    username_field.send_keys(Keys.DELETE)
    username_field.send_keys(username)

@step('I click on Update')
def i_click_on_update(context):
    context.helperfunc.find_by_xpath('/html/body/div[1]/div/div[2]/div/div[2]/div/form/div[3]/button').click()

@step('I click on Back')
def i_click_on_update(context):
    context.helperfunc.find_by_xpath('/html/body/div[1]/div/div[2]/div/div[1]/button').click()

@step('I click on View Profile')
def i_click_on_update(context):
    context.helperfunc.find_by_xpath('/html/body/div[1]/div/div/div/div/div[1]/div[2]/div[2]/button[1]').click()

@then("I should see my updated username '{username}'")
def i_should_see_my_updated_username(context, username):
    error = context.helperfunc.find_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div[4]/div/div[2]/div[1]/div[1]/span').text

    time.sleep(5)

    if error in username:
        return True
    else:
        raise Exception('Failed')