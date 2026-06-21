"""
companion.py
------------
Định nghĩa lớp trừu tượng (Abstract Base Class) Companion - khuôn mẫu chung
cho mọi sinh vật đồng hành trong game (Pet, Mount, Dragon...).

Mọi sinh vật đều có name, level và bắt buộc phải tự định nghĩa unleash_skill().
Kế thừa ABC để Python tự chặn việc khởi tạo trực tiếp Companion (Bẫy 1).
"""

from abc import ABC, abstractmethod


class Companion(ABC):
    def __init__(self, name, level=1, **kwargs):
        self.name = name
        self.level = level
        # super().__init__(**kwargs) để lớp này tham gia an toàn vào chuỗi
        # đa kế thừa (MRO) khi được dùng bởi Dragon(Pet, Mount) - xem dragon.py
        super().__init__(**kwargs)

    @abstractmethod
    def unleash_skill(self):
        """Bắt buộc mọi lớp con phải tự định nghĩa kỹ năng đặc trưng."""
        pass

    def info(self):
        return f"{self.name} | Cấp: {self.level}"
