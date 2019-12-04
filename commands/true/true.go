package main

import (
	"os"
	"strings"
)

// RetTrue returns True
func RetTrue() bool {
	return true
}

// RetFalse returns False
func RetFalse() bool {
	return false
}

func exitTrue() {
	if RetTrue() == true {
		os.Exit(0)
	} else {
		os.Exit(1)
	}
}

func exitFalse() {
	if RetFalse() == false {
		os.Exit(1)
	} else {
		os.Exit(2)
	}
}

func main() {
	cmd := strings.ToLower(os.Args[0])
	if strings.Contains(cmd, "true") {
		exitTrue()
	} else {
		exitFalse()
	}

}
