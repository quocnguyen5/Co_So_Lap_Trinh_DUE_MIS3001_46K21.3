HangHoa = []


while True:
    DacDiemHang = []
    for j in range(4):
        if j == 0:
            MaHang = str(input('Ma Hang:'))
            [DacDiemHang.append(MaHang)]
            if MaHang == '':
                break
        elif j == 1:
            DacDiemHang.append(float(input('So luong:')))
        elif j == 2:
            DacDiemHang.append(float(input('Don gia:')))

    HangHoa.append(DacDiemHang)
