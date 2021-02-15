import urandom
class Snake(object):
    def __init__(self,x=32,y=32,s=22):
        urandom.seed(s) #seed
        self.snake=[]
        self.apple=[]
        self.randapple()
        self.init_snake()
        self.x=x
        self.y=y
    def randapple(self):
        m=self.rand()
        if m in self.snake:
            self.randapple()
        self.apple=m
    def init_snake(self):
        s=self.rand()
        self.snake.append(s)
        if s in self.apple:
            self.snake=[]
            self.init_snake()
    def rand(self):
        x=urandom.randint(0,31)
        y=urandom.randint(0,31)
        return [x,y]
    def do(self,types=1):
        # m x n y
        # 上 y-1 0
        # 下 y+1 1
        # 左 x-1 2
        # 右 x+1 3
        ne=[]
        if types==0:
            m=0
            n=-1
        elif types==1:
            m=0
            n=1
        elif types==2:
            m=-1
            n=0
        elif types==3:
            m=1
            n=0
        i=self.snake[0]
        ne=[i[0]+m,i[1]+n]
        if self.juggl():
            if self.jugga(self.snake):
                q=[ne,]+self.snake
                self.snake=q
            else:
                q=[ne,]+self.snake
                self.snake=q
                self.snake.pop()
                
            return True
        else:
            return False
    def juggl(self):
        head=self.snake[0]
        if head in self.snake[1:]:
            return False
        if head[0]<0 or head[0]>=self.x or head[1]<0 or head[1]>self.y:
            return False
        return True
    def jugga(self,snakes):
        if self.apple in snakes:
            self.randapple()
            return True
        else:
            return False

def snake_oled(oled,apple,snake):
    oled.fill(0)
    oled.pixel(apple[0],apple[1],1)
    for i in snake:
        oled.pixel(i[0],i[1],1)
    # oled.show()

def snake_oled_2(oled,apple,snake):
    oled.fill(0)
    oled.pixel(2*apple[0],2*apple[1],1)
    oled.pixel(2*apple[0]+1,2*apple[1],1)
    oled.pixel(2*apple[0]+1,2*apple[1]+1,1)
    oled.pixel(2*apple[0],2*apple[1]+1,1)
    for i in snake:
        oled.pixel(2*i[0],2*i[1],1)
        oled.pixel(2*i[0]+1,2*i[1],1)
        oled.pixel(2*i[0]+1,2*i[1]+1,1)
        oled.pixel(2*i[0],2*i[1]+1,1)
    # oled.show()

#snake 前一个为后一个坐标