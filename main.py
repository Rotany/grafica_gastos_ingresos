import pandas as pd

# Asignar variables
data_columnas=["Operation date" , "Item","Value date","Amount","Balance","Reference1","Reference2"]
delete_columnas=["Reference1", "Reference2","Value date", "Balance"]
delete_filas= [0,1,2,3,4,5,6,7]

# Cargando excel
datos_bancarios= pd.read_excel("datos_bancarios_Jhon.xls")

# Asignando nombre de las columnas del excel
datos_bancarios.columns =data_columnas

# Eliminando columnas y filas
datos_bancarios.drop(delete_columnas,axis=1, inplace=True)
datos_bancarios.drop(delete_filas,axis=0,inplace=True)



# Aplicar logica
text_convertido={
    "supermercado":["aldi", "dia","lidl","alcampo","comsum","carrefur","mercadona","splau","bon area"]
}
text_esperado=[
"ALDI",
"DIA",
"ESPORTIU",
"SERVICIO BASICO",
"BIZUM",
"VIVID MONEY",
"MERCADONA",
"ZALANDO", 
"VUELING",
"BAZAR", 
"BAR RES",
"VETERINARIA",
"FARMACIA",
"XOAMI",
"GASOLINERA",
"UDEMY",
"AUTOMATICO",
"ASSOCIATS",
"COMISIONS",
"JHON",
"CONCEPCIÓN GUTIÉRREZ",
"TELEPIZZA",
"BON AREA",
"FARMACIA",
"ELECTRICITY",
"CAPRABO",
"VETERI",
"SEU & GO",
"EXP",
"COTIZACION",
"CAFETERIA",
"CARNICERIA",
"FRUTERIA",
"CENTRE VETERINARI",
"CA L'ARMENGOL",
"UNIVERSIT",
"BERSHKA",
"BASAR",
"BAR LA COTXERA",
"BOIX",
"BEN JHON",
"CAFÉ GRILL",
"CARREF",
"ALIMENTACION",
"COALIMENT",
"DECATHLON",
"GELATS",
"GRAD",
"E S VALENTI",
"LIDL",
"XIAOMI",
"THE NORTH",
"THE PHONEx",
"TRANSFER TO CONCEPCION GUTIERREZ",
"RYANAIR",
"ROCKNROLLA",
"DISSEU",
"DOMINO",
"GUISONA T347",
"COMISSIONS",
"CONSUM",
"ALE HOP",
"FIVERR",
"HOSTINGER" ,
"ARAP",
"ALCAMPO"
]

# Mostrando resultados
print (datos_bancarios.head(10))