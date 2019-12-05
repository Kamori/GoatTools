package main

import (
	"os"
	"testing"
)

func TestHeadFile(t *testing.T) {
	type args struct {
		filehandle *os.File
		lines      int
	}
	tests := []struct {
		name string
		args args
		want string
	}{
		// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := HeadFile(tt.args.filehandle, tt.args.lines); got != tt.want {
				t.Errorf("HeadFile() = %v, want %v", got, tt.want)
			}
		})
	}
}
