# Standard imports:
import joblib
from skimage import io
from skimage.io import imread
from skimage import color
from sklearn.preprocessing import StandardScaler
from skimage.transform import rescale, resize
from skimage.feature import hog
import numpy as np
import asyncio

from PIL import Image

async def ktm(immagine): 
    # Parametri per ottenere l'HOG: devono essere gli stessi della classe HOG_TRANSFORMER (vedi file classify.py)
    orientations=9
    pixels_per_cell=(16, 16)
    cells_per_block=(2, 2)
    block_norm='L2-Hys'

    #------------------------------------------------------------------------------------------------------------#
    # Specifico il percorso: dove ho inserito la cartella dell'immagine da classificare:
    # path = "C:\\Users\\Utente\\Documents\\Marconi\\5\\pythonstuff"
    # path = "C:\\Users\\sulta\\Documents\\Python\\sklearn\\sklearn\\Midolo\\"
    
    # Importo il classificatore:
    custom_classifier = joblib.load('cipo.pkl')

    # Codice Sultanico:
    image_classify = Image.open(immagine)
    image_to_classify = np.asarray(image_classify)

    # Importo l'immagine da classificare:
    # image_to_classify =  io.imread("gianni_cumer_0.jpg" )

    # Eseguo trasformazioni:
    resized_image = resize(image_to_classify, (128, 128), anti_aliasing=True)
    grey_image = color.rgb2gray(resized_image)
    X_test_hog = hog(grey_image, orientations = orientations, pixels_per_cell = pixels_per_cell, cells_per_block = cells_per_block, block_norm = block_norm)

    # Per un singolo campione, mi tocca effettuare il reshape dell'array:
    # Così la shape risulta: (1, 1764)
    X_test_hog = X_test_hog.reshape(1, -1)

    y_pred =  custom_classifier.predict(X_test_hog)
    
    print(y_pred[0])
    print("Fine programma.")
    
    return (str(y_pred[0]))
