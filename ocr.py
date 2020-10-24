from tkinter import*
from tkinter import filedialog
import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe"

def selectFile(en):
    en.delete(0,'end')
    filename=filedialog.askopenfilename(initialdir="C:\\Users\\{Username}\\Desktop",
                                        title="Select an Image",
                                        filetypes=(("all files", 
                                                        "*.*"),
                                                       ("JPEG files", 
                                                        "*.jpeg*")))
    en.insert(END,filename)

def ocr(file_path):
    #label.delete(1.0,END)
    img = cv2.imread(file_path)
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    height,width,_=img.shape
    output=pytesseract.image_to_string(img)
    label.insert(1.0,output)
    label.pack()
    print(type(output))
    boxes = pytesseract.image_to_data(img)
    for b in boxes.splitlines()[1:]:
        d = b.split()
        if len(d)==12:
            x,y,w,h = int(d[6]),int(d[7]),int(d[8]),int(d[9])
            cv2.rectangle(img,(x,y),(w+x,h+y),(0,0,255),1)
            #print(x,y,w,h)
    cv2.imshow('Result',img)
    cv2.waitKey(0)


root = Tk()

iFile=Label(root,text="Image File:")
iFile.pack()
ifEntry=Entry(root,width=50)
ifEntry.pack()
sButton=Button(root,text="Select File",command=lambda:selectFile(ifEntry))
sButton.pack(side='left')
label=Text(root)

cButton=Button(root,text="Convert",command=lambda: ocr(ifEntry.get()))
cButton.pack(side="right")


root.mainloop()
