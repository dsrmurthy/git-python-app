import schedule,time

def upload():
    print("Upload started.............") # do actual work

schedule.every(1).minute.do(upload)
schedule.every().monday.do(upload)


while True:
    schedule.run_pending()
    time.sleep(10)
    print('*')

''' Write a code to send mail with smtp-server'''