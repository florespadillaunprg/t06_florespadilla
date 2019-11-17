import os
# BOLETA DE VENTA
# Declarar variables
empresa,nro_computadoras,p_u= "",0,0.0

# Input
empresa=os.sys.argv[1]
nro_computadoras=os.sys.argv[2]
p_u=float(os.sys.argv[3])

#Procesing
total= (p_u * nro_computadoras)

#Verificador
comprador_compulsivo=(total>384)
#Output
print("#######################")
print("######Boleta de venta######")
print("#")
print("#item:    ",nro_computadoras,"nro_computadoras")
print("#p.u:       S/.", p_u)
print("#total:     S/.",total)
print("#######################")
print("comprador compulsivo", comprador_compulsivo)

# Si el total supera a 384 obtiene una tarjeta black
if (comprador_compulsivo == True):
    print ("GANASTE LA TARJETA BLACK")
# Si el total es menor que 384 se le da una tarjeta golden
if (comprador_compulsivo == True):
    print ("GANASTE UNA TARJETA GOLDEN")
# Si el total no es mayor que 370 tiene una tarjeta platinum
if (comprador_compulsivo == True):
    print ("GANASTE UNA TARJETA PLATINUM")

#FIN_IF
