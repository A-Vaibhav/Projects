import img2pdf

'''
combines multiple images and forms a pdf, 
condition is, all the images must be named sequentially
example : image1,image2,image3...
'''


list1 = []
for i in range(1,75):               # making the list(image1,image2,image3) manually, as os.listdir was unable to list them sorted
    list1.append(f'image{i}.jpg')

# print(list1)
    
with open('stock.pdf','wb') as f:       
    f.write(img2pdf.convert(list1))    # supply the list and it converts images to pdf
