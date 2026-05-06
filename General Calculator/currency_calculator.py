from forex_python.converter import CurrencyRates


currency_rates = CurrencyRates()


def run_currency_calculator():
    print("***CURRENCY CONVERTER***")

    while True:
        from_currency = input("Enter FROM currency (e.g. USD, SGD, EUR): ").upper()
        to_currency = input("Enter TO currency (e.g. USD, SGD, EUR): ").upper()

        try:
            amount = float(input("Enter amount to convert: "))
            result = currency_rates.convert(from_currency, to_currency, amount)
            print(f"{amount} {from_currency} = {result:.2f} {to_currency}")
            break
        except ValueError:
            print("Invalid input. Please enter a valid number for the amount.")
        except:
            print("Invalid input. Please enter valid currency codes and try again.")
