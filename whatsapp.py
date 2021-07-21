import pywhatkit
ph_number = input()
z=22
while True:
    z=z+1
    pywhatkit.sendwhatmsg(ph_number, 'I Love You', 20, z)
