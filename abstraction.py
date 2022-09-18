from abc import ABC, abstractmethod
class laptop(ABC):
    def purchase(self, amount):
        print("Your purchase amount: ",amount)

    @abstractmethod
    def payment(self,amount):
        pass


class VoucherPayment(laptop):
    def payment(self,amount):
        print('Your purchase amount of {} is covered by $100 vocher '.format(amount))

obj = VoucherPayment()
obj.purchase("$300")
obj.payment("$300")
