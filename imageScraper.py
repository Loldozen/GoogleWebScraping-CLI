#! python3
# This program accepts a url as a string, scrapes
# the Google images and returns the url of the first image
"""
 ToDo:
1. Get the search keyword for the CLI
2. Create a directory for the images
3. Download the pages with the requests module
4. Find the url of the image
5. Download the image
6. Save the image to the created directory
7. Return the url of the first image """

import requests,os,bs4,sys,webbrowser

search_keyword = 'https://google.com/search?q=' + '%20'.join(sys.argv[1:]) #1
#webbrowser.open(search_keyword)
search = requests.get(search_keyword, headers={'User-Agent':'Mozilla/5.0(Windows NT 10.0; Win64; x64) AppleWebkit/537.36(KHTML, like Gecko)'})#3
print('Downloading google search for %s ...' %search_keyword)
search.raise_for_status() # check if the download was succesful

os.makedirs('Images scraped', exist_ok=True) #2

soup = bs4.BeautifulSoup(search.text,features='html.parser')
print(soup)
imageElement = soup.select( 'body img')

if imageElement == []:
    print('Could not find image')
else:
    imageList = imageElement  #[0].get('src')
    for i in imageList:
        imageURL = imageList[i].get('src') #4
        print('Downloading image %s...' %imageURL)
        image = requests.get(imageURL)#5
        image.raise_for_status()
        # save the image to 'Image scraped' using its basename
        imageFile = open(os.path.join('Imaged scraped', os.path.basename(imageURL)), 'wb')
        for chunks in image.iter_content(100000):
            imageFile.write(chunks)
        imageFile.close()

    print('First image url is %s ' %imageList[0])
