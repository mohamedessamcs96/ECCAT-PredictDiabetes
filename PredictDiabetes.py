
import tkinter as tk
from sklearn.externals import joblib
window =tk.Tk()
window.title("Predicting Diabetes")
window.geometry("400x400")


def prediction():
    
    #label6
    label10=tk.Label(window,text='')
    label10.grid(row=11,column=1)


    num_preg=int(entry1.get())
    glucose_conc=int(entry2.get())
    diastolic_bp=int(entry3.get())
    thickness=int(entry4.get())
    insulin=int(entry5.get())
    bmi=int(entry6.get())
    diab_pred=int(entry7.get())
    age= int(entry8.get())
    skin=int(entry9.get())
    
    clf=joblib.load('ECCATDiabetes')
    data=clf.predict([[num_preg,glucose_conc,diastolic_bp,thickness,insulin,bmi,diab_pred,age,skin]])
    for i in range(1):
        if(data[i]==0):
            label10.config(text="Has No Diabetes")    

        elif(data[i]==1):
            label10.config(text="Has Diabetes")      
    
    




#Label
label=tk.Label(text="Predicting Diabetes",font=("Times new Roman",20))
label.grid(row=0,column=1)

"""num_preg"""
#label
label1=tk.Label(text="num_preg:")
label1.grid(row=1,column=0)

#entryfield
entry1=tk.Entry()
entry1.grid(row=1,column=1)
"""num_preg"""

"""glucose_conc"""
label2=tk.Label(text="glucose_conc:")
label2.grid(row=2,column=0)

#entryfield
entry2=tk.Entry()
entry2.grid(row=2,column=1)

"""glucose_conc"""


"""diastolic_bp"""
label3=tk.Label(text="diastolic_bp:")
label3.grid(row=3,column=0)

#entryfield
entry3=tk.Entry()
entry3.grid(row=3,column=1)

"""diastolic_bp"""


"""thickness"""
label4=tk.Label(text="thickness:")
label4.grid(row=4,column=0)

#entryfield
entry4=tk.Entry()
entry4.grid(row=4,column=1)

"""thickness"""

"""insulin"""
label5=tk.Label(text="insulin:")
label5.grid(row=5,column=0)

#entryfield
entry5=tk.Entry()
entry5.grid(row=5,column=1)

"""insulin"""

"""bmi"""
label6=tk.Label(text="bmi:")
label6.grid(row=6,column=0)

#entryfield
entry6=tk.Entry()
entry6.grid(row=6,column=1)

"""bmi"""

"""diab_pred"""
label7=tk.Label(text="diab_pred:")
label7.grid(row=7,column=0)

#entryfield
entry7=tk.Entry()
entry7.grid(row=7,column=1)

"""diab_pred"""


"""age"""
label8=tk.Label(text="age:")
label8.grid(row=8,column=0)

#entryfield
entry8=tk.Entry()
entry8.grid(row=8,column=1)

"""age"""

"""skin"""
label9=tk.Label(text="skin:")
label9.grid(row=9,column=0)

#entryfield
entry9=tk.Entry()
entry9.grid(row=9,column=1)

"""skin"""


#button
button1=tk.Button(text="Calculate",command=prediction)
button1.grid(row=10,column=1)

window.mainloop()  
    
