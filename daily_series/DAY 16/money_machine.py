class MoneyMachine:
    CURRENCY = "rupee"
    COIN_VALUES = {
        "quarters": 0.25,
        "nickels": 0.05,
        "pennies": 0.01,
        "dollars": 1.00,
        "dimes": 0.10,
    }

    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self):
        print(f"{self.CURRENCY} {self.profit}")

    def process_coins(self):
        print("Please insert coins.")
        self.money_received = 0
        for coin in self.COIN_VALUES:
            count = int(input(f"How many {coin}?: "))
            self.money_received += count * self.COIN_VALUES[coin]
        return self.money_received

    def make_payment(self, cost):
        """Returns True when payment is accepted, or False if insufficient."""
        self.process_coins()
        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            print(f"Here is {self.CURRENCY} {change} in change.")
            self.profit += cost
            self.money_received = 0
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")
            self.money_received = 0
            return False