#!/usr/bin/python

import os

import re
import time
from subprocess import call

sbt_pattern = re.compile(".*c$")
testPort = "9000"
grade = 0

for dir_entry in os.listdir('.'):
    if sbt_pattern.match(dir_entry):
        print ("processing file:" + dir_entry);
        
        result1 = call(["gcc", "-o", dir_entry + ".exe", dir_entry]);
        time.sleep(1)
        if (result1 == 0):
            grade = 20
            
            # Test 1

            print ("file:" + dir_entry + "compiled successfully!, result =" + str(result1) );
            exe_file = "./" + dir_entry + ".exe";
            print ("processing exe file: " + exe_file);
            f = open(exe_file + "test1.out",'w')
            lf = open(exe_file + "test1.err",'w')
            #time.sleep(1)
            result = call([exe_file, testPort, "test"], stdout=f, stderr=lf);
            testPort = str(int(testPort) + 1)
            lf.close();
            f.close()

            success = 0

            if (result == 0):
                print ("test1 exe file: " + exe_file +"returned 0, success!");
                grade += 30

            if (result != 0):
                print ("test1 exe file: " + exe_file +"returned " + str(result) + ", failure!");
                print ("test1 exe file: " + exe_file +"STDOUT= ");
                if (os.path.isfile(exe_file + "test1.out")):
                    f = open(exe_file + "test1.out",'r')
                    for line in f:
                        print (line);
                    f.close()
                else:
                    print ("test1 exe file: " + exe_file +"NO STDOUT!!");                    
                print ("test1 exe file: " + exe_file +"STDERR= ");
                if (os.path.isfile(exe_file + "test1.err")):                
                    f = open(exe_file + "test1.err",'r')
                    for line in f:
                        print (line);	
                    f.close()
                else:
                    print ("test1 exe file: " + exe_file +"NO STDERR!!");                                        

            print ("exe file: " + exe_file + "==>FINAL CLIENT GRADE = " + str(grade));
            
            print ("\n\n");
        if (result1 !=0):
            print ("file:" + dir_entry + "==>Compilation errors, result =" + str(result1));
            print ("exe file: " + exe_file + "==>FINAL CLIENT GRADE = " + str(grade));
            #time.sleep(1)
