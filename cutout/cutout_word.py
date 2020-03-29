from PIL import Image
import matplotlib.pyplot as plt 
import numpy as np

pic = np.array(Image.open('C:/Users/ky/Desktop/ps/words.png')) 
print(pic.shape) #((1030, 1853, 3))

N=35
for i in range(pic.shape[0]):
    for j in range(pic.shape[1]):
        if (pic[i][j][0] > N)&(pic[i][j][1] > N)&(pic[i][j][2] > N):
            pic.itemset((i,j,0),255)
            pic.itemset((i,j,1),255)
            pic.itemset((i,j,2),255)
        else:
            pic.itemset((i,j,0),0)
            pic.itemset((i,j,1),0)
            pic.itemset((i,j,2),0)
            
plt.imshow(pic)
plt.axis('off')
plt.savefig("result.jpg")
plt.show()
