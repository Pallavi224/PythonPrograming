import shutil

#get disk usage statistics
total, used, free = shutil.disk_usage("/")
#calculate percentage of used space

used_percentage = (used / total) * 100
#display the results
print(f"Total disk space: {total / (1024 ** 3):.2f} GB")
print(f"Used disk space: {used / (1024 ** 3):.2f} GB")
print(f"Free disk space: {free / (1024 ** 3):.2f} GB")
print(f"Percentage of used disk space: {used_percentage:.2f}%")
#check if used space is above 70%
if used_percentage > 70:
    print("Warning: Disk space is above 70%!")
#check if used space is above 90%
if used_percentage > 90:
    print("Critical: Disk space is above 90%!")
#check if used space is above 95%
if used_percentage > 95:
    print("Critical: Disk space is above 95%!")
#check if used space is above 98%
if used_percentage > 98:
    print("Critical: Disk space is above 98%!")
#check if used space is above 99%
if used_percentage > 99:
    print("Critical: Disk space is above 99%!")

#check if used space is above 100%
if used_percentage > 100:
    print("Critical: Disk space is above 100%!")
#check if used space is above 110%
if used_percentage > 110:
    print("Critical: Disk space is above 110%!")