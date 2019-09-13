package math

import "fmt"

func gcd(a int, b int) (int) {
	for b != 0 {
		remainder := a % b
		a = b
		b = remainder
	}
	return a
}

func main() {
	fmt.Printf("%v\n", gcd(100,1000))
}