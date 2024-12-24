# Đọc dữ liệu từ file sach.txt và ghi kết quả vào ketqua.txt
def filter_books():
    try:
        # Đọc dữ liệu từ file sach.txt
        with open('sach.txt', 'r', encoding='utf-8') as file:
            books = file.readlines()

        # Danh sách lưu trữ các cuốn sách thỏa mãn điều kiện
        filtered_books = []

        # Duyệt qua từng cuốn sách (mỗi cuốn sách có 3 dòng)
        for i in range(0, len(books), 3):
            name = books[i].strip()            # Tên sách
            pages = int(books[i + 1].strip())  # Số trang
            price = int(books[i + 2].strip())  # Giá tiền

            # Kiểm tra điều kiện (giá tiền > 100000 và số trang < 200)
            if price > 100000 and pages < 200:
                filtered_books.append(f"{name} - {pages} trang - {price} VNĐ")

        # Ghi kết quả vào file ketqua.txt
        with open('ketqua.txt', 'w', encoding='utf-8') as result_file:
            for book in filtered_books:
                result_file.write(book + '\n')

        print("Hoàn thành lọc sách và ghi vào ketqua.txt")

    except Exception as e:
        print(f"Lỗi: {e}")

# Gọi hàm để thực hiện
filter_books()
