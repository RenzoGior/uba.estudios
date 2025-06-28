package main

import (
	"fmt"
	"modulo1/matematicas"
	mate "modulo2/matematicas"
)

func main() {
	base, altura := 4, 6
	fmt.Println(matematicas.AreaRectangulo(base, altura))

	angulo := 30
	fmt.Println(mate.Cos(float64(angulo))) //la funcion cos de math recibe radianes por eso no da !/5

}
