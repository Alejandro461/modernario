memes = { "CRINGE": "Algo excepcionalmente raro o embarazoso",
             "LOL": "Una respuesta común a algo gracioso",
             "ROFL": "una respuesta a una broma",
             "SHEESH": "ligera desaprobación",
             "CREEPY": "aterrador, siniestro",
             "AGGRO": "ponerse agresivo/enojado",
            }
print("Hola bienvenido al diccionario moderno")
for i in range(6):
    word = input("Escribe una palabra que no sepas lo que significa (¡usa mayúsculas!): ")
    if word in memes.keys():
        print(word,"significa:",memes[word])
    else:
        print("Ni yo se lo que significa")
