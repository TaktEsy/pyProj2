import threading, random

class Bank:
    balance = 0
    lock = threading.Lock()


    def deposit(self):

        for i in range(1,101):
            r = random.randint(50,500)
            self.balance += r
            print(f'#{i} | Пополнение: {r} | Баланс: {self.balance}\n')

        if self.balance >= 500 and self.lock.locked():
            self.lock.release()

    def take(self):
        for i in range(1,101):
            r = random.randint(50, 500)
            print(f"Запрос на {r}")

            if r <= self.balance:
                self.balance -= r
                print(f'№{i} | Снятие: {r} | Баланс: {self.balance}\n')
            else:
                print('Запрос отклонен, недостаточно средств')
                self.lock.acquire()


bk = Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))
th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')

# import threading
# counter = 0
# l = threading.Lock()
# def increment(name):
#     global counter
#     l.acquire()
#
#     for i in range(0,1000):
#         counter += 1
#         print(f"\n{name, counter}")
#     l.release()
# def decrement(name):
#     global counter
#     l.acquire()
#
#     for i in range(0,1000):
#         counter -= 1
#         print(f"\n{name, counter}")
#     l.release()
#
#
# t1 = threading.Thread(target=increment, args=('t1',))
# t2 = threading.Thread(target=decrement, args=('t2',))
# t3 = threading.Thread(target=increment, args=('t3',))
# t4 = threading.Thread(target=decrement, args=('t4',))
#
# t1.start()
# t2.start()
# t3.start()
# t4.start()