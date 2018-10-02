while True:
  print('Who are you?')
  name = input()
  if name != 'Puruwin':      
    continue              
  print('Hello, Puruwin. What is the password?') 
  password = input()      
  if password == 'Python':
    break                 
print('Access granted.')