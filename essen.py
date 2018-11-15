import random 

def random_line(file):
  lines = open(file).read().splitlines()
  return random.choice(lines)

def add_line(input):
  with open('meals','a') as file:
   file.writelines(input)
   file.writelines('\n')
  return; 

menu = {}
menu['1']="Essen Auswahl"
menu['2']="Essen Hinzufuegen"
menu['42']="Sortie"

while True:
  options=menu.keys()
  options.sort()
  for entry in options:
   print entry, menu[entry]

  selection=raw_input("Auswahl, bitte.\n")
  if selection == '1':
    print "auswahl: \n"
    print(random_line('meals') + '\n')
  
  elif selection == '2':
    hinz = raw_input('Bitte schreiben: ')
    add_line(hinz)
  
  elif selection == '42':
    print "sortie\n"
    break
