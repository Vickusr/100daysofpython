import menu as m
"""Coffee machine example"""
"""Basic design is to have all values in a dictionary form and use them as needed """


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

    # have to first check if there are enough resources in the machine to be sure
    # that the transaction can even take place

    def enough_resources(self, drink):

        for r in m.MENU[drink]['ingredients']:

            if m.MENU[drink]['ingredients'][r] > self.resources[r]:
                print(f'Not enough {r}')
                return False

        return True

    # after the main transaction happens we need to remove the resource required from the drink

    def remove_resources(self, drink):
        for r in m.MENU[drink]['ingredients']:
            self.resources[r] -= m.MENU[drink]['ingredients'][r]

    @staticmethod
    def make_drink(drink_name):
        print(f'Making {drink_name}')

    # method to handle payment and refund where and if necessary
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
            return True

        else:
            print('Sorry that is not enough. Money Refunded')
            return False

    def perform_transaction_for_drink(self, drink):

        if self.enough_resources(drink):
            if self.take_payment(drink):
                self.remove_resources(drink)


# initiate the coffee machine
coffee_machine = CoffeeMachine()

# run
while coffee_machine.status == 'On':
    # concat the drinks so if more drinks are added we can simple show them
    # and will be catered for in design
    drinks_available = str(m.MENU.keys()).replace('dict_keys', '').replace('([', '').replace('])', '')
    user_command = str(input(f'what would you like?({drinks_available}): ')).lower()

    if user_command in m.MENU.keys():
        coffee_machine.perform_transaction_for_drink(user_command)
    elif user_command == 'report' or user_command == 'Off' or user_command == 'off':
        if user_command == 'report':
            coffee_machine.show_resources()
        else:
            coffee_machine.off()
    else:
        print(f'No drink or command available of {user_command}')
