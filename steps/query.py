import time

from radish import then, when

from controls import Input, Link


@when("I search for '{text}'")
def i_see_the_title(step, text):
    searchbox = Input(cssclass="js-search-input")
    searchbox.input(text)

    button = Input(cssclass='js-search-button')
    button.click()


@then("I see the link '{text}'")
def i_see_the_link(step, text):
    Link(text=text).locate()
    time.sleep(5)
