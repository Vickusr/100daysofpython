# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import menu as m


def multiply(coin_value, number_if_coins):
    return coin_value * number_if_coins


class CoffeeMachine:

    def __init__(self):
        self.resources = m.resources
        self.Money = 0
        self.status = 'On'

    def off(self):
        self.status = 'Off'
        print('Machine is off!')

    def on(self):
        self.status = 'On'
        print('Machine is on!')

    def show_resources(self):
        for r in self.resources:
            print(f'{r}: {self.resources[r]}')
        print(f'Money: {self.Money}')

    def enough_resources(self, drink):

        for r in m.MENU[drink]['ingredients']:

            if m.MENU[drink]['ingredients'][r] > self.resources[r]:
                print(f'Not enough {r}')
                return False

        return True

    def remove_resources(self, drink):
        for r in m.MENU[drink]['ingredients']:
            self.resources[r] -= m.MENU[drink]['ingredients'][r]

    @staticmethod
    def make_drink(drink_name):
        print(f'Making {drink_name}')

    def take_payment(self, drink):
        print('Please insert coins.')
        transaction_value = 0

        for k in m.coins:
            temp_amount = int(input(f'How many {k}?: '))
            temp_value = multiply(m.coins[k], temp_amount)
            transaction_value += temp_value

        if transaction_value >= m.MENU[drink]['cost']:
            self.Money += m.MENU[drink]['cost']

            change_to_refund = round(transaction_value - m.MENU[drink]['cost'], 2)
            if change_to_refund > 0:
                print(f'Here is ${change_to_refund} in change.')
            self.make_drink(drink)

        else:
            print('Sorry that is not enough. Money Refunded')

    def perform_transaction_for_drink(self, drink):

        if self.enough_resources(drink):
            self.take_payment(drink)
            self.remove_resources(drink)


coffee_machine = CoffeeMachine()

while True:
    drinks_available = str(m.MENU.keys()).replace('dict_keys', '').replace('([', '').replace('])', '')
    user_command = str(input(f'what would you like?({drinks_available}): '))

    if user_command in m.MENU.keys():
        coffee_machine.perform_transaction_for_drink(user_command)
    elif user_command == 'report' or user_command == 'Off' or user_command == 'off':
        if user_command == 'report':
            coffee_machine.show_resources()
        else:
            coffee_machine.off()
    else:
        print(f'No drink available of {user_command}')
