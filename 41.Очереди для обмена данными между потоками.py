import queue
import time
import threading


class Table:
    def __init__(self, number):
        self.number = number
        self.is_busy = False


class Cafe:

    def __init__(self, tables):
        self.queue = queue.Queue()
        self.tables = tables

    def customer_arrival(self):
        customer_number = 1
        while customer_number <= 5:
            print(f"Посетитель номер {customer_number} прибыл.")
            customer = Customer(customer_number, self)
            Cafe.serve_customer(self, customer)
            customer_number += 1
            time.sleep(1)

    def serve_customer(self, customer):
        for table in self.tables:
            if not table.is_busy and self.queue.empty():
                return customer.start()

        print(f"Посетитель номер {customer.number} ожидает свободный стол.")
        return self.queue.put(customer)


class Customer(threading.Thread):
    def __init__(self, number, cafe):
        super().__init__()
        self.number = number
        self.cafe = cafe

    def run(self):
        for table in self.cafe.tables:
            if not table.is_busy:
                table.is_busy = True
                print(f"Посетитель номер {self.number} сел за стол {table.number}.")
                time.sleep(5)
                print(f"Посетитель номер {self.number} покушал и ушёл.")
                table.is_busy = False
                break
        if not self.cafe.queue.empty():
            next_customer = cafe.queue.get()
            next_customer.start()
            self.cafe.queue.task_done()
            self.cafe.queue.join()


# Создаем столики в кафе
table1 = Table(1)
table2 = Table(2)
table3 = Table(3)
tables = [table1, table2, table3]

# Инициализируем кафе
cafe = Cafe(tables)

# Запускаем поток для прибытия посетителей
customer_arrival_thread = threading.Thread(target=cafe.customer_arrival)
customer_arrival_thread.start()

# Ожидаем завершения работы прибытия посетителей
customer_arrival_thread.join()
