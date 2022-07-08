## Práctica 2. 6 puntos
2 Práctica 2. Números enteros y reales.

Realiza los ejercicios de acuerdo a las indicaciones

2.1 Ejercicio 1 (1.5 puntos)

Escribir un programa que convierta un valor dado en grados Fahrenheit a grados
Celsius.

valor = int (input('ingrese valor en °F'))
celsius = valor - 32
resultado = celsius / 1.8
print ('tu resultado es ', resultado, ' grados celsius')

2.2 Ejercicio 2 (1.5 puntos)

Da dos dos números, mostrar la suma, resta, división y multiplicación de
ambos.
num1 = int(input('ingresa valor 1'))
num2 = int(input('ingresa valor 2'))

suma = num1 + num2
resta = num1 - num2
multiplicacion= num1 * num2
division = num1 / num2

print('suma ', suma)
print('resta ', resta)
print('multiplicacion', multiplicacion)
print('division ', division )


2.3 Ejercicio 3 (1.5 puntos)

Calcular el perímetro y área de un rectángulo dada su base y su altura.
Respuesta:

altura = int(input('ingrese la altura del rectangulo '))
base = int(input('ingrese la base del rectangulo'))
perimetro = base * 2 + altura * 2
area = base * altura
print('el perimetro es ', perimetro)
print('el area es ', area)


