from radish import then


@then("I run my own acre-test step")
def i_run_my_own_step(step):
    print("my own acre-test step")
    pass
