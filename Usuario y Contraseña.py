while True:
  print('Who are you?')
  name = input()
  if name != 'Puruwin':      
    continue              
  print('Hello, Puruwin. What is the password?') 
  password = input()      #(3)
  if password == 'Python':
    break                 #(4)
print('Access granted.')