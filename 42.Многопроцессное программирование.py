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
                print(product)
            else:
                self.data[product] = quantity
        elif action == "shipment":
            if product in self.data and self.data[product] > 0:
                self.data[product] -= quantity
                if self.data[product] <= 0:
                    del self.data[product]

    def run(self, requests):
        for req in requests:
            p = multiprocessing.Process(target=self.process_request, args=(req,))
            p.start()
            p.join()


if __name__ == '__main__':
    manager = WarehouseManager()
    requests = [
        ("product1", "receipt", 100),
        ("product2", "receipt", 150),
        ("product1", "shipment", 30),
        ("product3", "receipt", 200),
        ("product2", "shipment", 50),
    ]
    manager.run(requests)
    print(manager.data)
