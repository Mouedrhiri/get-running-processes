import wmi
from tqdm import tqdm
from time import sleep
def progress(range):
    for i in tqdm(range, desc ="Progress : "):
            sleep(.1)

f = wmi.WMI()
l = []
print("We Will Load Your Running Processes Please Wait ")
for process in f.Win32_Process():
    l.append(process.ProcessId)

progress(l)
print("ID Of Process:   Process name:")
for process in f.Win32_Process():
    print(f"{process.ProcessId:<10} {process.Name}")

print(f"\n le Nombre des fichier Ouvert est {len(l)}")
input()