import time
seconds = int(input("Enter Seconds to count down"))
for i in range(seconds):
    print(str(seconds-i)+" second left")
    time.sleep(1)

print("--end--")

