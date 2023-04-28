import subprocess
a = subprocess.check_output(['ipconfig'])
a = str(a)
a = a.replace(".", "")
a = a.replace("\\r", "")
#a = a.replace("\\n", "")
a = a.replace(" ", '')
b = a.split(":")
c = len(b)
for i in range(len(b)):
    if "\\n" in b[i]:
        d = b[i]
        d = d.split("\\n")
        b.insert(i, d[0])
        b.insert(i + 1, d[1])
        b.remove(i) 
