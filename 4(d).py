#here we are performing some string manipulation
s = "HumptyDumpty"
print('s=',s)
print(s.isalpha())
print(s.isdigit())
print(s.isalnum())
print(s.islower())
print(s.isupper())
print(s.startswith('hum'))
print(s.endswith('pty'))
s1=s2=s3="hello"
print(id(s1),id(s2),id(s3))
msg ='Aeroplane'
ch =msg[-0]
print(ch)
print(msg.partition(''))