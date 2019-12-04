package main

import (
	"flag"
	"fmt"
	"log"
	"os"
	"path/filepath"
)

// Stolen from https://stackoverflow.com/a/54747682/3105129
func isFlagPassed(name string) bool {
	found := false
	flag.Visit(func(f *flag.Flag) {
		if f.Name == name {
			found = true
		}
	})
	return found
}

func GetCwd(resolveSymbolicLinks bool) string {
	dir, err := os.Getwd()
	if err != nil {
		log.Fatal(err)
	}

	if resolveSymbolicLinks {
		dir, err = filepath.EvalSymlinks(dir)
		if err != nil {
			log.Fatal(err)
		}
	}
	return dir
}

func main() {
	flag.Bool("L", true, "Print current working directory (default)s")
	resolvesymlink := flag.Bool("P", false, "Print current working directory but resolve symlinks")

	flag.Parse()

	// To mimic the GNU/pwd if -L is passed then only get logical path
	if isFlagPassed("L") {
		*resolvesymlink = false
	}

	fmt.Println(GetCwd(*resolvesymlink))
}
