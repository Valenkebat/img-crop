import subprocess
import os
import glob, os
import recursos as r
import pandas as pd
from datetime import date

today = date.today()

# dd/mm/YY
d1 = today.strftime("%d/%m/%Y")
# NECESITA smartcroppy

df = pd.read_csv('obras.csv')
retval = os.getcwd()

formatos = list(r.formatos.items())

# folder imgs
imgfolder = "Procesar"

jsonArray = []

os.chdir(os.path.dirname(__file__)+imgfolder)

for file in glob.glob("*.jpg"):
    namesArray = []
    file = os.path.splitext(file)[0]
    for form in formatos:

        size= form[0]
        wh = list(form[1].items())

        for key, value in wh:
            if key == 'width':
                width = value
            if key == 'height':
                height = value             
        
        nombre = "/Images/"+file+size+".jpg"
        
        namesArray.append(nombre)
        
        ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
        proc = subprocess.run("python "+ROOT_DIR+ "/../venv/lib/site-packages/smartcrop/__init__.py -W {width} -H {height} -i {file}.jpg -o ../output/{file}{size}.jpg".format(width=width,height=height,size=size,file=file))
        print(proc)
    
    jsonElement = {
            'UrlImagePequenia': namesArray[2],
            'UrlImageMediana': namesArray[1],
            'UrlImageGrande': namesArray[0],
            'Descripcion': '',
            'Fecha': ''
    }
    jsonArray.append(jsonElement)

os.chdir(retval)

df2 = pd.DataFrame(jsonArray)
df['UrlImagePequenia']=df2['UrlImagePequenia']
df['UrlImageMediana']=df2['UrlImageMediana']
df['UrlImageGrande']=df2['UrlImageGrande']
df['Fecha']=d1 

print(df)

df.to_excel('cargar.xlsx', index=False, header=True)