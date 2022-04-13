package main

import (
	"bufio"
	"bytes"
	"fmt"
	"log"
	"os"
)

//important greppable map[int]string of Nikto output
//Either make another tool to parse source code, probably
//or find all the possible unique USEFUL output

//channels!! all the channels

func grepFile(file string, patterns []byte) (int64 map[int]string) {
	patCount := int64(0)
	artifacts := make(map[int]string)
	builder := strings.Builder{}
	f, err := os.Open(file)
	if err != nil {
		log.Fatal(err)
	}
	defer f.Close()
	scanner := bufio.NewScanner(f)
	for scanner.Scan() {
		for i := 0; i <= len(patterns)-1; i++ {
			if bytes.Contains(scanner.Bytes(), patterns[i]) {
				patCount++
				builder.WriteString("Scan " + file + " contains " + string(patterns[i]))
				artifacts[patCount] = builder.String()
				builder.Reset()
			}
		}
	}
	if err := scanner.Err(); err != nil {
		fmt.Fprintln(os.Stderr, err)
	}
	return patCount, artifacts
}

func buildDatabase() []byte {
	readFile, err := os.Open("output.txt")
	if err != nil {
		log.Fatal(err)
	}
	fileScanner := bufio.NewScanner(readFile)
	fileScanner.Split(bufio.ScanLines)
	data := []byte{}
	for fileScanner.Scan() {
		data = append(data, fileScanner.Byte())
	}
	readFile.Close()
	return data
}

//reportNikto.go is Nitko scan output report compiler
//Takes a directory, parses files to generate a report

//https://stackoverflow.com/questions/26709971/could-this-be-more-efficient-in-go#26716116
func main() {
	var multifileBool bool = false
	fmt.Printf("\n")
	//CLI stuff is very minimal, need a -h for help -o output -i for input

	db := buildDatabase()
}
