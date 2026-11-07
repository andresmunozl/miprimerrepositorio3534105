import time
while True:
    for hora in range (24):
       for minutos in range (60):
          for segundos in range (60):
            time.sleep(1)
            print (f"{hora}:{minutos}:{segundos}")