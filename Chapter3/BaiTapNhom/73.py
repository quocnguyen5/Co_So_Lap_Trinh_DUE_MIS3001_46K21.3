s = str(input('Nhập một chuỗi: '))
s = s.lower()  # Hàm chuyển thành chữ thường nếu có chữ viết hoa
x = ''  # Chuỗi sau khi xử lí

# hàm xóa dấu cách
for i in s:
    if i != ' ':
        x = x+i

# Hàm để kiểm tra có palindrome hay không (Bài 72)
def isPalindrome(str):

    for i in range(0, int(len(str)/2)):

        if str[i] != str[len(str)-i-1]:
            return False
    return True

# main function
ans = isPalindrome(x)

if (ans) is True:
    print("La chuoi Palindrome.")
else:
    print("Khong phai la chuoi Palindrome.")
