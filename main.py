from forex_python.converter import CurrencyRates

c = CurrencyRates()

def convert_currency():
    amount = float(input("Veuillez saisir le montant à convertir : "))
    from_currency = input("Veuillez saisir la devise source (dollar, euro, livre) : ").lower()
    to_currency = input("Veuillez saisir la devise cible (dollar, euro, livre) : ").lower()

    currency_mapping = {'dollar': 'USD', 'euro': 'EUR', 'livre': 'GBP'}

    if from_currency not in currency_mapping or to_currency not in currency_mapping:
        print("Les devises valides sont : dollar, euro, livre.")
        return

    exchange_rate = c.get_rate(currency_mapping[from_currency], currency_mapping[to_currency])

    converted_amount = amount / exchange_rate

    print(f"\n{amount} {from_currency} équivaut à {converted_amount:.2f} {to_currency}")

while True:
    convert_currency()
    cont = input("Voulez-vous effectuer une autre conversion ? (oui/non) : ").lower()
    if cont != 'oui':
        break

