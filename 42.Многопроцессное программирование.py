import multiprocessing


class WarehouseManager:
    def __init__(self):
        manager = multiprocessing.Manager()
        self.data = manager.dict()

    def process_request(self, request):
        product, action, quantity = request
        if action == "receipt":
            if product in self.data:
                self.data[product] += quantity
            else:
                self.data[product] = quantity
        elif action == "shipment":
            if product in self.data and self.data[product] > 0:
                self.data[product] -= quantity
                if self.data[product] == 0:
                    del self.data[product]

    def run(self, requests):
        for request in requests:
            p = multiprocessing.Process(target=self.process_request, args=(request,))
            p.start()
            p.join()


# Создаем менеджера склада
manager = WarehouseManager()

# Множество запросов на изменение данных о складских запасах
requests = [
    ("product1", "receipt", 100),
    ("product2", "receipt", 150),
    ("product1", "shipment", 30),
    ("product3", "receipt", 200),
    ("product2", "shipment", 50),
]

# Запускаем обработку запросов
manager.run(requests)

# Выводим обновленные данные о складских запасах
print(manager.data)
