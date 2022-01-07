import configparser

config = configparser.ConfigParser()
config.read('config.ini')
key = config["GLEE"]
user = key["USERNAME"]
passwd = key["PASSWORD"]
print(user)
print(passwd)