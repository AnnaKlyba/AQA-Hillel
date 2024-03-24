"""
Homework 11. Bank Card operations.

# write class for bank card.
# Class should reflect card lifecycle, card operations etc.
# use CVV, PIN, Name, Surname , end date, card_num as initial params
# class should have in addition to common logic some class attributes,
# as minimum one classmethod and as minimum  one staticmethod,
# two or more getters/setters, __str_ magic method
# do not forget about block if __name__ == '__main__':
# and code there to check your class written logic.
"""

import re
from datetime import datetime as dt
from random import SystemRandom as Sr

rand = Sr()


class CardOperations:
    """Card operations."""

    CVV_DIGITS = 3
    card_type = 'Standard'

    def __init__(self, cvv, card_num, end_date, surname, name, pin, money=0):
        """Has params."""
        self.__CVV = cvv if self.check_cvv(cvv) else str(rand.randint(1, 999)).zfill(3)
        self.__PIN = pin
        self.Name = name
        self.Surname = surname
        self.EndDate = end_date
        self.__Card_num = card_num if card_num else str(rand.randint(1, 9999999999999999)).zfill(12)
        self.Money = float(money)

    def check_pin(self):
        """Check pin code with 3 attempts."""
        att = 2
        while att >= 0:
            your_pin = input('Enter PIN:')
            if int(your_pin) == self.pin:
                return True
            else:
                print(f'Error, {att} attempts left')
                att -= 1
        return False

    def adding(self, money):
        """Refill."""
        self.Money += float(money)
        return float(self.Money)

    def withdraw(self, money):
        """Withdrawal from account."""
        if float(money) <= self.Money:
            self.Money -= float(money)
            return float(self.Money)
        else:
            raise ValueError('Not enough money')

    @classmethod
    def check_cvv(cls, cvv):
        cvv_pat = '^/d{' + str(cls.CVV_DIGITS) + '}$'
        return True if re.match(pattern=cvv_pat, string=str(cvv)) else False

    @property
    def cvv(self):
        return self.__CVV

    @property
    def pin(self):
        return self.__PIN

    def set_card_type(self, value):
        self.card_type = value

    @staticmethod
    def check_enddate(end_date):
        datetime = dt.now()
        return datetime < end_date

    @property
    def card_number(self):
        return str(self.__Card_num)[-4:]

    def get_data(self):
        """Checking data to obtain a card number."""
        entered_surname = input('Enter Surname: ')
        entered_name = input('Enter Name: ')

        if entered_name == self.Name and entered_surname == self.Surname:
            return self.card_number
        else:
            raise ValueError('Wrong Surname or name were defined')

    def __str__(self):
        """Return a string representation of the CardOperations object."""
        return f'{self.Name} {self.Surname} {self.card_number} {self.EndDate}'


if __name__ == '__main__':
    try:
        card = CardOperations(777, 1234123412341234, '2025-02-02',
                              'Shvets', 'Anna', 987, 100)

        if card.check_pin():
            card.set_card_type('Gold')
            print('Card type after change:', card.card_type)

            if card.check_enddate(dt(2026, 2, 2)):
                print('The card date is valid.')
            else:
                print('Card has expired.')

            refill_amount = input("Enter refill amount: ")
            card.adding(refill_amount)
            print("Refill successful. New balance:", card.Money)

            withdraw_amount = input("Enter withdrawal amount: ")
            card.withdraw(withdraw_amount)

            card_number = card.card_number
            if card_number:
                print('Card number:', card_number)
            else:
                print("The entered data doesn't match the data in the system.")
    except Exception as ex_h:
        print('An error occurred:', ex_h)
