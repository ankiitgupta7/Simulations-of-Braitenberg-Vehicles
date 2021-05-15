add_library('controlP5')

# https://tabreturn.github.io/code/processing/python/2019/03/19/processing.py_in_ten_lessons-7.5-_controlp5.html

def setup():
  size(720,485)
  global cp5
  cp5 = ControlP5(this)   
  slider = cp5.addSlider("2b")
  slider.setPosition(20,20).setSize(200,20)

  
  l = "zero", "one", "two", "three", "four", "five", "six", "seven"
  option = "Fixed","Moving"
  cp5.addScrollableList("Opt for Stimuli Motion").setPosition(20, 20).setSize(200, 100).setBarHeight(20).setItemHeight(20).addItems(option)

  cp5.addScrollableList("Number of 2a type stimulus").setPosition(20, 100).setSize(200, 100).setBarHeight(20).setItemHeight(20).addItems(l)
  cp5.addScrollableList("Number of 2b type stimulus").setPosition(240, 100).setSize(200, 100).setBarHeight(20).setItemHeight(20).addItems(l)
  cp5.addScrollableList("Number of 3a type stimulus").setPosition(460, 100).setSize(200, 100).setBarHeight(20).setItemHeight(20).addItems(l)
  cp5.get(ScrollableList, "Number of 2a type stimulus").setType(ControlP5.LIST)
  cp5.get(ScrollableList, "Number of 2b type stimulus").setType(ControlP5.LIST)
  cp5.get(ScrollableList, "Number of 3a type stimulus").setType(ControlP5.LIST)

  
  cp5.get(ScrollableList, "Opt for Stimuli Motion").setType(ControlP5.LIST)

 # cp5.addButton("startSim").setValue(0).setPosition(20, 200).setSize(200, 100)

def draw():
  background('#004477')
  print(cp5.getController("mySlider").getValue()) 
  opt = int(cp5.getController("Opt for Stimuli Motion").getValue())
  n2a = int(cp5.getController("Number of 2a type stimulus").getValue())
  n2b = int(cp5.getController("Number of 2b type stimulus").getValue())
  n3a = int(cp5.getController("Number of 3a type stimulus").getValue())
 

  #print opt, n2a, n2b, n3a
  if mousePressed and (mouseButton == RIGHT):
    fill(0)
  elif mousePressed and (mouseButton == LEFT ) and mouseX>20 and mouseX<100 and mouseY>250 and mouseY<270:
    print("oh yeah!!!")
  else:
    fill(126)
  rect(20, 250, 80, 20)

