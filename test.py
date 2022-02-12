import PasswordFunctions as pf
pf.createTable()
password = pf.generatePassword(14)
url = pf.generatePassword(10)
url += ".com"
name = pf.generatePassword(5)
pf.writeToDb(url,name,password)
pf.readDb()

