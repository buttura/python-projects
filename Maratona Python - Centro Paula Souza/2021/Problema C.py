while True:
  while True:
    s = 0
    v = str(input())
    for i in range(0, len(v.split())):
      if 0 <= int(v.split()[i]) <= 1000:
        s += 1
    if s == len(v.split()):
      break
  if len(v.split()) == 1 and int(v) == 0:
    break
  else:
    if int(v.split()[0]) == int(v.split()[1]) + int(v.split()[2]) + int(v.split()[3]) and int(v.split()[3]) == int(v.split()[2]) + int(v.split()[1]) and int(v.split()[1]) == int(v.split()[2]):
      print("S")
    else:
      print("N")
