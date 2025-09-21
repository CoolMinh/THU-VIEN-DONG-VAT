import streamlit as st

# Cấu hình trang
st.set_page_config(page_title='Vương quốc mô hình', page_icon=':sparkles:')

# Sidebar
with st.sidebar:
    st.title('Vương quốc mô hình')
    st.header('Chào mừng bạn đến Vương quốc mô hình!')
    st.image('PYDC4.13/hinh1.jpg')
    st.write(
        'Chúng tôi chuyên bán các mô hình nhân vật hoạt hình chất lượng. '
        'Luôn cập nhật và đa dạng sản phẩm. Cam kết sự hài lòng của khách hàng '
        'với dịch vụ chuyên nghiệp. Hãy đến và khám phá thế giới mô hình tại Vương quốc mô hình!'
    )
    st.write(':house: :')
    st.write(':phone: 123456789')

# Tiêu đề chính
st.title('Vương quốc mô hình')

# Các nút chọn
col1, col2, col3 = st.columns(3)
with col1:
    b1 = st.button('Dragon Ball')
with col2:
    b2 = st.button('Naruto')
with col3:
    b3 = st.button('One Piece')

# Nếu chọn Dragon Ball
if b1:
    st.header('Danh sách mô hình Dragon Ball')
    col4, col5, col6 = st.columns(3)
    with col4:
        st.image('https://i.ebayimg.com/images/g/~W8AAOSwIYBmVZIn/s-l1600.webp', caption='Goku Ultra Instinct – Mã số: 001')
    with col5:
        st.image('https://i.pinimg.com/736x/dd/24/6a/dd246adc152d309e9121a69f0f90cd7c.jpg', caption='Vegeta Super Saiyan – Mã số: 002')
    with col6:
        st.image('https://i.pinimg.com/736x/d0/e5/cd/d0e5cdcccdd1ca646e1ed18d031d00d1.jpg', caption='Picolo – Mã số: 003')

# Nếu chọn Naruto
if b2:
    st.header('Danh sách mô hình Naruto')
    col4, col5, col6 = st.columns(3)
    with col4:
        st.image('https://i.pinimg.com/1200x/4d/06/c0/4d06c0f85dbd9993f4ac8df38d905e4e.jpg', caption='Uzumaki Naruto – Mã số: 001')
    with col5:
        st.image('https://i.pinimg.com/1200x/01/d9/4a/01d94a9fc24a88c3f2f57e2131236836.jpg', caption='Uchiha Sasuke – Mã số: 002')
    with col6:
        st.image('https://i.pinimg.com/1200x/79/2d/79/792d79fa394c4c9df660ab6885a78f75.jpg', caption='Hatake Kakashi – Mã số: 003')

# Nếu chọn One Piece
if b3:
    st.header('Danh sách mô hình One Piece')
    col4, col5, col6 = st.columns(3)
    with col4:
        st.image('https://i.pinimg.com/1200x/03/9e/c8/039ec8ba6235b336cad62f4d5ea9151a.jpg', caption='Monkey D. Luffy – Mã số: 001')
    with col5:
        st.image('https://i.pinimg.com/1200x/f4/ba/e1/f4bae1a40e2e3b89e5d3158108b425c8.jpg', caption='Roronoa Zoro – Mã số: 002')
    with col6:
        st.image('https://i.pinimg.com/736x/f1/96/e4/f196e41afd462282c6412e4aa05d4227.jpg', caption='Vinsmoke Sanji – Mã số: 003')

  st.header('Đặt hàng')
  with st.form('đơn đặt hàng'):

    topics = ('Dragon Ball', 'Naruto', 'One Piece')
    option_topic = st.selectbox('Chọn loại mô hình:', topics)

    codes = ('001', '002', '003')
    option_code = st.selectbox('Chọn mã số:', codes)



  nums = st.slider('Số lượng bạn muốn đặt:', 0, 10, 0)
  name = st.text_input('Họ và tên')
  phone = st.text_input('Số điện thoại nhà riêng')
  address = st.text_input('Địa chỉ giao hàng')


  option_topic = st.selectbox('Loại mô hình:', ['Robot', 'Xe hơi', 'Máy bay'])
  option_code = st.text_input('Mã số sản phẩm')


  bill = {
      'Loại mô hình:': option_topic,
      'Mã số:': option_code,
      'Số lượng:': nums,
      'Họ tên khách hàng:': name,
      'Số điện thoại liên hệ:': phone,
      'Địa chỉ giao hàng:': address
  }

  submitted = st.form_submit_button("Xác nhận")
  if submitted:
      st.header('Bạn đã chọn:')
      for x, y in bill.items():
          st.write(x, y)


  print_bill = st.checkbox('In hoá đơn')
  if print_bill:
      ans = ''
      for x in bill:
          ans += str(x) + ' ' + str(bill[x]) + '\n'
      st.download_button('In hoá đơn', ans)

