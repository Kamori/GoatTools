// Purpose
// To mimic the GNU/cat utility for printing file contents

// Lessons learned
// * Defining a variable in an if statement doesn't allow the variable to act "defined" when compiled.
// -- We can get around that by defining the variable and type ahead of time... and/or move the variable
// -- usage to a function
// * All individual tools must have a "package main" Note: Having multiple mains per dir is bad practice +

// TODO: implement GNU/cat flags
// TODO: Change file structure to be more Go best practice, python can reasonably adopt that structure as well
// -- See: +
// -- An idea for a golang-refined method could be statically combine all tools into a single package.
// -- Think Busybox

package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
)

func print_data(file *os.File) {
	scanner := bufio.NewScanner(file)

	for scanner.Scan() {
		fmt.Println(scanner.Text())
	}

}

func main() {
	if len(os.Args) > 1 {
		for _, file_path := range os.Args[1:] {
			file, err := os.Open(file_path)
			if err != nil {
				log.Fatal(err)
			}
			defer file.Close()
			print_data(file)
		}

	} else {
		file := os.Stdin
		print_data(file)
	}

}
