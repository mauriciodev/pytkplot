'''
Created on 31/07/2013

@author: Mauricio de Paulo
'''
from math import *
from tkinter import *

class PyTkPlot(object):
    def __init__(self):
        '''
        Constructor
        Margins and scale can be set later.
        '''
        self.scaleX=1
        self.scaleY=1
        self.plotSizeX=300
        self.plotSizeY=300
        self.marginX=50
        self.marginY=self.plotSizeY+50
        
    def plotSeries(self,vX, vY):
        """Creates a new plot and plots a series."""
        self.scaleX=self.plotSizeX/(max(vX)-min(vX))
        self.scaleY=self.plotSizeY/(max(vY)-min(vY))
        self.marginX-=min(vX)*self.scaleX
        self.marginY+=min(vY)*self.scaleY
        self.plotSeriesRaw(vX,vY)
        
        
    def plotSeriesRaw(self, vX, vY):
        """Plots a series on an already scaled plot."""
        if len(vX)!= len(vY): 
            return False
        for i in range(0,len(vX)-1):
            self.plotLine(canvas, vX[i], vY[i], vX[i+1], vY[i+1])

    def plotLine(self,canvas, x0,y0,x1,y1,width=1):
        nx0=int(self.mapX(x0))
        nx1=int(self.mapX(x1))
        ny0=int(self.mapY(y0))
        ny1=int(self.mapY(y1))
        canvas.create_line(nx0,ny0,nx1,ny1,width=width)
    def plotText(self,canvas, x,y,text,anchor=N):
        nx=int(self.mapX(x))
        ny=int(self.mapY(y))
        canvas.create_text(nx,ny, text=text, anchor=anchor)
         
    def mapX(self,x):
            return floor(self.marginX+x*self.scaleX)
    def mapY(self,y):
            return floor(self.marginY-y*self.scaleY)
        
    def plotGrid(self,canvas, startX=0, endX=1500, startY=0, endY=1500,stepX=300,stepY=300):
        self.plotLine(canvas, startX, startY, startX, endY, 2)
        self.plotLine(canvas, startX, startY, endX, startY, 2)

        x=startX+stepX;
        while (x<endX):
            self.plotLine(canvas, x, startY, x, startY-5/self.scaleY, 2)
            self.plotText(canvas, x, startY-6/self.scaleY, '%d' % x, anchor=N)
            x += stepX
        
        y=startY+stepY;
        while (y<endY):
            #canvas.create_text(x0-4,y, text='%5.1f'% (y), anchor=E)
            self.plotLine(canvas, startX, y, startX-5/self.scaleX, y, 2)
            self.plotText(canvas, startX- 6/self.scaleX, y, "%d" % y, anchor=E)
            y+=stepY

   
    
    
if __name__=="__main__":
    test=PyTkPlot()
    root = Tk()
    root.title('Python Tk Plot Class')
    canvas = Canvas(root, width=400, height=400, bg = 'white')
    canvas.pack()
    Button(root, text='Quit', command=root.quit).pack()
    vX=[pi*x/100 for x in range(-200,400)]
    vY=[sin(x) for x in vX]
    test.plotSeries(vX, vY)
    root.mainloop()