from collections import namedtuple
from pprint import pprint
from selenium import webdriver



class Fundamentus:
	def __init__(self, driver):
		#papel = 'ALPA3'
		self.driver = driver
		self.url = 'https://www.fundamentus.com.br/detalhes.php?papel=ALPA3'
		self.nome_papel = 'data w35' #class
		self.nome_papel_text = 'txt' #class
	def navigate(self):
		self.driver.get(self.url)

	def _get_papel_name(self):
		return self.driver.find_elements_by_class_name(self.nome_papel)

	def _get_papel_name_text(self,papel_name):
		return papel_name.find_element_by_class_name(self.nome_papel_text)

	def get_papel_info(self):
		print(self._get_papel_name())
		#papeis = self._get_papel_name()
		#for papel in papeis:
		#	print(self._get_papel_name_text().text)
''' FUNCIONOU
	def _get_papel_name(self):
		return self.driver.find_elements_by_class_name(self.nome_papel_text)
	
	def teste(self):
		return self.driver.find_element_by_xpath("//table/tbody/tr[1]/td[1]").getText();

	def get_papel_info(self):
		papeis = self._get_papel_name()
		for papel in papeis:
			print(papel.text)
'''

ff = webdriver.Firefox(executable_path=r'C:\Program Files (x86)\Mozilla Firefox\geckodriver.exe')
c = Fundamentus(ff)
c.navigate()
c.get_papel_info()
