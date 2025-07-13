
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
        return self.tinh_trang in ['sống', 'hạt mầm']

    @staticmethod
    def cham_cay(game_list):
        ten = input("Nhập tên cây: ")
        for cay in game_list:
            if cay.ten == ten and cay.check_tinh_trang():
                nuoc_tang_them = int(input("Nhập lượng nước tăng thêm: "))
                anh_sang_tang_them = int(input("Bạn sẽ cho cây ở ngoài trời mấy tiếng: "))
                if cay.nuoc is not None and cay.anh_sang is not None:
                    cay.gia_thanh = (nuoc_tang_them, anh_sang_tang_them)
                    print(f"Đã chăm sóc cây {cay.ten}")
                    return True
                else:
                    print("Cây đã bán hoặc không tồn tại. Hãy nhập lại tên")
                    return False
        print("Cây không tồn tại hoặc không còn sống, hãy nhập lại tên")
        return False

    @staticmethod
    def ban_cay(game_list):
        ten = input("Cây bán tên là: ")
        for cay in game_list:
            if cay.ten == ten and cay.check_tinh_trang():
                Game.tien += cay.gia_thanh
                del cay.gia_thanh
                print(f"Đã bán cây {ten} với giá {cay.gia_thanh} đồng")
                return True
        print("===== Hãy nhập lại tên =====")
        return False

    def get_info(self):
        return f"Cây {self.ten} có tình trạng là {self.tinh_trang}, chiều cao là: {self.gia_thanh} mm"


def main():
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
            if Game.tien >= 200:
                ten = input("Bạn muốn đặt cây tên là: ")
                game.append(Game(ten=ten))
                print(f"Bạn đã thêm cây {ten} thành công")
            else:
                print("Không đủ tiền để mua cây mới (cần 200 đồng)")
                
        elif choice == "2":
            if game:
                Game.cham_cay(game)
            else:
                print("Không có cây nào để chăm sóc")
                
        elif choice == "3":
            if game:
                Game.ban_cay(game)
            else:
                print("Không có cây nào để bán")
                
        elif choice == "4":
            if game:
                for i in range(len(game)):
                    print(f"{i+1}. {game[i].get_info()}")
            else:
                print("Không có cây nào")
                
        elif choice == "5":
            print("Cảm ơn bạn đã chơi!")
            break
        else:
            print("Lựa chọn không hợp lệ. Hãy chọn lại.")


if __name__ == "__main__":
    main()
