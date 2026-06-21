"""
mount.py
--------
Định nghĩa lớp Mount (Thú cưỡi) - kế thừa từ Companion.
Có thêm bonus_speed và kỹ năng tăng tốc đặc trưng.
"""

from companion import Companion


class Mount(Companion):
    def __init__(self, name, bonus_speed, level=1, **kwargs):
        self.bonus_speed = bonus_speed
        super().__init__(name=name, level=level, **kwargs)

    def unleash_skill(self):
        print(f"{self.name} hí vang: Tăng tốc độ di chuyển thêm {self.bonus_speed} điểm!")

    def __add__(self, other):
        if type(self) != type(other):
            raise TypeError("Chỉ có thể lai tạo 2 sinh vật cùng loài!")
        new_name = f"{self.name} {other.name}"
        new_level = self.level + 1
        new_speed = self.bonus_speed + other.bonus_speed
        return Mount(new_name, new_speed, level=new_level)

    def info(self):
        return f"[Mount] {self.name} | Cấp: {self.level} | Speed: +{self.bonus_speed}"
