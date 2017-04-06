import os

outdir = "Outputs/"
for name in os.listdir("/home/gopal/lab7/"):
        if os.path.isfile(name):
                out = outdir+name.replace(".c","")
                display = "cat "+name+" >> outfile.txt "
                compileit = "gcc "+name+" -lmo"+out
                execute = "./" + out+" >> outfile.txt "
                os.system(display)
                os.system("echo '\n'")
                os.system(compileit)
                os.system("echo 'output:'")
                os.system(execute)
                os.system("echo '\n' ")
              
