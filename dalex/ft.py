f = open("C:/Users/lab/Desktop/ar.txt", 'r+')

# for Hat
for i in range(0,1016):
    f.write("C:/Users/lab/Desktop/train_data/"+str(i)+".jpg"+" 1")
    f.write("\n")

# for Mask
for i in range(1,1016):
    f.write("C:/Users/lab/Desktop/train_data/"+str(i)+" (2).JPG"+" 2")
    f.write("\n")

# for Sunglasses
for i in range(1,1016):
    f.write("C:/Users/lab/Desktop/train_data/"+str(i)+" (3).JPG"+" 3")
    f.write("\n")

f.close()
