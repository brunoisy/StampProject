import PastecLib


# open pastec
c = PastecLib.PastecConnection()
c.clearIndex()
c.loadIndex("pastecIndex")

# match images from Images_to_match with images from pastecIndex
for i in range(1, 100):
        res = c.imageQueryFile(self,"/home/brunoob/StampProject/Images_to_match/"+str(i)+".jpg"):
        if res != [] # match!
                print('MATCH for image' + str(i) + ".jpg with indexed image" + str(res[0]) + ".jpg")#! there could be more than one match
		

print ('done')
