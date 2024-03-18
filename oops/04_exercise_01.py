"""
Methods Exercise
Create a method, which takes the state and gross income as the arguments and returns the net income after
deducting tax based on the state.

Assume Federal Tax: 10%
Assume state tax on your wish.

You don’t have to do for all the states, just take 3-4 to solve the purpose of the exercise.
"""
federal_tax = 10


def calculateNetIncome (state, gross):
    """
    calculate the net income after federal and state tax
    :param state:
    :param gross:
    :return:
    """
    state_tax = {'CA': 10, "NY": 12, "ME": 9, "NJ": 7}
    net = gross - (gross * (federal_tax/100))

    if state in state_tax:
        net = net - (gross * (state_tax[state]/100))
        print("Your net income is :" + str(net))
        return net

    else:
        print("given State is not available in list")
        return None


calculateNetIncome('CA', 1000000)
calculateNetIncome('blr', 900000)

