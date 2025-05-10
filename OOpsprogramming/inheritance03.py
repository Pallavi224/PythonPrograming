class Server:
    def __init__(self, name):
        self.name = name


    def start(self):
        print(f"{self.name} server started.")

class Webserver(Server):
    def deploy(self):
        print(f"{self.name} Apache server deployed.")

class ApplicationServer(Server):
    def deploy(self):
        print(f"{self.name} application server deployed.")
ws1= Webserver("WebServer1")
ws1.start()
ws1.deploy()
#ws1.stop()
#creating object of class Server
#creating object of class Server
print(ws1.start())
print(ws1.deploy())
print(ws1.start())
print(ws1.deploy())
#print(ws1.stop())
#creating object of class Server

ws2=ApplicationServer("AppServer1")
ws2.start()
ws2.deploy()
#creating object of class Server
print(ws2.start())
print(ws2.deploy())
