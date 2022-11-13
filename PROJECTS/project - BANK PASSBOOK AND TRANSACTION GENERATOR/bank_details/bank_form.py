
class information:
    def __init__(self):
        super().__init__()
        self.name = str(input('NAME :'))
        self.father = str(input('Father :'))
        self.mother = str(input('Mother :'))
        self.gender = str(input('sex :'))
        mobile_number = str(input('your mobile number:'))

        if len(mobile_number)>9 and len(mobile_number)<11:
            self.mobile_no = int(mobile_number)
    def show1(self):
        return f'NAME : {self.name.upper()}\nFather : {self.father.upper()}\nMother : {self.mother.upper()}\nSex : {self.gender.upper()}\nmobile : {self.mobile_no}'

class official:
    def __init__(self):
        super().__init__()

        a=  str(input('16 digit adhar no :'))
        if len(a)>15 and len(a)<17:
            self.adhar = a
        else:
            print('INVALID ADHAR NO ')

        b = str(input('your pan number:'))

        if len(b)>9 and len(b)<11:
            self.pan = b
        else:
            print('INVALID PIN ')
            


    def show(self):
        aa = self.adhar
        bb= self.pan

        return f'ADHAR NO : {aa}\nPAN NO : {bb}'

class addressing:
    def __init__(self):
        super().__init__()
        self.village = str(input('VILLAGE: '))
        self.district = str(input('district: '))
        self.police_station = str(input('police_station: '))
        self.pincode = int(input('pincode:'))
    def show2(self):
        return f'VILLAGE :{self.village.upper()}\nDISTRICT : {self.district.upper()}\nPOLICE STATION: {self.police_station.upper()}\nPINCODE : {self.pincode}'


