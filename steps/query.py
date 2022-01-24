from selenium.webdriver.common.by import By

from radish import then
from radish import world


@then("I search for '{text}'")
def i_see_the_title(step, text):
    print(f"I search for {text}")
    box = world.webdriver.find_element(By.XPATH, "//input")
    print(f"found box: {box}")
    box.input(text)
    print("searching button")
    button = world.webdriver.find_element(By.XPATH,
        "//button[contains(., 'search')")
    print("click button")
    button.click()
