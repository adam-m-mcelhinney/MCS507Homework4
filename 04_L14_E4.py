"""
HW4, #4
L14, #4
Consider the newtoniterator.py of Lecture 10 and make a
matplotlib animation to show the convergence of Newton’s
method. Set up the main() with some good examples.

Done

"""

import newtoniterator as n
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np



def animate(pw,x_lim,y_lim):
    """
    Shows the progress towards
    the dominant eigenvalue.
    """
    plt.ion()
    fig = plt.figure()
    ax = fig.add_subplot(111)
    #ax.set_xlim(float(x_lim[0]),float(x_lim[1]))
    #ax.set_ylim(float(y_lim[0]),float(y_lim[1]))
    #ax.set_xlim(0,105)
    #ax.set_ylim(1.4,1.52)
    x = [float((pw.step))]
    y = [float((pw.x))]
    #dots, = ax.plot(x,y,'ro')
    #fig.canvas.draw()
    for i in range(50):
        pw.next()
        print pw
        x.append(float(pw.step))
        print x
        y.append(float(pw.x))
        print y
        #dots.set_xdata(x)  # update data for plot
        #dots.set_ydata(y)
        plt.plot(x,y)
        plt.pause(.01)        # pause for a second
        fig.canvas.draw()   # update canvas
        #if pw.accurate(): break
        plt.show()
    



        



def main():
    f = lambda x: (x**8)/x - 2.0
    df = lambda x: (8.0*x**2-x**8)/x**2
    pw = n.NewtonIterator(f,df,1,n=200)
    animate(pw,[0,21],[1.4,1.42])
    


    




if __name__=="__main__":
            t=main()
            t.x
    
