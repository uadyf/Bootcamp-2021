# 1. Pengalaman saya dalam bahasa pemrograman python yaitu Pemrosesan data, Pembelajaran mesin, Visualisasi data
# 2. Saya berharap bisa dihadirkan kelas Pembelajaran Mesin yang khusus membahas berbagai aspek pembelajaran mesin dari awal sampe akhir murni untuk pembelajaran mesih saja
# 3. 

class manipulasi:
	def __init__(self, string):
		self.string = string
	def cap_first(self):
		result = f'{self.string[0].upper()}{self.string[1:]}'
		return result
	def low_all(self):
		return self.string.lower()
	def cap_all(self):
		return self.string.upper()
	def sep(self):
		return list(self.string.split())
  
data = 'saya tinggal di indonesia'

cap_pertama = manipulasi(data).cap_first()

kec_semua = manipulasi(data).low_all()

cap_semua = manipulasi(data).cap_all()

separate = manipulasi(data).sep()

print(f'data = {data}\n{cap_pertama}\n{kec_semua}\n{cap_semua}\n{separate}')