'''
Created on 31/07/2013

@author: Mauricio de Paulo
'''
from math import *
from tkinter import *

class PyTkPlot(object):
    def __init__(self,canvas):
        '''
        Constructor
        Margins and scale can be set later.
        '''
        self.canvas=canvas
        self.dec="%.2f"
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
        self.plotGrid(min(vX), max(vX), min(vY), max(vY),(max(vX)-min(vX))/5,(max(vY)-min(vY))/5)
        self.plotSeriesRaw(vX,vY)
        
        
    def plotSeriesRaw(self, vX, vY):
        """Plots a series on an already scaled plot."""
        if len(vX)!= len(vY): 
            return False
        for i in range(0,len(vX)-1):
            self.plotLine(vX[i], vY[i], vX[i+1], vY[i+1])

    def plotLine(self, x0,y0,x1,y1,width=1):
        nx0=int(self.mapX(x0))
        nx1=int(self.mapX(x1))
        ny0=int(self.mapY(y0))
        ny1=int(self.mapY(y1))
        self.canvas.create_line(nx0,ny0,nx1,ny1,width=width)
    def plotText(self, x,y,text,anchor=N):
        nx=int(self.mapX(x))
        ny=int(self.mapY(y))
        self.canvas.create_text(nx,ny, text=text, anchor=anchor)
         
    def mapX(self,x):
            return floor(self.marginX+x*self.scaleX)
    def mapY(self,y):
            return floor(self.marginY-y*self.scaleY)
        
    def plotPoint(self,x,y,size=2):
        rx=size/self.scaleX
        ry=size/self.scaleY
        self.canvas.create_oval(self.mapX(x-rx),self.mapY(y-ry),self.mapX(x+rx),self.mapY(y+ry))
                
        
    def plotGrid(self, startX=0, endX=1500, startY=0, endY=1500,stepX=300,stepY=300):
        self.plotLine(startX, startY, startX, endY, 2)
        self.plotLine(startX, startY, endX, startY, 2)

        x=startX+stepX;
        while (x<endX):
            self.plotLine(x, startY, x, startY-5/self.scaleY, 2)
            self.plotText(x, startY-6/self.scaleY, self.dec % x, anchor=N)
            x += stepX
        
        y=startY+stepY;
        while (y<endY):
            #canvas.create_text(x0-4,y, text='%5.1f'% (y), anchor=E)
            self.plotLine(startX, y, startX-5/self.scaleX, y, 2)
            self.plotText(startX- 6/self.scaleX, y, self.dec % y, anchor=E)
            y+=stepY

   
    
    
if __name__=="__main__":
    
    root = Tk()
    root.title('Python Tk Plot Class')
    canvas = Canvas(root, width=400, height=400, bg = 'white')
    canvas.pack()
    test=PyTkPlot(canvas)
    print(dir(canvas))
    Button(root, text='Quit', command=root.quit).pack()
    vX=[pi*x/100 for x in range(-200,400)]
    vY=[sin(x) for x in vX]
    test.plotSeries(vX, vY)
    test.plotPoint(0, 0)
    root.mainloop()