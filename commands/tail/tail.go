package main

import (
	"bufio"
	"flag"
	"fmt"
	"log"
	"os"
)

var (
	lines      = flag.Int("n", 5, "num lines")
	linesqueue = make([]string, *lines, *lines)
)

func handleLine(line string) {
	linesqueue = append(linesqueue[1:], line)

}

func TailFile(filehandle *os.File, maxlines int) []string {
	scanner := bufio.NewScanner(filehandle)

	// Default scanner is line breaks
	for scanner.Scan() {
		handleLine(scanner.Text())
	}
	for _, line := range linesqueue {
		fmt.Println(line)
	}

	return linesqueue

}

func main() {
	if len(os.Args) > 1 {
		for _, file_path := range os.Args[1:] {
			file, err := os.Open(file_path)
			if err != nil {
				log.Fatal(err)
			}
			defer file.Close()
			TailFile(file, *lines)
		}

	} else {
		file := os.Stdin
		TailFile(file, *lines)
	}
}
