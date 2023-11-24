# OOP

class IotSAU :
    # data/property/field/attribute
    major = "SAU"
    name = ""

    # method (มันคือ Funciton แต่เราไม่เรียกฟังก์ชั่น)
    def showHi(self) :
        print('Hi....')

    def introduceMySelf(self) :
        print(f'My name is {self.name}')        
        print(f'My major is {self.major}')        

# --------------------------------------------------------
# สร้าง Object
obA = IotSAU() #เป็นการเรียกใข้ constructor ของคลาสให้ทำงาน (ถ้ามี)
obB = IotSAU()


# การใช้งาน data ของ object คือ เอาค่ามันมาใช้ หรือ เปลี่ยนค่าให้มันใหม่
print(obA.major)
obA.major = "Wow"
obA.major = "ฟ้าร้อง"
obB.major = "ฝนตกแล้ว"

# การใช้งาน method ของ object คือ สั่งให้เมธอดของ object นั้นๆ ทำงาน
obA.introduceMySelf()
obB.introduceMySelf()