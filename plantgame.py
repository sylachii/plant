import random 
from tkinter import *
from PIL import ImageTk, Image

def openImage(file):
  load = Image.open(file)
  render = ImageTk.PhotoImage(load)
  img = Label(image=render)
  img.image = render
  img.place(x=0, y=0)


def plant():

  root = Tk()
  root.title('Plant Game :)')

  print("")
  print("Take care of your digital plant for a week!")
  print("Water it if the dirt is dry, fertilize it if it's yellowing")
  print("")
  print("Good luck!")

  days = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]
  dry = [False, True]
  wilt = [False, True]
  score = 14
  dCont = False
  wCont = False
  oWaterState = False
  oFertState = False

  #Day cycles
  for day in days:
    print (day)

    #Assigns states
    #If the plant was in good condition, states are randomized, otherwise conditions persist
    dState = random.choice(dry)
    wState = random.choice(wilt)
    oWater = ""
    oFert = ""

    if dCont == True:
      dState = True
    if wCont == True:
      wState = True

    #assigns over-watered or over-fertilized state if plant was watered/fertilized when not needed
    if oWaterState == True:
      oWater = True
      dState = False
    else:
      oWater = False

    if oFertState == True:
      oFert = True
      wState = False
    else:
      oFert = False

    if dState == True:
      print ("The soil is dry")
    elif oWater == True:
      print("The soil is soaked")
    else:
      print("The soil is damp")

    if wState == True:
      print ("The leaves are yellowing")
    elif oFert == True:
      print("The leaves have too many nutrients") 
    else:
      print ("The leaves are green")

    if oWater == True and oFert == True:
      openImage("ofertow.png")

    elif oWater == True and wState == True:
      openImage("wiltow.png")

    elif oWater == True and wState == False:
      openImage("nowiltow.png")

    elif dState == True and oFert == True:
      openImage("ofdry.png")

    elif dState == False and oFert == True:
      openImage("ofwater.png")

    elif dState == True and wState == True:
      openImage("wiltdry.png")

    elif dState == True and wState == False:
      openImage("nowiltdry.png")

    elif dState == False and wState == False:
      openImage("nowiltwater.png")

    elif dState == False and wState == True:
      openImage("wiltwater.png")




    w = input("Water? ")
    w = w.lower()

    if w[0] == "y" and dState == False:
      oWaterState = True
      score = score - 1

    if w[0] == "y" and dState == True:
      dState = False

    if w[0] != "y" and oWaterState == True:
      oWaterState = False

    f = input ("Fertilizer? ")
    f = f.lower()

    if f[0] == "y" and wState == False:
      oFertState = True
      score = score - 1

    if f[0] == "y" and wState == True:
      wState = False

    if f[0] != "y" and oFertState == True:
      oFertState = False

    if dState == True:
      score = score - 1
      dCont = True

    else:
      dCont = False

    if wState == True:
      score = score - 1
      wCont = True

    else:
      wCont = False

    print ("")

  if score >12:
    print("Congrats! You should consider buying a real plant")
    openImage("alive.png")

  if score >= 8 and score <= 12:
    print("Not bad!")
    openImage("nowiltwater.png")

  if score < 8:
    print("Please never buy any living thing... yikes")
    openImage("dead.png")

while True:
  plant()

  print("")
  cont = input("Would you like to play again? ")
  cont = cont[0]
  cont = cont.lower()
  if cont == "y":
    continue
  else:
    print("Bye!")
    break
