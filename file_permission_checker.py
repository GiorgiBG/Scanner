import os


class FilePermission():
    def __init__(self):
        self.file_path = input("Indicate file path: ")
        self.check_permission()

    def check_permission(self):
        if not os.path.exists(self.file_path):
            print(f"File '{self.file_path}' does not exist.")
        else:
            mode = os.stat(self.file_path).st_mode
            if mode & 0o400:
                print(f"File '{self.file_path}' is readable by the current user")
            if mode & 0o200:
                print(f"File '{self.file_path}' is writable by the current user.")
            if mode & 0o100:
                print(f"File '{self.file_path}' is executable by the current user.")
