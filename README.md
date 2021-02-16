# pico_snake
PICO 使用SSD1306 OLED AD KeyBoard 制作贪吃蛇


使用之前的OLED SSD1306 IIC 和 ADkeyBoard 即可制作贪吃蛇游戏


## 接线
将ADKeyBoard 和 OLED 与树莓派pico连接起来

|OLED|PICO|
|-|-|
|3v3|3v3|
|GND|GND|
|SDA|GPIO0|
|SCL|GPIO1|


|ADKeyboard|PICO|
|-|-|
|VCC|3v3|
|GND|GND|
|OUT|GPIO28(ADC2)|

## 上传
依次上传代码snake.py 和 main.py到你的PICO上，上电即可玩
