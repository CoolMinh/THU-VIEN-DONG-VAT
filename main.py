
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

    def get_info(self):
        return f"Tên: {self.ten}, Tình trạng: {self.tinh_trang}, Giá thành: {self.gia_thanh} vnd"

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
                    print(cay.get_info())
                    return True
                else:
                    print("Cây đã bán hoặc không tồn tại. Hãy nhập lại tên")
                    return False
        print("Cây không tồn tại hoặc không còn sống, hãy nhập lại tên")
        return False

    @staticmethod
    def ban_cay(game_list):
        ten = input("Nhập tên cây: ")
        for i, cay in enumerate(game_list):
            if cay.ten == ten and cay.check_tinh_trang():
                Game.tien += cay.gia_thanh
                del cay.gia_thanh
                print(f"Đã bán cây {ten} với giá {cay.gia_thanh} vnd")
                return True
        print('Cây không tồn tại hoặc không thể bán')
        return False

    @staticmethod
    def tao_cay():
        ten = input("Nhập tên cây mới: ")
        if Game.tien >= 200:
            return Game(ten)
        else:
            print("Không đủ tiền để mua cây mới")
            return None

    @staticmethod
    def hien_thi_tat_ca(game_list):
        if not game_list:
            print("Không có cây nào")
            return
        
        print("\n=== DANH SÁCH CÂY ===")
        for i, cay in enumerate(game_list):
            print(f"{i+1}. {cay.get_info()}")
        print(f"\nSố lượng cây: {Game.so_luong}")
        print(f"Tiền còn lại: {Game.tien} vnd")

def main():
    game = []
    
    while True:
        print("\n=== GAME TRỒNG CÂY ===")
        print("1. Tạo cây mới")
        print("2. Chăm sóc cây")
        print("3. Bán cây")
        print("4. Hiển thị tất cả cây")
        print("5. Thoát")
        
        try:
            lua_chon = int(input("Chọn một lựa chọn (1-5): "))
            
            if lua_chon == 1:
                cay_moi = Game.tao_cay()
                if cay_moi:
                    game.append(cay_moi)
                    print(f"Đã tạo cây {cay_moi.ten}")
                    
            elif lua_chon == 2:
                if game:
                    Game.cham_cay(game)
                else:
                    print("Không có cây nào để chăm sóc")
                    
            elif lua_chon == 3:
                if game:
                    Game.ban_cay(game)
                else:
                    print("Không có cây nào để bán")
                    
            elif lua_chon == 4:
                Game.hien_thi_tat_ca(game)
                
            elif lua_chon == 5:
                print("Cảm ơn bạn đã chơi!")
                break
                
            else:
                print("Lựa chọn không hợp lệ. Vui lòng chọn từ 1-5")
                
        except ValueError:
            print("Vui lòng nhập một số hợp lệ")
        except KeyboardInterrupt:
            print("\nTạm biệt!")
            break

if __name__ == "__main__":
    main()
