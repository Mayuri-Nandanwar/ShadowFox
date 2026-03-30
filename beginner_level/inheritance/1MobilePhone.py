#Create inheritance using MobilePhone as base class and Apple & Samsung as child class 1. The base class should have properties: 1. ScreenType = Touch Screen
#2. NetworkType = 4G/5G, 3. DualSim = True or False, 4. FrontCamera = (5MP/8MP/12MP/16MP), 5. rearCamera = (8MP/12MP/16MP/32MP/48MP), 6. RAM = (2GB/3GB/4GB), 7. Storage = (16GB/32GB/64GB)

# Base class
class MobilePhone:
    def __init__(self, screen_type, network_type, dual_sim, front_camera, rear_camera, ram, storage):
        self.screen_type = screen_type
        self.network_type = network_type
        self.dual_sim = dual_sim
        self.front_camera = front_camera
        self.rear_camera = rear_camera
        self.ram = ram
        self.storage = storage

    def show_details(self):
        print("Screen Type:", self.screen_type)
        print("Network Type:", self.network_type)
        print("Dual SIM:", self.dual_sim)
        print("Front Camera:", self.front_camera)
        print("Rear Camera:", self.rear_camera)
        print("RAM:", self.ram)
        print("Storage:", self.storage)


# Apple class
class Apple(MobilePhone):
    def __init__(self):
        super().__init__(
            "Touch Screen",
            "4G/5G",
            False,
            "12MP",
            "48MP",
            "4GB",
            "64GB"
        )


# Samsung class
class Samsung(MobilePhone):
    def __init__(self):
        super().__init__(
            "Touch Screen",
            "4G/5G",
            True,
            "16MP",
            "48MP",
            "4GB",
            "64GB"
        )


# creating objects
apple_phone = Apple()
samsung_phone = Samsung()

# displaying details
print("Apple Phone Details:")
apple_phone.show_details()

print("\nSamsung Phone Details:")
samsung_phone.show_details()