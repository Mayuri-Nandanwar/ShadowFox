#Create basic mobile phone functionalities in the classes like: make_call, recieve_call, take_a_picture, etc.

# Base class
class MobilePhone:
    def __init__(self, brand_name, screen_type, network_type, dual_sim, front_camera, rear_camera, RAM, storage):
        self.brand_name = brand_name
        self.screen_type = screen_type
        self.network_type = network_type
        self.dual_sim = dual_sim
        self.front_camera = front_camera
        self.rear_camera = rear_camera
        self.RAM = RAM
        self.storage = storage

    # Basic mobile functions
    def make_call(self, number):
        print(self.brand_name, "is calling", number)

    def receive_call(self):
        print(self.brand_name, "is receiving a call")

    def take_picture(self):
        print(self.brand_name, "is taking a picture using", self.rear_camera)

    def show_phone_details(self):
        print("\nBrand:", self.brand_name)
        print("Screen Type:", self.screen_type)
        print("Network:", self.network_type)
        print("Dual SIM:", self.dual_sim)
        print("Front Camera:", self.front_camera)
        print("Rear Camera:", self.rear_camera)
        print("RAM:", self.RAM)
        print("Storage:", self.storage)


# Apple class (child class)
class Apple(MobilePhone):
    def __init__(self, screen_type, network_type, dual_sim, front_camera, rear_camera, ram, storage):
        super().__init__("Apple", screen_type, network_type, dual_sim, front_camera, rear_camera, ram, storage)


# Samsung class (child class)
class Samsung(MobilePhone):
    def __init__(self, screen_type, network_type, dual_sim, front_camera, rear_camera, ram, storage):
        super().__init__("Samsung", screen_type, network_type, dual_sim, front_camera, rear_camera, ram, storage)


# Create Apple objects
applephone1 = Apple("Touch Screen", "5G", False, "12MP", "48MP", "4GB", "64GB")
applephone2 = Apple("Touch Screen", "5G", False, "16MP", "32MP", "4GB", "128GB")

# Create Samsung objects
samsungphone1 = Samsung("Touch Screen", "5G", True, "16MP", "48MP", "4GB", "64GB")
samsungphone2 = Samsung("Touch Screen", "4G/5G", True, "12MP", "32MP", "3GB", "32GB")


# Display details
applephone1.show_phone_details()
applephone2.show_phone_details()
samsungphone1.show_phone_details()
samsungphone2.show_phone_details()


# Using functions
applephone1.make_call("9876543210")
samsungphone1.receive_call()
samsungphone2.take_picture()