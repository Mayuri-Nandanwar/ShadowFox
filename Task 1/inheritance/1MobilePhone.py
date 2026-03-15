#Create inheritance using MobilePhone as base class and Apple & Samsung as child class 1. The base class should have properties: 1. ScreenType = Touch Screen
#2. NetworkType = 4G/5G, 3. DualSim = True or False, 4. FrontCamera = (5MP/8MP/12MP/16MP), 5. rearCamera = (8MP/12MP/16MP/32MP/48MP), 6. RAM = (2GB/3GB/4GB), 7. Storage = (16GB/32GB/64GB)

#Base Class
class MobilePhone:
    def __init__(self, ScreenType, NetworkType, DualSim, FrontCamera, RearCamera, RAM, Storage):
        self.ScreenType = ScreenType
        self.NetworkType = NetworkType
        self.DualSim = DualSim
        self.FrontCamera = FrontCamera
        self.RearCamera = RearCamera
        self.RAM = RAM
        self.Storage = Storage
        
    def Show_Details(self):
        print("Screen Type :", self.ScreenType)
        print("Network Type :", self.NetworkType)
        print("Dual Sim :", self.DualSim)
        print("Front Camera :", self.FrontCamera)
        print("Rear Camera :", self.RearCamera)
        print("RAM :", self.RAM)
        print("Storage :", self.Storage)
        
#Child class Apple
class Apple(MobilePhone):
    def __init__(self):
        super().__init__(
           "Touch Screen",
            "4G/5G",
            "False",
            "12MP",
            "48MP",
            "4GB",
            "64GB"
        )
# Child class Samsung
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

#create objects
iphone = Apple()
Galaxy = Samsung()

#print results
print("Apple phone Details :")
iphone.Show_Details()

print("\nSamsung phone details :")
Galaxy.Show_Details()

        
        