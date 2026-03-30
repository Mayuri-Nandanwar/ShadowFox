#Create basic mobile phone functionalities in the classes like: make_call, recieve_call, take_a_picture, etc.

# base class
class MobilePhone:
    def __init__(self, brand, screen, network, sim, front_cam, rear_cam, ram, storage):
        self.brand = brand
        self.screen = screen
        self.network = network
        self.sim = sim
        self.front_cam = front_cam
        self.rear_cam = rear_cam
        self.ram = ram
        self.storage = storage

    # basic functions
    def make_call(self, number):
        print(self.brand, "is calling", number)

    def receive_call(self):
        print(self.brand, "is receiving a call")

    def take_picture(self):
        print(self.brand, "is taking a picture with", self.rear_cam)

    def show_details(self):
        print("\nBrand:", self.brand)
        print("Screen:", self.screen)
        print("Network:", self.network)
        print("Dual SIM:", self.sim)
        print("Front Camera:", self.front_cam)
        print("Rear Camera:", self.rear_cam)
        print("RAM:", self.ram)
        print("Storage:", self.storage)


# Apple class
class Apple(MobilePhone):
    def __init__(self, screen, network, sim, front_cam, rear_cam, ram, storage):
        super().__init__("Apple", screen, network, sim, front_cam, rear_cam, ram, storage)


# Samsung class
class Samsung(MobilePhone):
    def __init__(self, screen, network, sim, front_cam, rear_cam, ram, storage):
        super().__init__("Samsung", screen, network, sim, front_cam, rear_cam, ram, storage)


# creating Apple objects
apple1 = Apple("Touch Screen", "5G", False, "12MP", "48MP", "4GB", "64GB")
apple2 = Apple("Touch Screen", "5G", False, "16MP", "32MP", "4GB", "128GB")

# creating Samsung objects
samsung1 = Samsung("Touch Screen", "5G", True, "16MP", "48MP", "4GB", "64GB")
samsung2 = Samsung("Touch Screen", "4G/5G", True, "12MP", "32MP", "3GB", "32GB")


# showing details
apple1.show_details()
apple2.show_details()
samsung1.show_details()
samsung2.show_details()


# using functions
apple1.make_call("9876543210")
samsung1.receive_call()
samsung2.take_picture()