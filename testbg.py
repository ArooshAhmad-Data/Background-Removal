from rembg import remove

image = "download.jpg"
output = "Output1.jpg"

with open(image,'rb') as i:
    with open(output,'wb') as o:
        input = i.read()
        output = remove(input)
        o.write(output)

print("Called !")