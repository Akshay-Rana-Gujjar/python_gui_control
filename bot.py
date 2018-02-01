import pyautogui, subprocess, time


# get screen height and width
screenWidth, screenHeight = pyautogui.size()

# move cursor to coresponding x and y coordinates, 
# duration is how much it take time to moving cursor and 
# tween is how the pattern to move the cursor
pyautogui.moveTo(510, 1500, duration=2, tween=pyautogui.easeInOutQuad)

# cursor scroll(up direction)
pyautogui.scroll(1)



# wait for 1 sec
time.sleep(1)

image_path = "./images/connect1.png"
send_now = "./images/send_now.png"
next_image = "./images/next.png"
count = 0


def find_connect_btn():
  try:
    global count
    if "btns" not in locals() :
      btns = list(pyautogui.locateAllOnScreen(image_path)) # get the Buttons by image
      print("\n\n\nBTN NOT EXIST\n\n\n")

    for index, btn in enumerate(btns):
    # for btn in btns:
      if btn:
        print(index," btn =",btn)
      
      # # get the center of image
      btn_center = pyautogui.center(btn)
      print("btn_center", btn_center)
      center_coordinates = list(btn_center)

      print("center_coordinates",center_coordinates)

      pyautogui.moveTo(center_coordinates[0], center_coordinates[1], duration=2, tween=pyautogui.easeOutQuad)
      pyautogui.click()
      time.sleep(0.5)

      send_now_btn = list(pyautogui.locateOnScreen(send_now))
      send_now_btn_coordinates = list(pyautogui.center(send_now_btn))
      pyautogui.click(send_now_btn_coordinates, duration=2 )
      time.sleep(0.5)

      if index == len(btns)-1 and count < 2:
        count += 1
        print("i am in")
        # move cursor and then scroll(down direction)
        # pyautogui.scroll(-10)
        # pyautogui.moveTo(screenWidth / 2, screenHeight / 2, 2 , pyautogui.easeInOutQuad)
        pyautogui.scroll(-16)
        btns = list(pyautogui.locateAllOnScreen(image_path)) # get the Buttons by image
        find_connect_btn()
        print(len(btns)," btns =",btns)

    click_next()
    count = 0
    find_connect_btn()
  except Exception as identifier:
    print(identifier)
    subprocess.call(["notify-send" , "Failed", str(identifier)])
    click_next()
    
    find_connect_btn()

def click_next():
  pyautogui.scroll(-20)
  time.sleep(2)
  next_btn = list(pyautogui.locateOnScreen(next_image))
  next_btn_coordinates = list(pyautogui.center(next_btn))
  pyautogui.click(next_btn_coordinates, duration=2 )
  time.sleep(3)

find_connect_btn()

# pyautogui.moveTo(100, 100, 2, pyautogui.easeInQuad)     # start slow, end fast
# pyautogui.moveTo(100, 100, 2, pyautogui.easeOutQuad)    # start fast, end slow
# pyautogui.moveTo(100, 100, 2, pyautogui.easeInOutQuad)  # start and end fast, slow in middle
# pyautogui.moveTo(100, 100, 2, pyautogui.easeInBounce)   # bounce at the end
# pyautogui.moveTo(100, 100, 2, pyautogui.easeInElastic)  # rubber band at the end