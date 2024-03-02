from fastapi import FastAPI

# funciones para generar las respuestas de la api
from functions.compareImages.compare_images import calcular_similitud_M
from functions.scannerHand.scanner_hand import detectar_lineas_palma

#Esquemas de la app
from schemes.schemeHand import Hand




app = FastAPI()

##Tags de la documentacion generada por Fast API
app.title = "Michelob Hand scanner API"

app.version = "1.0.0"

@app.post('/scanner', tags=['scanner'])

##la funcion ira en esta parte, recibira como parametro la imagen de la mano
async def handScanner(hand: Hand):

    handInfo = []

    handInfo.append(hand.model_dump())

    if handInfo:
        try:       
            # Marca las lineas de la palma y devuelve la imagen con las lienas remarcadas
            scannHand = await detectar_lineas_palma(hand.image)

            # Recibe la imagen hace el calculo de similitus y devuelve el porcentaje de similitud
            #compareImage = calcular_similitud_M(scannHand) 

            if scannHand:

                #response = [
                #    {
                #        'similitud' : compareImage
                #    }
                #]

                response = [
                    {
                        'imagen' : scannHand
                    }
                ]


                return response
    
    
        except:
            respuesta = [
                {
                    'datos': 'Los datos ingresados son incorrectos'
                }
            ]
            return respuesta
    else:
        respuesta = [
            {
                'datos': 'Datos incorrectos'
            }
        ]
        return respuesta

    
    ##aqui ira la funcion que retornara un json con la imagen codificada en base 64