import random


def get_random_digits(count: int) -> str:
    result = ' '
    for i in range(count):
        result += str(random.randint(0, 9))
    return result


class BankAccount:
    def __init__(self, card_holder):
        self.card_holder = card_holder.upper()
        self.money = 0
        self.account_number = get_random_digits(20)
        self.card_number = get_random_digits(16)


class Bank:
    def __init__(self):
        self.bank_accounts: dict[str, BankAccount] = {}

    def open_account(self, card_holder):
        account = BankAccount(card_holder)
        self.bank_accounts[account.account_number] = account
        return account

    def add_money(self, account_number, money):
        account = self.bank_accounts[account_number]
        account.money += money

    def transfer_money(self, from_account_number, to_account_number, money):
        from_account = self.bank_accounts[from_account_number]
        from_account -= money
        to_account = self.bank_accounts[to_account_number]
        to_account += money

    def external_transfer(self, from_account_number, to_external_number, money):
        from_account = self.bank_accounts[from_account_number]
        from_account -= money
        print('Банк перевёл ' + money + 'с вашего счёта' + from_account_number + 'на внешний счёт' + to_external_number)


class Controller:
    def __init__(self):
        self.bank = Bank()

    def run(self):
        print('Здравствуйте, наш банк открылся!')
        while True:
            print('Выберите действие: ')
            print('0. Завершить программу')
            print('1. Открыть новый счёт')
            print('2. Просмотреть открытые счета')
            print('3. Положить деньги на счёт')
            print('4. Перевести деньги между счетами')
            print('5. Совершить платёж')

            user_answer = int(input())
            if user_answer == 0:
                print('До свидания!')
                break
            elif user_answer == 1:
                cart_holder = input('Введите имя и фамилию держателя карты (на английском): ')
                account = self.bank.open_account(cart_holder)
                print(f'Счёт {account.account_number} создан ')


            elif user_answer == 2:
                self.show_accounts()
            elif user_answer == 3:
                account_number = input('Введите номер счёта: ')
                money = float(input(f'Количество денег: '))
                self.bank.add_money(account_number, money)
            elif user_answer == 4:
                from_account_number = input('Введите номер счёта-отправителя: ')
                to_account_number = input('Введите номер счёта-получателя:')
                money = float(input(f'Количество денег: '))
                self.bank.external_transfer(from_account_number, to_account_number, money)
            elif user_answer == 5:
                from_account_number = input('Введите номер счёта-отправителя: ')
                to_external_number = input(' Введите номер счёта внешнего получателя:')
                money = float(input(f'Количество денег: '))
                self.bank.external_transfer(from_account_number, to_external_number, money)
            else:
                print('Не поддерживаемая опреация')
            print()

    def show_accounts(self):
        print('Ваши открытые счета: ')
        for account_number, account in self.bank.bank_accounts.items():
            print(f'Счёт : {account_number}')
            print(f'Остаток на счету: {account.money}$')
            print(f'Номер карты: {account.card_number}')
            print(f'Держатель карты: {account.card_holder}')


if __name__ == '__main__':
    controller = Controller()
    controller.run()
