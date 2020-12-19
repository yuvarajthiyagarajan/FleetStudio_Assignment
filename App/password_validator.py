import re

class CheckPassword():

	def __init__(self, password):
		self.password = password

	def __atleastonechar(self):
		pattern = re.compile(r'[a-zA-Z]')
		matches = None
		matches = pattern.finditer(self.password)
		for match in matches:
			return True
		return False

	def __atleastonenumber(self):
		pattern = re.compile(r'[0-9]')
		matches = None
		matches = pattern.finditer(self.password)
		for match in matches:
			return True
		return False

	def __atleastonspchar(self):
		pattern = re.compile(r'[#_-]')
		matches = None
		matches = pattern.finditer(self.password)
		for match in matches:
			return True
		return False

	def validator(self):
		charerror = self.__atleastonechar()
		numerror = self.__atleastonenumber()
		spcharerror = self.__atleastonspchar()
		print(charerror, numerror, spcharerror)
		report = charerror and numerror and spcharerror

		if report:
			message = "Your password is chosen correctly"
			return (True, message)
		elif not charerror:
			message = "You should use atleast one alphabetical character in your password"
			return (False, message)
		elif not numerror:
			message = "You should use atleast one numerical character in your password"
			return (False, message)
		elif not spcharerror:
			message = "You should use atleast one special character out of this (#,-,_) in your password"
			return (False, message)
		else:
			return None


# val = CheckPassword("Test1-")			
# print(val.validator()[0])