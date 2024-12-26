import os
import time
from prettytable import PrettyTable, TableStyle
import psutil
size = ['bytes', 'KB', 'MB', 'GB', 'TB']
def getSize(bytes):
    for unit in size:
        if bytes < 1024:
            return f"{bytes:.1f}{unit}"
        bytes /= 1024
def printData():
    card = PrettyTable()
    card.set_style(TableStyle.PLAIN_COLUMNS)  
    card.field_names = ["Received", "Receiving", "Sent", "Sending"]
    card.add_row([
        f"{getSize(netStats2.bytes_recv)}", 
        f"{getSize(downloadStat)}/s", 
        f"{getSize(netStats2.bytes_sent)}", 
        f"{getSize(uploadStat)}/s"
    ])
    print(card)
netStats1 = psutil.net_io_counters()
dataSent = netStats1.bytes_sent
dataRecv = netStats1.bytes_recv
try:
    while True:
        time.sleep(1)
        os.system('cls')  # Use 'clear' for Linux/MacOS
        netStats2 = psutil.net_io_counters()
        uploadStat = netStats2.bytes_sent - dataSent
        downloadStat = netStats2.bytes_recv - dataRecv
        printData()
        dataSent = netStats2.bytes_sent
        dataRecv = netStats2.bytes_recv
except KeyboardInterrupt:
    print("\nProgram terminated by user.")
