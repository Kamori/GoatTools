package main

import (
	"os"
	"os/exec"
	"strconv"
	"testing"
)

func TestTrue(t *testing.T) {
	t.Run("Ensure the RetTrue func returns true", func(t *testing.T) {
		got := RetTrue()
		want := true

		if got != want {
			t.Fatalf("got %q want %q", strconv.FormatBool(got), strconv.FormatBool(want))
		}
	})
}

func TestCommandRun(t *testing.T) {
	t.Run("Ensure the binary main() exits true", func(t *testing.T) {
		if os.Getenv("EXIT_CODE_TESTER") == "1" {
			main()
			return
		}
		cmd := exec.Command(os.Args[0], "-test.run=TestCommandRun")
		cmd.Env = append(os.Environ(), "EXIT_CODE_TESTER=1")
		err := cmd.Run()
		if err == nil {
			return
		}
		t.Fatalf("process ran with err %v, want exit status 0", err)
	})
}
