import virustotal_python
import os.path
import subprocess
# API key for VirusTotal
API_KEY = "6f3cab1070600e63c15bea06c55aa04ec96ecae6cef1ebe6127bc9514131ba8a"
# URL for uploading files
file_path = "C:/Users/Gio/Desktop/Master_Thesis_project/Open port report.txt"

# files = {"file": (os.path.basename(file_path), open(os.path.abspath(file_path), "rb"))}
#
# with virustotal_python.Virustotal(API_KEY) as vtotal:
#     resp = vtotal.request("files", files=files, method="POST")
#     print(resp.text)



def sha256sum(filename):
    """Compute the SHA-256 hash of a file"""
    cmd = ['sha256sum', filename]
    output = subprocess.check_output(cmd)
    return output.decode('utf-8').split()[0]

# Example usage:
hash_value = sha256sum(file_path)
print('SHA-256 hash:', hash_value)

