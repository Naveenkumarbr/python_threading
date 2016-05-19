#searching the word in the text file
import re
import threading
import time

def searchparallel(findstr,i):
	fo=open("sample_"+i+".txt","r+")
	strfile = fo.read()
	time.sleep(2)
	match=re.search(findstr,strfile,re.I)
	if match:
		print("\n"+threading.current_thread().name+"------>"+match.group())
	else:
		print("\n"+threading.current_thread().name+"------>not found")
	fo.close()

time_start=time.time()
for i in range(0,4):
	t1=threading.Thread(target=searchparallel, args=('Naveen',str(i)))
	t1.start()

print("\nThis should be printed first\n")
print("The main thread completed the task in : ", (time_start-time.time()))