package main

import (
	"os"
	"testing"
)

func TestPwd(t *testing.T) {
	t.Run("Run 2 change dirs and get WorkingDirector", func(t *testing.T) {
		os.Chdir("/tmp")
		got := GetCwd(false)
		want := "/tmp"

		if got != want {
			t.Fatalf("got %q want %q", got, want)
		}

		os.Chdir("/")
		got = GetCwd(false)
		want = "/"

		if got != want {
			t.Fatalf("got %q want %q", got, want)
		}
	})
}

func TestSysmlinkPWD(t *testing.T) {
	t.Run("Generate 2 dirs, one a symlink. Test GetCWD in symlink with both", func(t *testing.T) {
		physicaldir := "/tmp/goattest_physicaldir"
		symlinkdir := "/tmp/goattest_symlinkdir"
		os.Mkdir(physicaldir, 0770)
		os.Symlink(physicaldir, symlinkdir)

		os.Chdir(symlinkdir)
		os.Setenv("PWD", symlinkdir)

		got := GetCwd(false)
		want := symlinkdir
		if got != want {
			t.Fatalf("got %q want symlink dir %q", got, want)
		}

		got2 := GetCwd(true)
		want2 := physicaldir
		if got2 != want2 {
			t.Fatalf("got %q want physical dir  %q", got2, want2)
		}

	})
}
