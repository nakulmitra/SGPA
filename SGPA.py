import tkinter as tk
import pandas as pd

font=("Wide Latin",10)

def find():
    
    # Importing the dataset
    dataset = pd.read_csv(r'C:\Users\DELL\.spyder-py3\scripts\Industrial_Training_Project\SGPA\Result.csv')
    X = dataset.iloc[:, 1:-1].values
    y = dataset.iloc[:, -1].values
    
    # Training the Multiple Linear Regression model on the Training set
    from sklearn.linear_model import LinearRegression
    regressor = LinearRegression()
    regressor.fit(X, y)
    
    in_t=int(internal_theory_e.get())
    in_l=int(internal_lab_e.get())
    ex_t=int(external_theory_e.get())
    ex_l=int(external_lab_e.get())
    b=int(back_e.get())
    u=int(ufm_e.get())
    
    lst=[]
    lst.append(in_t)
    lst.append(in_l)
    lst.append(ex_t)
    lst.append(ex_l)
    lst.append(b)
    lst.append(u)
    
    ans=str(regressor.predict([lst]))
    ans=float(ans[1:len(ans)-1])
    ans=round(ans,2)
    result.config(text=ans)
    
    
root=tk.Tk()

root.title("SGPA Prediction")
root.config(bg="green")

frame=tk.Frame(root)
frame.pack(side="top",padx=10,pady=10,fill="x")
frame.config(bg="red")

internal_theory=tk.Label(frame,text="Enter Internal Theory Marks (180)",font=font,width=27,anchor="w")
internal_theory.grid(row=0,column=0,padx=5,pady=5)
internal_theory_e=tk.Entry(frame)
internal_theory_e.grid(row=0,column=1,padx=5,pady=5)

internal_lab=tk.Label(frame,text="Enter Internal Lab Marks (200)",font=font,width=27,anchor="w")
internal_lab.grid(row=1,column=0,padx=5,pady=5)
internal_lab_e=tk.Entry(frame)
internal_lab_e.grid(row=1,column=1,padx=5,pady=5)

external_theory=tk.Label(frame,text="Enter External Theory Marks (420)",font=font,width=27,anchor="w")
external_theory.grid(row=2,column=0,padx=5,pady=5)
external_theory_e=tk.Entry(frame)
external_theory_e.grid(row=2,column=1,padx=5,pady=5)

external_lab=tk.Label(frame,text="Enter External Lab Marks (200)",font=font,width=27,anchor="w")
external_lab.grid(row=3,column=0,padx=5,pady=5)
external_lab_e=tk.Entry(frame)
external_lab_e.grid(row=3,column=1,padx=5,pady=5)

back=tk.Label(frame,text="Enter Total no of Backs",font=font,width=27,anchor="w")
back.grid(row=4,column=0,padx=5,pady=5)
back_e=tk.Entry(frame)
back_e.grid(row=4,column=1,padx=5,pady=5)

ufm=tk.Label(frame,text="Enter Total no of UFM Cases",font=font,width=27,anchor="w")
ufm.grid(row=5,column=0,padx=5,pady=5)
ufm_e=tk.Entry(frame)
ufm_e.grid(row=5,column=1,padx=5,pady=5)

btn=tk.Button(root,text="Click",font=("Bodoni MT Black", 12),width=10,relief="solid",fg="#920323",command=find)
btn.pack(side="top",padx=10,pady=5)

result=tk.Label(root,text="",background="yellow",font=("Bodoni MT Black", 12))
result.pack(side="top",padx=10,pady=5,fill="x")

root.mainloop()

