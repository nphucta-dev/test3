"""
pet.py
------
Định nghĩa lớp Pet (Thú cưng) - kế thừa từ Companion.
Có thêm bonus_atk và kỹ năng tấn công đặc trưng.
"""

from companion import Companion


class Pet(Companion):
    def __init__(self, name, bonus_atk, level=1, **kwargs):
        self.bonus_atk = bonus_atk
        super().__init__(name=name, level=level, **kwargs)

    def unleash_skill(self):
        print(f"{self.name} gầm gừ: Tấn công kẻ thù, gây {self.bonus_atk} sát thương!")

    def __add__(self, other):
        # Bẫy 2: chỉ cho phép lai tạo 2 sinh vật CÙNG LOÀI (cùng kiểu chính xác)
        if type(self) != type(other):
            raise TypeError("Chỉ có thể lai tạo 2 sinh vật cùng loài!")
        new_name = f"{self.name} {other.name}"
        new_level = self.level + 1
        new_atk = self.bonus_atk + other.bonus_atk
        return Pet(new_name, new_atk, level=new_level)

    def info(self):
        return f"[Pet] {self.name} | Cấp: {self.level} | Atk: +{self.bonus_atk}"
