lst = list(map(int, input("Nhập danh sách số nguyên, cách nhau bởi dấu phẩy: ").split(',')))
average = sum(lst) / len(lst) if lst else 0
print("Giá trị trung bình của danh sách là : ", average)

