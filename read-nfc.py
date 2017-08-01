import MFRC522
import signal
import os

continue_reading = True
MIFAREReader = MFRC522.MFRC522()

cardA = [46,44,187,26,163]
cardB = [176,203,130,124,133]
cardC = [20,38,121,207,132]

def end_read(signal, frame):
  global continue_reading
  continue_reading = False
  print "Ctrl+C captured, ending read."
  MIFAREReader.GPIO_CLEEN()

signal.signal(signal.SIGINT, end_read)

while continue_reading:
  (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)
  if status == MIFAREReader.MI_OK:
    print "Card detected"
  (status,backData) = MIFAREReader.MFRC522_Anticoll()
  if status == MIFAREReader.MI_OK:
    print "Card read UID: "+str(backData[0])+","+str(backData[1])+","+str(backData[2])+","+str(backData[3])+","+str(backData[4])
    if  backData == cardA:
      print "Evghenii"
      os.system("sshpass -p a ssh root@10.10.0.60 fbi -T 1 -d /dev/fb1 -noverbose /home/pi/Documents/pic/ep.jpg")
      os.system("sshpass -p a ssh root@10.10.0.60 /home/pi/Documents/open.sh 2>/dev/null")
      os.system("sshpass -p a ssh root@10.10.0.60 killall fbi")
    elif backData == cardB:
      print "Vlad"
      os.system("sshpass -p a ssh root@10.10.0.60 fbi -T 1 -d /dev/fb1 -noverbose /home/pi/Documents/pic/vl.jpg")
      os.system("sshpass -p a ssh root@10.10.0.60 /home/pi/Documents/open.sh 2>/dev/null")
      os.system("sshpass -p a ssh root@10.10.0.60 killall fbi")
    elif backData == cardC:
      print "is Card C"
    else:
      print "wrong Card"
      os.system("sshpass -p a ssh root@10.10.0.60 /home/pi/led2.py 2>/dev/null")
