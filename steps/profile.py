from time import sleep
import re

from radish import then, when

from controls import Input, Link


@when("I login to 'account_name' account")
def i_see_the_title(step, account_name):
    email = "hazem.a.ahmed@gmail.com"
    password = "HazemIbrahim1"
