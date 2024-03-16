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

from datetime import datetime as dt
import re


class CardOperations:
    CVV_DIGITS = 3
    card_type = "Standard"


    def __init__(self, CVV, Card_num, EndDate, Surname, Name, PIN, Money):
        self.CVV = CVV if self.check_CVV(CVV) else "000"
        self.PIN = PIN
        self.Name = Name
        self.Surname = Surname
        self.EndDate = EndDate
        self.Card_num = Card_num
        self.Money = Money

    def check_pin(self):
        for att in (2,1,0):
            your_PIN = input('Enter PIN:')
            if int(your_PIN) == self.PIN:
                return True
            else:
                print(f"Error, {att} attempts left")
        return False

    def adding(self, Money):
        if Money > 0:
            self.Money += Money
            return True
        else:
            return 'Error'

    def print_balance(self):
        return self.Money

    @classmethod
    def check_CVV(cls, CVV):
        cvv_pattern = "^/d{" + str(cls.CVV_DIGITS) + "}$"
        return True if re.match(pattern=cvv_pattern, string=str(CVV)) else False

    def get_cvv(self):
        return self.CVV

    def set_card_type(self, value):
        self.card_type = value

    @staticmethod
    def check_EndDate(EndDate):
        datetime = dt.now()
        return datetime < EndDate

    def get_card_number(self):
        entered_surname = input('Enter Surname: ')
        entered_name = input('Enter Name: ')

        if entered_name == self.Name and entered_surname == self.Surname:
            return self.Card_num
        else:
            return None

    def __str__(self):
        """Returns a string representation of the CardOperations object."""
        return f"{self.Name} {self.Surname} {self.Card_num} {self.CVV} {self.EndDate}"


if __name__ == "__main__":
    try:
        card = CardOperations(777,1234123412341234,'2025-02-02',
                                 'Shvets', 'Anna', 987, 100)

        if card.check_pin():

            card.set_card_type("Gold")
            print("Card type after change:", card.card_type)

            if card.check_EndDate(dt(2026, 2, 2)):
                print("The card date is valid.")
            else:
                print("Card has expired.")

            card_number = card.get_card_number()
            if card_number:
                print("Card number:", card_number)
            else:
                print("The entered data doesn't match the data in the system.")
    except Exception as ex_h:
        print("An error occurred:", ex_h)
