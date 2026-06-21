"""
dragon.py
---------
Định nghĩa lớp Dragon - đa kế thừa từ cả Pet và Mount, sở hữu đồng thời
cả hai chỉ số (bonus_atk, bonus_speed) và thi triển cả hai kỹ năng.

Không cần viết lại __init__: nhờ cơ chế kwargs + super() hợp tác đã thiết
kế sẵn trong Pet, Mount và Companion, MRO sẽ tự chạy theo thứ tự
Dragon -> Pet -> Mount -> Companion -> ABC -> object, đảm bảo cả hai
chỉ số đều được gán đầy đủ (vượt Bẫy 3 - Nút thắt MRO).
"""

from pet import Pet
from mount import Mount


class Dragon(Pet, Mount):
    def unleash_skill(self):
        print(f"{self.name} thị uy:")
        print(f"   - Tấn công kẻ thù, gây {self.bonus_atk} sát thương!")
        print(f"   - Tăng tốc độ di chuyển thêm {self.bonus_speed} điểm!")

    def info(self):
        return (f"[Dragon] {self.name} | Cấp: {self.level} | "
                f"Atk: +{self.bonus_atk} | Speed: +{self.bonus_speed}")
