import os
# BOLETA DE VENTA
# Declarar variables
cliente,kg,P_u ="",0,0.0

# Input
cliente=os.sys.argv[1]
kg=int(os.sys.argv[2])
P_u=float(os.sys.argv[3])

#Procesing
total= (P_u * kg)

#Verificador
comprador_compulsivo=(total>30)

#Output
print("#########################")
print("######Boleta de venta########")
print("#########################")
print("#")
print("# cliente:", cliente)
print("#item:    ",kg,"kg")
print("#P.U:      S/.", P_u)
print("#total:    S/.",total)
print("##########################")
print("comprador compulsivo", comprador_compulsivo)

# Si el total es mayor a 30 obtendran un bono especial
if (comprador_compulsivo == True):
    print ("OBTUVISTE UN BONO ESPECIAL")
# Si el total es menor a 30 obtiene una rifa
if (comprador_compulsivo ==True):
    print ("GANASTEM UNA RIFA")
# Si el comprador es recurrente gana un kg gratis
if (comprador_compulsivo ==True):
    print ("GANASTE UN KG GRATIS")

#FIN_IF
