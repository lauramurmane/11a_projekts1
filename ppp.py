laiks = input("Cik ir pulkstens :")

if '04:00' <= laiks <= '11:59':
    print("Labrīt")
if '12:00' <= laiks <= '17:59':
    print("Labdien")
if '18:00'<= laiks <= '23:59':
    print("Labvakar")
if '00:00'<= laiks <= '03:59':
    print("Arlabunakti")
else:
    print("Neatbistošs rezultāts")
