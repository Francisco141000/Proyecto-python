#!/usr/bin/env python
# coding: utf-8

# In[1]:


# funcion suma
def suma ():
    print ("\nSUMA\n")
    archivo = open ('complejos.txt','a')
    archivo.write ("\nSUMA\n")
    print ("Introduce z1")
    z1 = complex (input ())
    print ("Introduce z2")
    z2 = complex (input ())
    print ("La suma de z1 + z2 es:")
    archivo.write ("La suma de z1 + z2 es:\n")
    print (z1, "+", z2, "=", z1+z2)
    archivo.write (str(z1) + "+" + str(z2) + "=" + str(z1+z2) + "\n")


# In[2]:


# funcion producto
def producto ():
    archivo = open ('complejos.txt','a')
    print ("\nPRODUCTO\n")
    archivo.write ("\nPRODUCTO\n")
    print ("Introduce z1")
    z1 = complex (input ())
    print ("Introduce z2")
    z2 = complex (input ())
    print ("El producto de z1 * z2 es:")
    archivo.write ("El producto de z1 * z2 es:\n")
    print (z1, "*", z2, "=", z1*z2)
    archivo.write (str(z1) + "*" + str(z2) + "=" + str(z1*z2) + "\n")


# In[3]:


#funcion potencia
def potencia ():
    archivo = open ('complejos.txt','a')
    print ("\nPOTENCIA\n")
    archivo.write ("\nPOTENCIA\n")
    print ("Introduce z")
    z = complex (input ())
    print ("Introduce la potencia")
    n = int (input ())
    p = pow (z,n)
    print ("La potencia de z a la n es:")
    archivo.write ("La potencia de z a la n es:\n")
    print (z , "^" , n , "=" , p)
    archivo.write (str(z) + "^" + str(n) + "=" + str(p) + "\n")


# In[4]:


def captura():
    print("Ingresa los valores del polinomio 1 iniciando desde el termino independiente")
    for i in range (g):
        if (i==0):
            c=int(input("valor independiente:"))
            pol1.append(c)
        else:
            print("coeficioente ", i," :", end=" ")
            c=int(input())
            pol1.append(c)
    print("Ingresa los valores del polinomio 2 iniciando desde el termino independiente")       
    for i in range (g):
        if (i==0):
            c=int(input("valor independientemente:"))
            pol2.append(c)
        else:
            print("coeficiente ", i, " :", end=" ")
            c=int(input())
            pol2.append(c)


# In[5]:


def sumaP():
    archivo = open('polinomio.txt', 'w')
    archivo.write ("Polinomios:")
    for i in range (g):
        c=pol1[i]+pol2[i]
        res.append(c)
    print(" polinomio1 + polinomio2 = ")
    archivo.write (" polinomio1 + polinomio2 = ")
    for i in range (2,-1,-1):
        if (i==0):
            print ("(", pol1[i], ")")
            archivo.write ("(" + str(pol1[i]) + ")")
        else:
            print ("(",pol1[i], "x^",i ,") +", end=" ")
            archivo.write ("(" + str(pol1[i]) + "x^" + str(i) + ") +")
    for i in range (2,-1,-1):        
        if (i==0):
            print ("(", pol2[i], ")", end=" ")
            archivo.write ("(" + str(pol2[i]) + ")")
        else:
            print ("+ (",pol2[i], "x^",i ,")", end=" ")
            archivo.write ("+ (" + str(pol2[i]) + "x^" + str(i) + ")")
    print(" = ")
    archivo.write ("=")
    for i in range (2,-1,-1):        
        if (i==0):
            print ("(", res[i], ")")
            archivo.write ("(" + str(res[i]) + ")")
        else:
            print ("(",res[i], "x^",i ,") +", end=" ")
            archivo.write ("(" + str(res[i]) + "x^" + str(i) + ") +")


# In[6]:


def captura_matrizA(renglones,columnas,rango): 
    lista=[]
    print("Dame los datos de la primera matriz")
    for r in range(1,renglones+1):
        for c in range(1,columnas+1):
            print("Elemento: [",r,"][",c,"]",end="= ")
            dato=int(input())
            lista.append(dato)
    print("")
    print("| Matriz A |")
    print("")
    for i in range(1,rango+1):
        if (i-1) == 0:
            print("|",end=" ")
        print(lista[i-1],end="   ")
        if (i)%c == 0:
            print("|",end=" ")
            print("")  
            if i!=rango:
                print("|",end=" ")
    print("")
    return lista


# In[7]:


def captura_matrizB(renglones,columnas,rango):
    lista2=[]
    print("Dame los datos de la segunda matriz")
    for r in range(1,renglones+1):
        for c in range(1,columnas+1):
            print("Elemento: [",r,"][",c,"]",end="= ")
            dato=int(input())
            lista2.append(dato)
    print("")
    print("| Matriz B |")
    print("")
    for i in range(1,rango+1):
        if (i-1) == 0:
            print("|",end=" ")
        print(lista2[i-1],end="   ")
        if (i)%c == 0:
            print("|",end=" ")
            print("")  
            if i!=rango:
                print("|",end=" ")
    return lista2  


# In[8]:


#------Realizamos la suma de las dos matrices ingresadas-------#
def sumaM(lista,lista2,rango): 
    listar=[]
    for i in range(0,rango):
        dato=lista[i]+lista2[i]
        listar.append(dato)
    return listar


# In[9]:


def imprimir_mr(listar,renglones,columnas,rango):
    print("")
    print("| Matriz resultante |")
    print("")
    for i in range(1,rango+1):
        if (i-1) == 0:
            print("|",end=" ")
        print(listar[i-1],end="   ")
        if (i)%c == 0:
            print("|",end=" ")
            print("")  
            if i!=rango:
                print("|",end=" ")
    archivo=open("matriz.txt","w")
    for i in range(1,rango+1):
        dato=listar[i-1]
        if (i-1) == 0:
            archivo.write("|")
        archivo.write(" %s "%dato)
        if (i)%columnas == 0:
            archivo.write("|\n")
            if i!=rango:
                archivo.write("|")
    archivo.close()  


# In[10]:


import os
 
def menu():
    """
    Función que limpia la pantalla y muestra nuevamente el menu
    """
    os.system('clear')
    print ("Selecciona una opción")
    print ("\t1 - Operaciones con Números complejos")
    print ("\t2 - Polinomios")
    print ("\t3 - Operaciones con Matrices")
    print ("\t5 - salir")


# In[11]:


while True:
    # Mostramos el menu
    menu()
    # solicituamos una opción al usuario
    opcionMenu = input("inserta un numero valor >> ")
    if opcionMenu=="1":
        print ("")
        input("Has pulsado la opción 1...\npulsa una tecla para continuar")
        archivo = open ('complejos.txt','w')
        suma ()
        producto ()
        potencia ()
        archivo.close ()
    elif opcionMenu=="2":
        print ("")
        input("Has pulsado la opción 2...\npulsa una tecla para continuar")
        pol1=[]
        pol2=[]
        res=[]
        i=0
        j=0
        g=int(input ("grado del polinomio:"))
        captura()
        sumaP()
    elif opcionMenu=="3":
        print ("")
        input("Has pulsado la opción 3...\npulsa una tecla para continuar")
        print("\t\tSuma de matrices de cualquier orden")
        m1=[]
        m2=[]
        mr=[]
        print("Dame el orden la matriz a sumar")
        r=int(input("Numero de renglones: "))
        c=int(input("Numero de columnas: "))
        ran=r*c 
        m1=captura_matrizA(r,c,ran)
        m2=captura_matrizB(r,c,ran)
        mr=sumaM(m1,m2,ran)
        imprimir_mr(mr,r,c,ran)
    elif opcionMenu=="5":
        break
    else:
        print ("")
        input("No has pulsado ninguna opción correcta presta atención de favor compadre :D...\npulsa una tecla para continuar")


# In[ ]:




