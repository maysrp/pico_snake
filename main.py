from snake import Snake,snake_oled,snake_oled_2
from machine import I2C,Pin,ADC
from ssd1306 import SSD1306_I2C#I2C的oled选该方法
import utime as time
import urandom

i2c=I2C(0,sda=Pin(0), scl=Pin(1), freq=2000000) 
oled = SSD1306_I2C(128, 64, i2c) #你的OLED分辨率，使用I2C
c=ADC(2)
l=1
# c.read_u16()
def level(l=1):
    if l==1:
        time.sleep(0.8)
    elif l==2:
        time.sleep(0.6)
    elif l==3:
        time.sleep(0.4)
    elif l==4:
        time.sleep(0.3)
    else:
        time.sleep(0.2)
def jugg_level(score=0):
    if  score in range(10):
        l=1
    elif  score in range(10,20):
        l=2
    elif score in range(20,30):
        l=3
    elif score in range(30,40):
        l=4
    else:
        l=5
    return l

s=range(9000,11000)
x=range(19000,21000)
z=range(0,2000)
y=range(30000,32000)
q=range(45000,47000)

vs=Snake()
f=urandom.randint(0,3)
while True:
    cc=c.read_u16()
    if cc in s:
        f=0
        # m=vs.do(0)
        print("s")
    elif cc in x:
        f=1
        # m=vs.do(1)
        print("x")
    elif cc in z:
        f=2
        # m=vs.do(2)
        print("z")
    elif cc in y:
        f=3
        # m=vs.do(3)
        print("y")
    elif cc in q:
        # vs.do()
        #NOne
        pass
        print("q")
    else:
        pass 
        print("0")
    m=vs.do(f)
    score=len(vs.snake)
    if m:
        snake_oled_2(oled,vs.apple,vs.snake)
        # snake_oled(oled,vs.apple,vs.snake)
    else:
        l=jugg_level(score)

        oled.fill(0)
        oled.text("GAME",8,20,1)
        oled.text("OVER",8,32,1)
    oled.line(64,0,64,63,1)
    oled.text("SNAKE",72,4,1)
    oled.line(68,13,127,13,1)
    oled.text("Score",68,16,1)
    oled.text(str(score),78,25,1)
    oled.text("Level:"+str(l),68,38,1)
    oled.show()
    level(l)
    # print(vs.snake)
    # print(vs.apple)