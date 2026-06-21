from companion import Companion
from pet import Pet
from mount import Mount
from dragon import Dragon


def test_trap_1_abstract_class():
    """Bẫy 1: không thể khởi tạo trực tiếp lớp trừu tượng Companion."""
    print("=== KIỂM TRA BẪY 1: Khởi tạo trực tiếp lớp trừu tượng Companion ===")
    try:
        Companion("Test")
    except TypeError as e:
        print(f"Đã chặn thành công -> TypeError: {e}")


def test_breeding_and_trap_2():
    """Chức năng 4 (lai tạo) + Bẫy 2 (chỉ lai tạo cùng loài)."""
    print("\n=== TẠO PET & LAI TẠO (Chức năng 4) ===")
    p1 = Pet("Sói Trắng", bonus_atk=50)
    p2 = Pet("Sói Đen", bonus_atk=60)
    p3 = p1 + p2
    print(f">> Lai tạo thành công! Nhận được: {p3.info()}")

    print("\n=== KIỂM TRA BẪY 2: Lai tạo sai loại (Pet + Mount, Pet + số) ===")
    m1 = Mount("Ngựa", bonus_speed=10)
    try:
        p1 + m1
    except TypeError as e:
        print(f"Đã chặn thành công (Pet + Mount) -> TypeError: {e}")
    try:
        p1 + 10
    except TypeError as e:
        print(f"Đã chặn thành công (Pet + số nguyên) -> TypeError: {e}")

    return p3, m1


def test_trap_3_dragon():
    """Bẫy 3: đa kế thừa Dragon(Pet, Mount) phải giữ đủ cả 2 chỉ số."""
    print("\n=== KIỂM TRA BẪY 3: Đa kế thừa Dragon(Pet, Mount) ===")
    d1 = Dragon("Rồng Lửa", bonus_atk=500, bonus_speed=200)
    print(f"Rồng Lửa khởi tạo đầy đủ -> Atk: {d1.bonus_atk} | Speed: {d1.bonus_speed}")
    return d1


def show_team(team):
    """Chức năng 1: xem đội hình sinh vật."""
    print("\n=== XEM ĐỘI HÌNH (Đa hình - in info từng loại) ===")
    for idx, companion in enumerate(team, start=1):
        print(f"{idx}. {companion.info()}")


def battle(team):
    """Chức năng 5: xuất chiến - gọi đồng nhất unleash_skill() (Đa hình)."""
    print("\n=== XUẤT CHIẾN (Đa hình - Chức năng 5) ===")
    for companion in team:
        companion.unleash_skill()


def main():
    test_trap_1_abstract_class()
    p3, m1 = test_breeding_and_trap_2()
    d1 = test_trap_3_dragon()

    equipped = [p3, m1, d1]
    show_team(equipped)
    battle(equipped)


if __name__ == "__main__":
    main()