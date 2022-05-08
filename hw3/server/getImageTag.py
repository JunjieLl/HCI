
import os
from os import path
import re
os.chdir(path.dirname(__file__))

def getImageKind(images: list):
    favoPath = r'./favo/favo.txt'
    if not path.exists(favoPath):
        open(favoPath,'w').close()
    with open(favoPath) as f:
        ls = f.readlines()
    favos = set(list(map(lambda x: x.strip(),ls)))
    
    pattern = re.compile(r"(?<=im)\d+(?=\.jpg)")
    res = []
    
    for image in images:
        match = pattern.search(image)
        if match:
            imageIndex = match.group(0)
            res.append({
                'imageUrl':image,
                'imageIndex':imageIndex,
                'kinds':[],
                "isFavo": imageIndex in favos
            })
    print(res)
    print(type(res[0]['isFavo']))
    
    files = []
    for i in os.walk("./database/tags"):
        files = i[2]
    print(files)
    
    totalKinds = set()
    for file in files:
        if file=='.gitkeep' or file=='README.txt':
            continue
        filePath = path.join("database","tags",file)
        print(filePath)
        with open(filePath) as f:
            curKind = file.split('.')[0].title()
            
            lines = list(map(lambda x: x.strip(),f.readlines()))
            for index in range(len(res)):
                if res[index]['imageIndex'] in lines:
                    res[index]['kinds'].append(curKind)
                    totalKinds.add(curKind)
    
    print(res)
    totalKinds = sorted(list(totalKinds))
    print(totalKinds)
    return {'images':res,'kinds':totalKinds}
            
if __name__ == '__main__':
    getImageKind(
        [
            "/result/im1427.jpg",
            "/result/im45.jpg",
            "/result/im2895.jpg",
            "/result/im403.jpg",
            "/result/im2006.jpg",
            "/result/im928.jpg",
            "/result/im1260.jpg",
            "/result/im1516.jpg",
            "/result/im2906.jpg"
            ]
        )
    