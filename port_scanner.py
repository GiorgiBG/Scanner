import socket

class PortScann():
    def __init__(self, ip, start_port, end_port):
        self.ip = ip
        self.start_port = start_port
        self.end_port = end_port
        self.main()
        self.open_port_list = []
        save = input("Do you want to save report? Y/N ")
        if save.lower() == "Y":
            self.write_report()
        else:
            pass

    def tcp_scan(self):
        for port in range(self.start_port, self.end_port + 1):
            try:
                tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                if not tcp.connect_ex((self.ip, port)):
                    report = f'>>> {self.ip}:{port}/TCP Open'
                    print(report)
                    self.write_report(report+"\n")
                    tcp.close()
            except Exception:
                pass

    def main(self):
        socket.setdefaulttimeout(0.01)
        self.tcp_scan()

    def write_report(self, report):
        with open("Open port report.txt", 'a') as file:
            file.write(report)


