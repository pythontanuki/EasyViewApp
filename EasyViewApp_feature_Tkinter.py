from tkinter import *
import tkinter.filedialog
import os 
import sys
from PIL import ImageTk, Image

root = Tk()
root.title("Swapman ViewerApp")


global imgList
imgList = []

def getFilePath():
    fileTypes = [("画像", "*.png")]
    idir = os.path.expanduser("~")
    fileAbsPath = tkinter.filedialog.askopenfilename(filetypes=fileTypes, initialdir=idir)
    if fileAbsPath == "":
        return "cancel!!"
    return fileAbsPath

def openImage():
    fileAbsPath = getFilePath()
    if fileAbsPath == "cancel!!":
        return
    img = Image.open(fileAbsPath)
    img = img.resize((400, 600))
    ImgObg = ImageTk.PhotoImage(img)
    addImage(ImgObg)
    return

def addImage(ImgObj):
    imgList.append(ImgObj)
    return

def deleteImage():
    return

openImage()
if len(imgList) != 0:
    myLabel = Label(image=imgList[0])
    myLabel.grid(row=0, column=0, columnspan=3)

def backward(imageNumber):
    global myLabel
    global forwardButton
    global backwardButton
    global exitButton
    global addButton
    if imageNumber == 0:
        backwardButton = Button(root, text="<<", state=DISABLED)
        return
    myLabel = Label(image=imgList[imageNumber-1])
    backwardButton = Button(root, text="<<", command=lambda: backward(imageNumber-1))
    forwardButton = Button(root, text=">>", command=lambda: forward(imageNumber-1))
    exitButton = Button(root, text="exit", command=root.quit)
    addButton = Button(root, text="add", command=lambda: openImage())
    myLabel.grid(row=0,column=0,columnspan=3)
    backwardButton.grid(row=1,column=0)
    exitButton.grid(row=1,column=1)
    forwardButton.grid(row=1,column=2)
    addButton.grid(row=2,column=0)
    delete.grid(row=2, column=1)
    return

def forward(imageNumber):
    global myLabel
    global forwardButton
    global backwardButton
    global exitButton
    global addButton
    lastImgIdx = len(imgList)
    if imageNumber == lastImgIdx-1:
        forwardButton = Button(root, text=">>", state=DISABLED)
        return
    myLabel = Label(image=imgList[imageNumber+1])
    backwardButton = Button(root, text="<<", command=lambda: backward(imageNumber+1))
    forwardButton = Button(root, text=">>", command=lambda: forward(imageNumber+1))
    exitButton = Button(root, text="exit", command=root.quit)
    addButton = Button(root, text="add", command=lambda: openImage())
    myLabel.grid(row=0,column=0,columnspan=3)
    backwardButton.grid(row=1,column=0)
    exitButton.grid(row=1,column=1)
    forwardButton.grid(row=1,column=2)
    addButton.grid(row=2, column=0)
    deleteButton.grid(row=2,column=1)
    return

backwardButton = Button(root, text="<<", command=lambda: backward(0))
forwardButton = Button(root, text=">>", command=lambda: forward(0))
exitButton = Button(root, text="exit", command=root.quit)
addButton = Button(root, text="add", command=lambda: openImage())
deleteButton = Button(root, text="delete", command=delete)

backwardButton.grid(row=1,column=0)
exitButton.grid(row=1,column=1)
forwardButton.grid(row=1,column=2)
addButton.grid(row=2, column=0)
deleteButton.grid(row=2, column=1)

root.mainloop()
