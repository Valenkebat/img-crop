import  os
import shutil
from pathlib import Path
import pandas as pd




pathP = Path('Procesar')
jsonArray = []

paths = Path('crudos').glob('*')
src_dir = os.getcwd() #get the current working dir
print(src_dir)
for fichero in paths:
    cont = 0
    nombreObra = fichero.name
    print(nombreObra)
    for image in fichero.glob("*.jpg"):
        cont = cont + 1
        nombreFoto = nombreObra + "_" + cont.__str__() + ".jpg"
        p=os.path.join(pathP,nombreFoto)
        if os.path.isfile(image):
            shutil.copy(image, p)

        # CARGO JSON
        jsonElement = {
            'IdProyecto': nombreObra,
            'CodigoBPIN': '',
            'UrlImagePequenia': '',
            'UrlImageMediana': '',
            'UrlImageGrande': '',
            'Descripcion': '',
            'Fecha': ''
        }
        jsonArray.append(jsonElement)

# CREO EXCEL
df = pd.DataFrame.from_dict(jsonArray, orient='columns')
df.to_csv('obras.csv', index=False, header=True)         