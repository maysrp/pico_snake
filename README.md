# pico_snake
PICO 使用SSD1306 OLED AD KeyBoard 制作贪吃蛇


使用之前的OLED SSD1306 IIC 和 ADkeyBoard 即可制作贪吃蛇游戏

## 贪吃蛇规则
+ 蛇碰到墙壁或者自己的身体则结束游戏
+ 蛇吃到苹果身体增长一节积分加一
+ 积分到一定分数后等级增加，运动速度变大
+ 保持最高得分


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
