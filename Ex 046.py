from time import sleep
for fogos in range(10, -1, -1):
    print(fogos)
    sleep(1)
print('\033[1;7;40mFeliz ano novo!\033[m')
