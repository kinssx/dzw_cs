"""Բ��-Circle
�������-get_area(self)
�ܳ�����-get_perimeter(self) 
"""
class Circle:
    def __int__(self,r):
        self.r=r
    def get_area(self):
        return 3.14 * pow(self.r,2)
    def get_perimeter(self):
        return 2 * 3.14 * self.r

r= eval(input("������Բ�İ뾶��"))
c=Circle(r)
print("Բ�������",c.get_area())
print("Բ���ܳ���",c.get_perimeter())
