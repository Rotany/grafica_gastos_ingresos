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

# Mostrando resultados
print (datos_bancarios.head(10))