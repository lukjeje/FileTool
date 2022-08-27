def FileTool():
  print(" ")
  D_or_C = input("(DF) for delete file, (CF) for create file, (DD) for delete Directory, (CD) for crete Directory, (X) for exit >>> ")

  if D_or_C == "CF":
   def CF(): 
    print(" ")
    print("insert your path to crate file for exeple /root/index.txt or /home/user/file.html and etc...")
    print("---------------------------------------------------------------------------------------------")
    pathinp = input("path >>> ")
    pathinp

    print(" ")

    print("write text if you like in your file")
    print("-------------------------------------")
    textinp = input("text >>> ")
    textinp

    print(" ")

    print("your file is created at: ", pathinp)
    print("------------------------------------")

    f = open(pathinp, "w")
    f.write(textinp)
    f.close()

    print(" ")
  
    cont = input("do you want to crete other file? (Y) for yes (N) for no: ")
    print(" ")

    if cont == "Y":
     CF()
    elif cont == "N":
     FileTool() 
   CF()    

  elif D_or_C == "DF":
   def DF():
    print(" ")
    print("insert your path to delete file for exeple /root/index.txt or /home/user/file.html and etc...")
    print("---------------------------------------------------------------------------------------------")
    pathinp = input("path >>> ")
    pathinp

    print(" ")

    import os
    if os.path.exists(pathinp):
     os.remove(pathinp)
     print("file was deleted")
     print("------------------")
    else:
     print("The file does not exist")
     print("-------------------------")

    print(" ")
  
    cont = input("do you want to delite other file? (Y) for yes (N) for no: ")
    print(" ")

    if cont == "Y":
       DF()
    elif cont == "N":
       FileTool()   
   DF()

  if D_or_C == "CD":
   def DC():

    print(" ")
    print("insert your path to crate Directory for exeple /root/files or /home/user/img and etc...")
    print("-----------------------------------------------------------------------------------------")

    pathinp = input("path >>> ")
    pathinp

    import os
    os.mkdir(pathinp)
    print(" ")
    print("Directory is created") 
    print("----------------------")

    print(" ")
    cont = input("do you want to crete other directory? (Y) for yes (N) for no: ")
    print("----------------------------------------------------------------------")
    print(" ")
    
    if cont == "Y":
      DC()
    elif cont == "N":
      FileTool()   

   DC()

  if D_or_C == "DD":
   def DD():
    print(" ")
    print("insert your path to delete Directory for exeple /root/files or /home/user/img and etc...")
    print("-----------------------------------------------------------------------------------------")

    pathinp = input("path >>> ")
    pathinp
 
    import shutil
    shutil.rmtree(pathinp)
    print(" ")
    print("Directory is deleted")
    print("----------------------")

    print(" ")
    cont = input("do you want to delete other directory? (Y) for yes (N) for no: ")
    print("-------------------------------------------------------------------------")
    print(" ")
    
    if cont == "Y":
      DD()
    elif cont == "N":
      FileTool()   

   DD()

  if D_or_C == "X":
    print(" ")
    print("FileTool closed") 
    print("-----------------")  

FileTool()


 

