package math

import "testing"

func TestGCD1(t *testing.T) {
	answer := gcd(100,1000)
	if answer != 100 {
		t.Errorf("The gcd was incorrect, got : %d, want: %d", answer, 100)
	}
}

func TestGCD2(t *testing.T) {
	answer := gcd(50,1000)
	if answer != 50 {
		t.Errorf("The gcd was incorrect, got : %d, want: %d", answer, 50)
	}
}

func TestDouble(t *testing.T) {
	answer := double(5)
	if answer != 10 {
		t.Errorf("The double was incorrect, got : %d, want: %d", answer, 10)
	}
}
