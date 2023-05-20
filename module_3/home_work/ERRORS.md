# Ошибки и исправления класса Person
* Были заданы неверные отступы внутри класса и функций
* В методе get_age() перепутаны в return self.yob и now.year,  
возраст получался отрицательный
* В методе set_name() self.name = self.name исправлено на self.name = name
* В методе set_address() исправлено == на =
* В методе is_homeless() изменены одинарные кавычки на двойные,  
добавлен self.address вместо address