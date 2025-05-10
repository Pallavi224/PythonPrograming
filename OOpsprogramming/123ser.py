class Server:
    def __init__(self, server_id, name, ip):
        self.server_id = server_id
        self.name = name
        self.ip = ip
        self.status = "offline"
        self.memory_usage = 0

    def ping(self):
        return f"Pinging {self.ip}..."

    def start(self):
        self.status = "online"
        return f"Server {self.name} is now {self.status}."

    def stop(self):
        self.status = "offline"
        return f"Server {self.name} is now {self.status}."

    def get_status(self):
        return f"Server {self.name} (ID: {self.server_id}) is currently {self.status}."
    def update_status(self):
        return f"Server {self.name} (ID: {self.server_id}) is currently {self.status}."
# Example usage
web_server1 = Server("s123", "WebServer1", "123.89.00")
print(web_server1.ping())
print(web_server1.start())
print(web_server1.update_status())
print(web_server1.stop())