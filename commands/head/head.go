package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
)

func HeadFile(filehandle *os.File, maxlines int) string {
	scanner := bufio.NewScanner(filehandle)
	lines := 0

	// Default scanner is line breaks
	for scanner.Scan() {
		fmt.Println(scanner.Text())
		lines++
		if lines >= maxlines {
			break
		}
	}
	return "Done"

}

func main() {
	if len(os.Args) > 1 {
		for _, file_path := range os.Args[1:] {
			file, err := os.Open(file_path)
			if err != nil {
				log.Fatal(err)
			}
			defer file.Close()
			HeadFile(file, 5)
		}

	} else {
		file := os.Stdin
		HeadFile(file, 5)
	}
}
