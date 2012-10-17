"""
HW4, #6
L15, #3
Extend our basic GUI for billiards into

"""

# L-15 MCS 507 Mon 1 Oct 2012 : basic GUI for billiard ball

from Tkinter import *
import random,math

class BilliardBall():
   """
   GUI to simulate billiard ball movement.
   """
   #def __init__(self,wdw,dimension,increment,delay):
   def __init__(self,wdw,dimension,increment):
      "determines the layout of the GUI"
      wdw.title('a pool table')
      self.dim = dimension # dimension of the canvas
      self.inc = increment
      #self.dly = delay
      
      #self.dly = 100
      self.go = False # state of animation
      # initial coordinates of the ball
      self.x = random.randint(10,self.dim-10)
      self.y = random.randint(10,self.dim-10)
      self.c = Canvas(wdw,width=self.dim,\
        height=self.dim,bg ='green')
      self.c.grid(row=1,column=1,columnspan=3)
      self.b0 = Button(wdw,text='start',\
        command = self.start)
      self.b0.grid(row=3,column=1,sticky=W+E)
      self.b1 = Button(wdw,text='stop',\
        command = self.stop)
      self.b1.grid(row=3,column=2,sticky=W+E)

      # Create array to store the path
      self.path=[]
      self.count=0


      # Add slider for delay
      self.delayLbl = Label(wdw,text='delay',justify=LEFT)
      self.delayLbl.grid(row=0,column=0)
      self.dly1=IntVar()
      self.d=Scale(wdw,orient='vertical',from_=0,to=200,\
         tickinterval=20,resolution=20,length=self.dim,\
         variable=self.dly1,command=self.animate())

      self.d.grid(row=1,column=0)

      # Get boxes to display x and y coords
      self.ex = Entry(wdw,justify=LEFT) # for x value
      self.ex.grid(row=0,column=1)
      self.ex.insert(INSERT,"x = ")
      self.ey = Entry(wdw,justify=LEFT) # for y value
      self.ey.grid(row=0,column=2)
      self.ey.insert(INSERT,"y = ")

      # check button for drawing of path
      self.path_flg = IntVar()
      self.cb = Checkbutton(wdw,text='draw path',\
        variable=self.path_flg,onvalue=1,offvalue=0)
      self.path_flg.set(1)
      print self.path_flg.get()
      self.cb.grid(row=0,column=3)

      # Clear button
      self.b2 = Button(wdw,text='clear',\
        command = self.Clear)
      self.b2.grid(row=3,column=3,sticky=W+E)

   def UpdateValues(self):
      self.dly=self.dly1.get()
      
      

   def MapToTable(self,p):
      "keeps the ball on the pool table"
      if p < 0:
         (q,r) = divmod(-p,self.dim)
      else:
         (q,r) = divmod(p,self.dim)
      if q % 2 == 1:
         r = self.dim - r
      return r

   def DrawBall(self):
      "draws the ball on the pool table"
      x = self.MapToTable(self.x)
      y = self.MapToTable(self.y)
      self.c.delete('dot')
      self.c.create_oval(x-6,y-6,x+6,y+6,width=1,\
        outline='black',fill='red',tags='dot')
      self.path.append((x,y))

   def animate(self):
      "performs the animation"
      self.UpdateValues()
      self.DrawBall()
      angle = random.uniform(0,2*math.pi)
      vx = math.cos(angle)
      vy = math.sin(angle)
      self.lines=[]
      while self.go:
         x = self.x; y = self.y
         self.x = x + vx*self.inc
         self.y = y + vy*self.inc
         self.c.after(self.dly)
         self.DrawBall()
         self.count=self.count+1         
         self.draw_path()
         self.FillEntries()
         self.c.update()

   def start(self):
      "starts the animation"
      self.go = True
      self.animate()

   def stop(self):
      "stops the animation"
      self.go = False

   def draw_path(self):
      """
      Draws the path of the ball
      """
      i=self.count-1
      j=self.count
      x0 = self.path[i][0]
      y0 = self.path[i][1]
      x1 = self.path[j][0]
      y1 = self.path[j][1]
      
      if self.path_flg.get()==1:
         t=self.c.create_line(x0,y0,x1,y1,fill='black', width=3.0, tag='tkpath')
         self.lines.append(t)

   def FillEntries(self):
      """
      Fills the entry fields with the coordinates
      of the ball
      """
      sx = 'x = %f' % self.x
      sy = 'y = %f' % self.y
      self.ex.delete(0,END)
      self.ex.insert(INSERT,sx)
      self.ey.delete(0,END)
      self.ey.insert(INSERT,sy)

   def Clear(self):
      """
      Clears the path
      """
      #print self.lines
      for i in range(len(self.lines)):
         self.c.delete(self.lines[i])
      self.c.update()
      

  
def main():
   top = Tk()
   dimension = 400 # dimension of pool table
   increment = 10  # increment for coordinates
   #delay = 60      # how much sleep before update
   #show = BilliardBall(top,dimension,increment,delay)
   show = BilliardBall(top,dimension,increment)
   top.mainloop()

if __name__ == "__main__": main()
