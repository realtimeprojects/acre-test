import time
import re

from radish import then, when

from controls import Input, Link


@when("I search for '{text}'")
def i_see_the_title(step, text):
    searchbox = Input(cssclass="js-search-input")
    searchbox.input(text)

    button = Input(cssclass='js-search-button')
    button.click()


@then(re.compile(r"I (see|follow) the link '(.*)'"))
def i_see_the_link(step, command, text):
    link = Link(text=text)
    link.locate()
    if command == 'follow':
        link.click()

    time.sleep(5)
