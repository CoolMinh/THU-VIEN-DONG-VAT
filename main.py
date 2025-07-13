
class Game:
    tien = 5000
    so_luong = 0

    def __init__(self, ten):
        self.ten = ten
        self.nuoc = 0
        self.anh_sang = 0
        Game.so_luong += 1
        Game.tien -= 200

    @property
    def tinh_trang(self):
        if self.nuoc is None and self.anh_sang is None:
            return "đã bán"
        elif self.nuoc == 0 and self.anh_sang == 0:
            return 'hạt mầm'
        elif self.nuoc > 0 and self.anh_sang > 0:
            return 'sống'
        else:
            return 'chết'
    
    @property
    def gia_thanh(self):
        if self.nuoc is None and self.anh_sang is None:
            return 0
        return max(0, self.nuoc + self.anh_sang * 10)
    
    @gia_thanh.setter
    def gia_thanh(self, value):
        nuoc_tang_them, anh_sang_tang_them = value
        if nuoc_tang_them > 100 or anh_sang_tang_them > 10:
            self.nuoc = -1
            self.anh_sang = -1
        elif self.check_tinh_trang():
            self.nuoc += nuoc_tang_them
            self.anh_sang += anh_sang_tang_them

    @gia_thanh.deleter
    def gia_thanh(self):
        self.nuoc = None
        self.anh_sang = None

    def check_tinh_trang(self):
        return self.tinh_trang == 'sống' or self.tinh_trang == 'hạt mầm'

    @staticmethod
    def cham_cay():
        ten = input("Nhập tên cây: ")
        for i in range(Game.so_luong):
            if game[i].ten == ten and game[i].check_tinh_trang():
                nuoc_tang_them = int(input("Nhập lượng nước tăng thêm: "))
                anh_sang_tang_them = int(input("bạn sẽ cho cây ở ngoài trời mấy tiếng: "))
                if game[i].nuoc is not None and game[i].anh_sang is not None:
                    game.[i].gia_thanh = (nuoc_tang_them, anh_sang_tang_them)
                    print(game[1])
                    return True
                else:
                    print("cây đã bán hoặc không tồn tại.hãy nhập lai tên")
                    return False
        print("cây không tồn tại hoặc không còn sống,hãy nhập lại tên")
        return False
    @staticmethod
    def ban_cay():
        ten = input("Cây bán tên là: ")
        for i in range(Game.so_luong):
            if game[i].ten == ten and game[i].check_tinh_trang():
                del game[i].gia_thanh
                break
        else:
            print("===== Hãy nhập lại tên =====")
            return False
        return True

    def check_tinh_trang(self):
        if self.tinh_trang == 'sống' or 'hạt mầm':
            return True
        else:
            return False

    def get_info(self):
        return f"Cây {self.ten} có tình trạng là {self.tinh_trang}, chiều cao là: {self.gia_thanh} mm"

    game = []
    while True:
        print("Chọn một trong các tùy chọn sau:")
        print("1. Thêm cây mới")
        print("2. Chăm sóc cây")
        print("3. Bán cây")
        print("4. Xem danh sách các cây")
        print("5. Thoát chương trình")
        print(f"Bạn đang có {Game.tien} đồng")

        choice = input("Nhập lựa chọn của bạn (1-5): ")
        if choice == "1":
            ten = input("Bạn muốn đặt cây tên là: ")
            game.append(Game(ten=ten))
            print(f"Bạn đã thêm cây {ten} thành công")
        elif choice == "2":
            Game.cham_cay()
        elif choice == "3":
            Game.ban_cay()
        elif choice == "4":
            for i in range(Game.so_luong):
                print(f"{i+1}. {game[i].get_info()}")
        elif choice == "5":
            break
        else:
            print("Lựa chọn không hợp lệ. Hãy chọn lại.")


