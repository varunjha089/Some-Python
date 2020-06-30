"""
    https://github.com/MicroPyramid/forex-python
"""
from forex_python.converter import CurrencyRates, CurrencyCodes

cur_rate = CurrencyRates()
cur_code = CurrencyCodes()


def remote_to_inr_fun(remote):
    usd_to_inr = cur_rate.get_rate(remote, 'INR')
    print("1" + str(cur_code.get_symbol(remote)) + " is " + str(usd_to_inr) + "Rs.")


def convert_remote_to_origin(remote, origin, amount):
    usd_to_inr_convert = cur_rate.convert(remote, origin, amount)
    return str(cur_code.get_symbol(origin)) + str(usd_to_inr_convert)


if __name__ == "__main__":
    remote_to_inr_fun('USD')
    print("Please select what you want to do.")
    print("1 -> Convert USD to INR")

    OPTIONS = int(input("Enter the option here: "))

    if OPTIONS == 1:
        AMOUNT = float(input("Enter the amount in USD: "))
        converted_usd_to_inr_amount = convert_remote_to_origin('USD', 'INR', AMOUNT)
        print(converted_usd_to_inr_amount)

    # print()
    # print(cur_code.get_symbol('INR'))
