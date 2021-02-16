from snake import Snake,snake_oled,snake_oled_2
from machine import I2C,Pin,ADC
from ssd1306 import SSD1306_I2C#I2C的oled选该方法
import utime as time
import urandom
import ujson



i2c=I2C(0,sda=Pin(0), scl=Pin(1), freq=2000000) 
oled = SSD1306_I2C(128, 64, i2c) #你的OLED分辨率，使用I2C
c=ADC(2)
l=1
# c.read_u16()
def level(l=1):
    if l==1:
        time.sleep(0.7)
    elif l==2:
        time.sleep(0.5)
    elif l==3:
        time.sleep(0.4)
    elif l==4:
        time.sleep(0.3)
    else:
        time.sleep(0.2)
def jugg_level(score=0):
    if  score in range(5):
        l=1
    elif  score in range(5,10):
        l=2
    elif score in range(10,15):
        l=3
    elif score in range(15,20):
        l=4
    else:
        l=5
    return l

s=range(9000,11000)
x=range(19000,21000)
z=range(0,2000)
y=range(30000,32000)
q=range(45000,47000)

def game():
    try:
        fs=open("game.conf",'r')
        snake_score=ujson.loads(fs.read())
        fs.close()
    except Exception as e:
        fs=open("game.conf",'w')
        snake_score=[1,]
        fs.close()
    vs=Snake(32,32,len(snake_score))
    f=urandom.randint(0,3)
    while True:
        cc=c.read_u16()
        qx=f
        if cc in s:
            f=0
            if qx==1:
                f=1
            print("s")
        elif cc in x:
            f=1
            if qx==0:
                f=0
            print("x")
        elif cc in z:
            f=2
            if qx==3:
                f=3
            print("z")
        elif cc in y:
            f=3
            if qx==2:
                f=2
            print("y")
        elif cc in q:
            #NOne
            pass
            print("q")
        else:
            pass 
            print("0")
        
        m=vs.do(f)
        score=len(vs.snake)
        l=jugg_level(score)
        if m:
            snake_oled_2(oled,vs.apple,vs.snake)
            # snake_oled(oled,vs.apple,vs.snake)
        else:
            oled.fill(0)
            oled.text("GAME",8,20,1)
            oled.text("OVER",8,32,1)
            fs=open("game.conf",'w')
            snake_score.append(score)
            fs.write(ujson.dumps(snake_score))
            fs.close()
        oled.line(64,0,64,63,1)
        oled.text("SNAKE",80,4,1)
        oled.line(68,13,127,13,1)
        oled.text("Score",68,16,1)
        oled.text(str(score),128-8*len(str(score)),24,1)
        oled.text("Level",64,32,1)
        oled.text(str(l),120,40,1)
        oled.text("MAX",68,48,1)
        oled.text(str(max(snake_score)),128-8*len(str(max(snake_score))),56,1)
        oled.show()
        level(l)
        print(snake_score)
        if not m:
            time.sleep(3)
            game()

game()
