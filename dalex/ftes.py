f = open("C:/Users/lab/Desktop/ates.txt", 'r+')

# for Hat
for i in range(1016,2031):
    f.write("C:/Users/lab/Desktop/val_data/"+str(i)+".jpg"+" 1")
    f.write("\n")

# for Mask
for i in range(1016,1824):
    f.write("C:/Users/lab/Desktop/val_data/"+str(i)+" (3).JPG"+" 2")
    f.write("\n")

# for Sunglasses
for i in range(1016,2001):
    f.write("C:/Users/lab/Desktop/val_data/"+str(i)+" (2).JPG"+" 3")
    f.write("\n")

f.close()
