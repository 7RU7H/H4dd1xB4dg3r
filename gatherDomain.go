package main

import (
	"fmt"
	"os/exec"
)



func runTool(tool, args string) {
	cmd := exec.Command(tool, args)
	stdout, err := cmd.Output()
	if err != nil {
		fmt.Println(err.Error())
		return
	}
}

func main() {
	amass := "amass"
	args := 
}

