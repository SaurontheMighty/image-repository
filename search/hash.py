from PIL import Image

#Average Hashing Algorithm 

def aHash(img): 

    img.resize((128,128),Image.ANTIALIAS).save("smallgreybear.jpg")

    img = img.resize((8,8), Image.ANTIALIAS) #anti alias preserves quality
    img = img.convert("L") #greyscale

    pixels = list(img.getdata()) #a list of the pixels
    average = (sum(pixels))/len(pixels)

    bits="" #a list of 0s and 1s, length is 64 since 8*8
    for i in range (len(pixels)):
        if(pixels[i]>=average):
            bits = bits+"1"
        else:
            bits = bits+"0"

    imageHash = hex(int(bits, 2)).upper() # eg. 0xFDSKDFJHSKS

    return imageHash


def similar(hash1, hash2): # Image Search (Visually similar images)

    #remove the 0X
    hash1 = hash1[2:]
    hash2 = hash2[2:]

    # Both will be of length 16 (4 binary digits = 1 hex digit)
    c=0
    for i in range(16): # Hamming Distance: counts dissimilar digits
        if(hash1[i]!=hash2[i]):
            c+=1

    if(c<=4): #atleast 75% similar
        return True
    else:
        return False