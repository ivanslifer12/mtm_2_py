f1=open("finalresults.txt",'r')
f2=open("output.txt",'r')
final1=f1.readlines()
final2=f2.readlines();
counter=0;
for i in range(1,51):
    if(final1[i-1]==final2[i-1]):
        print("test " + str(i) +" passed \n")
        counter+=1
    else:
        print("test " + str(i) + "failed \n")
print("total result: "+str(counter)+" passed from 50 tests")