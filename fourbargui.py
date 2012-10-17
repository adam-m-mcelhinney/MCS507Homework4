# L-15 MCS 507 Mon 1 Oct 2012 : GUI model for 4-bar mechanism

# The GUI consists of one canvas to draw a 4-bar mechanism.
# A 4-bar mechanism consists of four rigid bars.  The first bar, the crank,
# drives the mechanism.  The first two scales at the left regulate the 
# length of the crank and the angle of the crank.
# The horizontal scale below the canvas determine the position of the
# rightmost bottom joint, at the start of the right bar.

# The bar attached to the crank connects to the right bar.
# six scales and six corresponding labels.  Five of the six scales
# determine the lenghts of the bars of the mechanims, 

from Tkinter import *
from math import cos, sin, pi, sqrt
from fourbar import *

class FourBarGUI():
   """
   GUI to model a 4-bar mechanism.
   """ 
   def __init__(self,wdw,r,c):
      """
      Determines layout of the canvas,
      number of rows and colums is r and c.
      """
      wdw.title('a 4-bar mechanism')
      self.fbr = FourBar()
      self.rows = r; self.cols = c
      self.ox = c/3; self.oy = 3*r/4
      # print "A =" , (self.ox,self.oy)
      self.go = False
      # the canvas and start, stop, and clear buttons
      self.c = Canvas(wdw,width=self.cols,height=self.rows,bg='green')
      self.c.grid(row=1,column=2,columnspan=2)
      self.b0 = Button(wdw,text='start',command = self.start)
      self.b0.grid(row=3,column=2,sticky=W+E)
      self.b1 = Button(wdw,text='stop',command = self.stop)
      self.b1.grid(row=3,column=3,sticky=W+E)
      self.b2 = Button(wdw,text='clear',command = self.clear)
      self.b2.grid(row=3,column=4,columnspan=3,sticky=W+E)
      # the length of the crank
      self.crankLbl = Label(wdw,text='crank',justify=LEFT)
      self.crankLbl.grid(row=0,column=0)
      self.crankBar = IntVar()
      self.L = Scale(wdw,orient='vertical',from_=0,to=self.rows/2,\
         tickinterval=20,resolution=1,length=self.rows,\
         variable=self.crankBar,command=self.DrawMechanism)
      self.L.set(self.fbr.crank)
      self.L.grid(row=1,column=0)
      # the angle that drives the crank
      self.angleLbl = Label(wdw,text='angle',justify=LEFT)
      self.angleLbl.grid(row=0,column=1)
      self.angle = DoubleVar()
      self.t = Scale(wdw,orient='vertical',from_=0,to=6.30,\
         tickinterval=0.30,resolution=0.01,length=self.rows,\
         variable=self.angle,command=self.DrawMechanism)
      self.t.grid(row=1,column=1)
      self.angle.set(self.fbr.angle)
      # the bar at the right
      self.RightBarLbl = Label(wdw,text='right bar',justify=LEFT)
      self.RightBarLbl.grid(row=0,column=4)
      self.rightBar = IntVar()
      self.r = Scale(wdw,orient='vertical',from_=0,to=self.rows/2,\
         tickinterval=20,resolution=1,length=self.rows,\
         variable=self.rightBar,command=self.DrawMechanism)
      self.r.grid(row=1,column=4)
      self.rightBar.set(self.fbr.right)
      # the top bar attached to the crank
      self.topBarLbl = Label(wdw,text='top bar',justify=LEFT)
      self.topBarLbl.grid(row=0,column=5)
      self.RtopBar = IntVar()
      self.R = Scale(wdw,orient='vertical',from_=0,to=self.rows/2,\
         tickinterval=20,resolution=1,length=self.rows,\
         variable=self.RtopBar,command=self.DrawMechanism)
      self.R.grid(row=1,column=5)
      self.RtopBar.set(self.fbr.top)
      # the scale for the coupler bar
      self.CouplerBarLbl = Label(wdw,text='coupler',justify=LEFT)
      self.CouplerBarLbl.grid(row=0,column=6)
      self.couplerBar = IntVar()
      self.cpl = Scale(wdw,orient='vertical',from_=0,to=self.rows/2,\
         tickinterval=20,resolution=1,length=self.rows,\
         variable=self.couplerBar,command=self.DrawMechanism)
      self.cpl.grid(row=1,column=6)
      self.couplerBar.set(self.fbr.coupler)
      # the horizontal bottom bar
      self.flatLbl = Label(wdw,text='right joint',justify=RIGHT)
      self.flatLbl.grid(row=2,column=1)
      self.flat = IntVar()
      self.f = Scale(wdw,orient='horizontal',from_=0,to=self.rows/2,\
         tickinterval=50,resolution=1,length=self.cols,\
         variable=self.flat,command=self.DrawMechanism)
      self.f.grid(row=2,column=2,columnspan=2)
      self.flat.set(self.fbr.flat)
      # coordinates of the coupler point appear on top
      self.ex = Entry(wdw) # for x value
      self.ex.grid(row=0,column=2)
      self.ex.insert(INSERT,"x = ")
      self.ey = Entry(wdw) # for y value
      self.ey.grid(row=0,column=3)
      self.ey.insert(INSERT,"y = ")
      # check button for drawing of coupler curve
      self.curve = IntVar()
      self.cb = Checkbutton(wdw,text='coupler',\
        variable=self.curve,onvalue=1,offvalue=0)
      self.curve.set(1)
      self.cb.grid(row=3,column=0)
      # draw the mechanism on canvas
      self.DrawMechanism(0)

   def UpdateValues(self):
      """
      Takes all values of the scales and updates
      the data attributes of self.fbr.
      """
      self.fbr.flat = self.flat.get()
      self.fbr.crank = self.crankBar.get()
      self.fbr.top = self.RtopBar.get()
      self.fbr.right = self.rightBar.get()
      self.fbr.coupler = self.couplerBar.get()
      self.fbr.angle = self.angle.get()
      #self.fbr.PrintJoints()

   def DrawCouplerPoint(self,p):
      """
      Draws coupler point with coordinates in p
      if the curve checkbox is on.
      Note that the previous values for the coordinates
      of the coupler point are stored in the entry fields.
      """
      if self.curve.get() == 1:
         px = self.ox + p[0]; py = self.oy - p[1]
         eqx = self.ex.get(); Lx = eqx.split('='); 
         if Lx[1] == ' ':
            qx = 0.0
         else:
            qx = float(Lx[1])
         eqy = self.ey.get(); Ly = eqy.split('=');
         if Ly[1] == ' ':
            qy = 0.0
         else:
            qy = float(Ly[1])
         if (qx != 0.0) and (qy != 0.0):
            qx = self.ox + qx; qy = self.oy - qy
            self.c.create_line(qx,qy,px,py,width=1)

   def FillEntries(self,p):
      """
      Fills the entry fields with the coordinates
      of the coupler point in p.
      """
      sx = 'x = %f' % p[0]
      sy = 'y = %f' % p[1]
      self.ex.delete(0,END)
      self.ex.insert(INSERT,sx)
      self.ey.delete(0,END)
      self.ey.insert(INSERT,sy)

   def DrawLink(self,p,q,s):
      """
      Draws the link from point with coordinates in p
      to the point with coordinates in q, using s as tag.
      """
      self.c.delete(s)
      px = self.ox + p[0]; py = self.oy - p[1]
      qx = self.ox + q[0]; qy = self.oy - q[1]
      self.c.create_line(px,py,qx,qy,width=2,tags=s)

   def DrawMechanism(self,v):
      """
      Fills the canvas with the current model
      of the planar 4-bar mechanism.
      Because this command is called by the sliders,
      the argument v is needed but not used.
      """
      self.UpdateValues()
      L = self.fbr.Joints()
      for i in range(0,len(L)):
         p = L[i]
         px = self.ox + p[0]; py = self.oy - p[1]
         sj = 'joint%d' % i
         self.c.delete(sj)
         self.c.create_oval(px-6,py-6,px+6,py+6,width=1,\
            outline='black',fill='red',tags=sj)
      self.DrawLink(L[0],L[2],'link0')
      self.DrawLink(L[1],L[3],'link1')
      self.DrawLink(L[2],L[3],'link2')
      self.DrawLink(L[2],L[4],'link3')
      self.DrawCouplerPoint(L[4])
      self.FillEntries(L[4])

   def start(self):
      """
      Starts the animation, adding 0.01 to angle.
      """ 
      self.go = True
      while self.go:
         theta = self.angle.get()
         theta = theta + 0.01
         if theta > 6.28: theta = 0
         self.angle.set(theta)
         self.DrawMechanism(0)
         self.c.update()

   def stop(self):
      """
      Stops the animation.
      """
      self.go = False

   def clear(self):
      """
      Clears the canvas.
      """
      self.c.delete(ALL)

def main():
   top = Tk()
   r = 400; c = 600
   # r = 600; c = 800
   show = FourBarGUI(top,r,c)
   top.mainloop()

if __name__ == "__main__": main()
