class game:
  tien=5000
  so_luong=0

  def __init__(self,ten):
    self.ten=ten
    self.nuoc=0
    self.anh_sang=0
    game.so_luong+=1
    game.tien-=200

  @property
  def tinh_trang(self):
    if (self.nuoc==none and self.anh_sang=none):
      return "đã bán"
    elif (self.nuoc==0 and self.anh_sang==0):
      return 'hạt mầm'
    elif (self.nuoc>0 and self.anh_sang>0):
      return 'sống'
    else: return 'chết'
    
  @property
  def gia_thanh(self,value):
    if (self.nuoc==none and self.anh_sang==none)
      return 0
    return max(0,self.nuoc+self.anh_sang*10)
  @gia_thanh.setter
  def gia_thanh(self.value):
    nuoc_tang_them,anh_sang_tang_them=Value
    if (nuoc_tang_them>100 or anh_sang_tang_them>10):
      self.nuoc=-1
      self.anh_sang=-1
    elif self.check_tinh_trang():
      self.nuoc+=nuoc_tang_them
      self.anh_sanh+=anh_sang_tang_them

  @gia_thanh.deleter
  def gia_thanh(self):
    self.nuoc=none
    self.anh_sang=none

  @saticmethod
  def ban_cay():
    ten=input('day')