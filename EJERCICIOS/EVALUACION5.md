# 5 Práctica 5. Operadores relacionales. (6 puntos) 
### 5.1 Ejercicio 1 (2 puntos)
Programa que imprima si el número es positivo o negativo

numero = int(input('ingrese el numero'))
if numero < 0 :
  print('tu numero es negativo')
else :
    print('tu numero es positivo')

### 5.2 Ejercicio 2 (2 puntos)
Programa que imprima si el número ingresado esta en el rango de 1 a 7

numero = int(input('ingrese el numero'))
if numero == (1,2,3,4,5,6,7) :
  print('tu numero es incorrecto')
else:
  print('numero correcto')


### 5.3 Ejercicio 3 (2 puntos)
Programa si el interés es mayor al 30%, sino informa el importe total:

interes = int(input('ingrese el interes'))
numero= int(input('ingrese el numero'))
iva = numero / interes
total = numero + iva
if interes >= 30 :
  print('tu iba es alto y es de ', total)
else:
  print('tu iva es bajo  y es de ', total)
