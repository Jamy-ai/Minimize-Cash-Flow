from tkinter import *
import numpy as np
root=Tk()
root.title("Min Cash Flower")
root.geometry("700x500")
root.configure(bg="bisque2")

n=0
names=[]
text_var = []

def getNames():
    global names
    global n
    names=[]
    names.extend(name_of_people.get().split(" "))
    print(names)
    createNewWindow()

def getMin(net):
    ind=0
    for i in range(1,n):
        if(net[i]<net[ind]):
            ind=i
    return ind

def getMax(net):
    ind=0
    for i in range(1,n):
        if(net[i]>net[ind]):
            ind=i
    return ind

def minOf2(x,y):
    return y if x>y else x

def rec(net,ans):
    debitor=getMin(net)
    creditor=getMax(net)

    if(net[debitor]==0 and net[creditor]==0):
        return 0

    flow=minOf2(-net[debitor],net[creditor])
    net[debitor]+=flow
    net[creditor]-=flow
    ans[debitor][creditor]=flow
    rec(net,ans)

def showResult(ans):
    result=Toplevel(root)
    print(ans)
    resultCanvas=Canvas(result,width=1000,height=1000,bg="pink")
    resultCanvas.grid(columnspan=n+2,rowspan=n+2)
    for i in range (n):
        Label(result, text=names[i], font=('arial', 10, 'bold'), bg="black", fg="white").grid(column=i + 1, row=0)
        Label(result, text=names[i], font=('arial', 10, 'bold'), bg="black", fg="white").grid(column=0, row=i + 1)

    for i in range(n):
        for j in range(n):
            Label(result,text=ans[i][j], font=('arial', 10, 'bold'), bg="yellow", fg="black").grid(column=j+1,row=i+1)



def minCashFlow(matrix):
    net=[]
    for i in range(n):
        temp=0
        for j in range(n):
            temp+=matrix[j][i]-matrix[i][j]
        net.append(temp)
    ans=np.zeros((n,n))
    rec(net,ans)
    print(ans)
    showResult((ans))

def get_mat():
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(n):
            matrix[i].append(int(text_var[i][j].get()))

    print(matrix)
    minCashFlow(matrix)

def createNewWindow():
    print(names)
    print(n)
    global text_var
    matrix = Toplevel(root)
    matrix.title("MATRIX")
    matrix.geometry("1000x1000")
    matrix.configure(bg="pink")
    canvas=Canvas(matrix,width=1000,height=1000,bg="pink")
    canvas.grid(columnspan=n+2,rowspan=n+2)
    for i in range(n):
        Label(matrix,text=names[i],font=('arial', 10, 'bold'),bg="black",fg="white").grid(column=i+1,row=0)
        Label(matrix,text=names[i],font=('arial', 10, 'bold'),bg="black",fg="white").grid(column=0,row=i+1)
    text_var=[]
    entries=[]
    Button(matrix, text="SUBMIT",command=get_mat, bg="#20bebe").grid(column=1, row=n+1)
    for i in range(n):
        text_var.append([])
        entries.append([])
        for j in range(n):
            text_var[i].append(StringVar())
            entries[i].append(Entry(matrix,textvariable=text_var[i][j],width=7))
            entries[i][j].grid(column=j+1,row=i+1)


def getN():
    global n
    n=int(no_of_people.get())
    print(n)


Label(root,text="Enter no of person :",font=('arial', 10, 'bold'),bg="black",fg="white").place(x=20,y=20)
no_of_people=Entry(root,width=10)
no_of_people.place(x=180,y=20)
Button(root,text="Enter",bg="#20bebe",width=15,height=1,command=getN).place(x=270,y=15)

Label(root, text="Enter names :", font=('arial', 10, 'bold'), bg="black", fg="white").place(x=20, y=50)
name_of_people = Entry(root, width=10)
name_of_people.place(x=180, y=50)
Button(root, text="Enter", bg="#20bebe", width=15, height=1, command=getNames).place(x=270, y=45)


root.mainloop()