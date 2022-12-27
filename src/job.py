import src.filehandler as filehandler
import src.phrase as phrase

class Job:
	uid:str
	filepaths:list

	consolidated_path:str
	isZipped:bool
	done:bool = False

	def generate_consolidated_file(self) -> None:
		# Get a consolidated path
		self.consolidated_path, self.isZipped = filehandler.get_consolidated_path(self.filepaths, phrase.get_short_phrase(self.uid))

	def __init__(self, uid:str, filepaths:list) -> None:
		self.uid = uid
		self.filepaths = filepaths

