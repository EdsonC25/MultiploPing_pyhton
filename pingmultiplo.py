import os
import time

with open('/home/edsonchinendele/Documentos/Python/Projecto/venv/pingmultiplo/host.txt') as file:
    dump=file.read()
    dump = dump.splitlines()

for ip in dump:
    print(ip)
    os.system('ping -n  {} ' .format(ip))
    time.sleep(5)

