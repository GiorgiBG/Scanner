import password_checker
from port_scanner import PortScann as ps
import os
from file_permission_checker import FilePermission

user_input = ""
while user_input != 0:
    print("""Zero-Day vulnerability scanning tool
1.  Password checker
2.  Port scanner
3.  File permission checker
0.  Exit    """)
    user_input = int(input("Choose the function: "))
    os.system('cls')
    try:
        if user_input == 1:
            user_input = input("Write the password: ")
            pas_checker = password_checker.PasswordCheck(user_input)

            pas_checker.showing_result()
        elif user_input == 2:
            ip = input("IP address: ")
            start_port = int(input("Start port: "))
            end_port = int(input("End port: "))
            scan_port = ps(ip, start_port, end_port)

        elif int(user_input) == 3:
            FilePermission()
        elif user_input == 0:
            print("Good Bye")
        else:
            print("Wrong number")
    except ValueError:
        print("Write integers only")



