import PastecLib


# open pastec
c = PastecLib.PastecConnection()
c.clearIndex()
#c.loadIndex("pastecIndex")

# index the images_db into pastecIndex
for i in range(1, 100):
        c.indexImageFile(i, "/home/brunoob/StampProject/Images_db/"+str(i)+".jpg")

c.writeIndex("pastecIndex")
print ('done')
