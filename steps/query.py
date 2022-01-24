from selenium.webdriver.common.by import By

from radish import then
from radish import world


@then("I search for '{text}'")
def i_see_the_title(step, text):
    print(f"I search for {text}")
    box = world.webdriver.find_element(By.XPATH, "//input")
    print(f"found box: {box}")
    box.send_keys(text)
    print("searching button")
    button = world.webdriver.find_element(By.XPATH,
        "//span[contains(class, 'js-jump-to-badge-search-text-global')]")
    print("click button")
    button.click()
