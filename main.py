import pandas as pd
import matplotlib.pyplot as plt

# Asignar variables
data_columnas=["Operation date" , "Item","Value date","Amount","Balance","Reference1","Reference2"]
delete_columnas=["Reference1", "Reference2","Value date", "Balance"]
delete_filas= [0,1,2,3,4,5,6,7]

# Cargando excel
datos_bancarios= pd.read_excel("datos_bancarios_Jhon.xls")

# Asignando nombre de las columnas del excel
datos_bancarios.columns = data_columnas

# Eliminando columnas y filas
datos_bancarios.drop(delete_columnas,axis=1, inplace=True)
datos_bancarios.drop(delete_filas,axis=0,inplace=True)

# Aplicar logica
text_convertido={
    "supermercado":["aldi", "dia","lidl","alcampo","consum","carrefur","mercadona","splau","bon area","caprabo","seu & go","arap","coaliment","carniceria","disseu","fruteria","ca l'armengol", "boix","alimentacion",],
    "restaurant":["telepizza","cafeteria","café grill","gelats", "ben jhon","bar la cotxera", "domino","grad","rocknrolla", "bar res","son soles"],
    "gatos":["veterinaria","bazar","veteri","centre veterinari",],
    "ropa":["zalando","bershka","the north","decathlon", "esportiu",],
    "coche":["gasolinera","e s valenti","guisona t347",  ],
    "servicio basico":["electricity","iberdrola", "libertad", "concepción gutiérrez","transfer to concepcion gutierrez", ],
    "salud":["farmacia", ],
    "viajes":["vueling","ryanair",],
    "educacion":["udemy","universit","platzi"],
    "autonomo": ["cotizacion","associats", ],
    "varios":[ "bizum", "vivid money", "automatico", "jhon", "exp", ],
    "tecnologia": ["ale hop","hostinger","fiverr","xoami","xiaomi","the phone", ]
}

category_dict = {}
for key in text_convertido.keys():
    for value in text_convertido[key]:
        category_dict[value.lower()] = key


# Funcion para encontrar la categoria adecuada
def find_category(item, category_dict):
    item_lower = item.lower()
    for keyword, category in category_dict.items():
        if keyword in item_lower:
            return category
    return "Desconocido"


# Pasando Item a minuscula y poniedo la categoria
datos_bancarios["Item"] = datos_bancarios["Item"].apply(lambda elemento: elemento.lower())

datos_bancarios["Category"] = datos_bancarios["Item"].apply(lambda x: find_category(x, category_dict))

# Eliminar filas con categorías varias y montos mayores a 120
datos_bancarios = datos_bancarios.loc[(datos_bancarios["Category"] != "varios") |
                                      ((datos_bancarios["Category"] == "varios") &
                                       (datos_bancarios["Amount"].abs() <= 120))]

# Crear archivo "desconocido.csv" con filas con categorías desconocidas
desconocido = datos_bancarios[datos_bancarios["Category"] == "Desconocido"]
desconocido.to_csv("desconocido.csv", index=False)

# Crear columna de año
datos_bancarios['Year'] = datos_bancarios['Operation date'].apply(lambda x: x.split("/")[2])

# crear dos dataframes
gastos=datos_bancarios[datos_bancarios["Amount"]  <0  ]
ingresos =datos_bancarios[datos_bancarios["Amount"]  >0 ]


# Pasando a positivo los valores de gastos
gastos["Amount"] =- gastos["Amount"]


# Obtener años únicos
years = gastos["Year"].unique()

# Graficar
for year in years:
    # Filtrar por año
    data = gastos[gastos["Year"] == year]
    # Agrupar por categoría y sumar los montos
    grouped_data = data.groupby("Category")["Amount"].sum()
    # Graficar
    plt.bar(grouped_data.index, grouped_data.values, label=year, width=0.8)

# Configurar gráfico
plt.title("Gastos por categoría y año")
plt.xlabel("Categoría")
plt.ylabel("Gasto")
plt.legend()
# Rotar etiquetas del eje x para que se puedan ver todas
plt.xticks(rotation=45, ha='right')

# Mostrar gráfico
plt.show()