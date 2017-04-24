import os
i = 1
for name in os.listdir("/home/gopal/lab7/"): #put the name of the directory where the c programs are present
        if os.path.isfile(name):
             if ".c" in name:
                out = name.replace(".c","")
                display = "cat "+name+" >> outfile.odt " #outfile.odt is where the outputs will be stored
                compileit = "gcc "+name+" -lm -o "+out
                execute = "./" + out+" >> outfile.odt"
                os.system("echo " + str(i) + ".  >> outfile.odt")
                os.system(display)
                os.system("echo '\n' >> outfile.odt")
                os.system(compileit)
                os.system("echo 'output:' >> outfile.odt")
                os.system(execute)
                os.system("echo '\n' >> outfile.odt")
                i += 1
