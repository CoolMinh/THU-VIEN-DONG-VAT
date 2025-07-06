
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
    def ban_cay():
        ten = input("Nhập tên cây: ")
        return ten

# Example usage
if __name__ == "__main__":
    cay = Game("Hoa hồng")
    print(f"Tên cây: {cay.ten}")
    print(f"Tình trạng: {cay.tinh_trang}")
    print(f"Giá thành: {cay.gia_thanh}")
    print(f"Số lượng cây: {Game.so_luong}")
    print(f"Tiền còn lại: {Game.tien}")
