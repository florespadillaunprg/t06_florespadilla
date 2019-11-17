import os
# BOLETA DE VENTA
# Declarar variables
empresa,nro_computadoras,p_u= "",0,0.0

# Input
empresa=os.sys.argv[1]
nro_computadoras=int(os.sys.argv[2])
p_u=float(os.sys.argv[3])

#Procesing
total= (p_u * nro_computadoras)

#Verificador
comprador_compulsivo=(total>38)
#Output
print("#######################")
print("######Boleta de venta######")
print("#")
print("#item:    ",nro_computadoras,"nro_computadoras")
print("#p.u:       S/.", p_u)
print("#total:     S/.",total)
print("#######################")
print("comprador compulsivo", comprador_compulsivo)

# Si el total supera a 38 obtiene una tarjeta black
if (comprador_compulsivo == True):
    print ("GANASTE LA TARJETA BLACK")

# Si el total es menor que 38 se le da una tarjeta golden
else:
    print ("GANASTE UNA TARJETA GOLDEN")

#FIN_IF
