#CURRENCY CONVERTER:

class CurrencyConverter:
    def __init__(self, rates):
        self.rates = rates

    def convert(self, amount, from_currency, to_currency):
        initial_amount = amount
        if from_currency != 'EUR':
            amount = amount / self.rates[from_currency]
        # limit the precision to 4 decimal places
        amount = round(amount * self.rates[to_currency], 4)
        return amount

rates = {
    'EUR': 1.0,
    'USD': 1.19,
    'GBP': 0.87
}

converter = CurrencyConverter(rates)

print(converter.convert(100, 'EUR', 'USD'))
print(converter.convert(100, 'USD', 'GBP'))
