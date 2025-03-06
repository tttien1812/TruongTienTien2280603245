
from SinhVien import SinhVien

class QuanLySinhVien:
    listSinhVien = []

    def generateID(self) :
        maxId = 1 
        if (self. soluongSinhVien() > 0):
            maxId = self.listSinhVien[0]._id 
            for sv in self.listSinhvien:
                if (maxId < sv._id):
                    maxid - sv._id
                maxId = maxid + 1
            return maxId
        
    def soLuongSinhVien(self): 
        return self.listSinhVien._len_()
    def nhapSinhVien(self):
        svId = self-generateID()
        name = input ("Nhap ten sinh vien: ")
        sex = input( "Nhap giơi tinh sinh vien: ")
        major = input("Nhap chuyen nganh cua sinh vien:")
        diemTB = float("Nhap diem cua sinh vien: 3")
        sv = SinhVien(svId, name, sex, major, diemTB)
        self.xepLoaiHocLuc(sv)
        self. listSinhVien.append(sv)

    def updateSinhVien(self, ID):
        sv: SinhVien = self. FindByID(ID)
        if (sv != None):
            name = input ("Nhap ten sinh vien: ")
            sex - input("Nhap gioi tinh sinh vien: ")
            major - int (input("Nhap chuyen nganh của sinh vien: "))
            diemTB = float(input("Nhap diem cua sinh vien: "))
            sv._name = name
            sv._sex = sex
            sv._major = major
            sv. _diemTB - diemTB 
            self.xepLoaiHocLuc(sv)