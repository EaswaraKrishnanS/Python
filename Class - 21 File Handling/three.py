fp1 = open('data.txt','r')
data = fp1.read()
fp2 = open('bangalore.txt','w')
fp2.write(data)
fp3 = open('city.txt','a')
fp3.write(data)
print('New File Has Been Created!')
fp1.close()
fp2.close()
fp3.close()