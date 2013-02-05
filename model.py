import ntpath

# context
class Context:
	window = None
	settingsPath = ""
	basedir = ""
	scriptModules = None
	textModules = None
	modulesByImportString = {}

	def __init__(self, window, settingsPath):
		self.window = window
		self.settingsPath = settingsPath

	def window(self):
		return self.window

	def settingsPath(self):
		return self.settingsPath

	def getBaseDir(self):
		return ntpath.dirname(self.settingsPath) + "/"

	def setSettings(self, settings):
		self.settings = settings

	def settings(self):
		return self.settings

	def isSublimeRJS(self):
		return self.settingsPath is not ""

	def resetModules(self):
		self.scriptModules = []
		self.textModules = []
		self.scriptPackages = []
		self.textPackages = []

	def addScriptModule(self, module):
		self.scriptModules.append(module)
		self.modulesByImportString[module.getImportString()] = module
		if module.package not in self.scriptPackages:
			self.scriptPackages.append(module.package)

	def getModuleByImportString(self, importString):
		if importString in self.modulesByImportString:
			return self.modulesByImportString[importString]
		else:
			return None

	def getScriptModules(self):
		return self.scriptModules

	def addTextModule(self, module):
		self.textModules.append(module)
		self.modulesByImportString[module.getImportString()] = module
		if module.package not in self.textPackages:
			self.textPackages.append(module.package)

	def getTextModules(self):
		return self.textModules

	def setModuleAliasMap(self, moduleAliasMap):
		self.moduleAliasMap = moduleAliasMap

	def getModuleAliasMap(self):
		return self.moduleAliasMap

	def getTextPackages(self):
		return self.textPackages

	def getScriptPackages(self):
		return self.scriptPackages


# module
class Module:
	name = ""
	path = ""
	type = ""
	package = ""
	importAlias = ""
	refrenceAlias = ""

	def __init__(self, name, path, ext, type, package):
		self.name = name
		self.path = path
		self.ext = ext
		self.type = type
		self.package = package

	def name(self):
		return self.name

	def package(self):
		return self.package

	def getImportString(self):
		if self.importAlias is not "":
			return self.importAlias
		if self.type == "script":
			return self.package + self.name.split(self.ext)[0]
		elif self.type == "text":
			return "text!" + self.package + self.name

	def getRefrenceString(self):
		if self.importAlias is not "":
			if self.refrenceAlias is not "":
				return self.refrenceAlias
			return self.importAlias

		if self.refrenceAlias is not "":
			return self.refrenceAlias
		
		return self.name.split(self.ext)[0]

	def setImportAlias(self, alias):
		self.importAlias = alias

	def setRefrenceAlias(self, alias):
		self.refrenceAlias = alias

