class Account:
    def __init__ (self, firstname, lastname, account_number, money, currency):
        self.firstname = firstname
        self.lastname = lastname
        self.account_number = account_number
        self.money = money
        self.currency = currency

    def display_account(self):
        print(f'Owner: {self.firstname} {self.lastname} Account number: {self.account_number} Status: {self.money} {self.currency}')

    def input_money(self):
        old_status = self.money
        print(old_status)
        money_in = int(input('How much in: '))
        self.money = old_status + money_in
        print(self.money)
        print(f'Owner: {self.firstname} {self.lastname} Account number: {self.account_number} Status: {self.money} {self.currency}')

    def output_money(self):
        old_status = self.money
        print(old_status)
        money_out = int(input('How much out: '))
        if money_out > old_status:
            print('Not enough money!')
        elif money_out > 1000:
                print('Cannot pay out more than 1000 zl at a time!')
        else:
            self.money = old_status - money_out
            print(self.money)
            print(f'Owner: {self.firstname} {self.lastname} Account number: {self.account_number} Status: {self.money} {self.currency}')

    def transfer_input_money(self, amount):
        old_status = self.money
        money_in = int(amount)
        self.money = old_status + money_in
        print(f'Owner: {self.firstname} {self.lastname} Account number: {self.account_number} Status: {self.money} {self.currency}')

    def transfer_output_money(self, amount):
        old_status = self.money
        money_out = int(amount)
        if money_out > old_status:
            print('Not enough money!')
        elif money_out > 1000:
                print('Cannot pay out more than 1000 zl at a time!')
        else:
            self.money = old_status - money_out
            print(f'Owner: {self.firstname} {self.lastname} Account number: {self.account_number} Status: {self.money} {self.currency}')

    def TransferMoney(self):
        for i in self.lastname:
            money_from = input('Money from: ')
            if money_from == self.lastname:
                account_A = self.money
                print(account_A)
                transfer = int(input('How much to transfer: '))
                if transfer > account_A:
                    print('Not enough money')
                else:
                    account_A = account_A - transfer
                    print(account_A)
            else:
                print('No such person exists')
        for i in self.lastname:
            money_to = input('Money to: ')
            if money_to == self.lastname:
                account_B = self.money
                print(account_B)
                account_A = account_A - transfer
                print(account_A)
            else:
                print('No such person exists')


def transfer_money(sender, receiver, amount):
    print('Transfer', amount, sender.currency, 'z konta', sender.lastname, 'na konto',
          receiver.lastname)
    sender.transfer_output_money(amount)
    receiver.transfer_input_money(amount)


if __name__ == '__main__':



    Kowalska = Account('Pola', 'Kowalska', 889990, 500, 'zl')
    Pawlowski = Account('Adam', 'Pawlowski', 944523, 700, 'zl')

    Kowalska.display_account()

    Kowalska.input_money()

    Kowalska.output_money()

    print('Stan konta Kowalska przed transferem:', Kowalska.money)
    print('Stan konta Pawlowski przed transferem:', Pawlowski.money)

    transfer_money(Kowalska, Pawlowski, 100)

    print('Stan konta Kowalska po transferze:', Kowalska.money)
    print('Stan konta Pawlowski po transferze:', Pawlowski.money)





