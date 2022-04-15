package main

import (
	"bufio"
	"bytes"
	"flag"
	"fmt"
	"log"
	"os"
)

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

func checkExists(path string) bool {
	_, err := os.Stat(path)
	if err == nil {
		log.Fatal(err)
		return false
	}
	if os.IsNotExist(err) {
		log.Fatal("Not Exists")
		return false
	}
	return true
}

func isDirectory(path string) (bool, error) {
	fileInfo, err := os.Stat(path)
	if err != nil {
		return false, err
	}

	return fileInfo.IsDir(), err
}

//reportNikto.go is Nitko scan output report compiler
//Takes a directory, parses files to generate a report
//https:stackoverflow.com/questions/26709971/could-this-be-more-efficient-in-go#26716116

func checkArgs() bool

func main() {
	var directoryBool bool = false
	var helpFlag string
	var outputFlag string
	var inputFlag string
	fmt.Printf("\n")
	//CLI stuff is very minimal, need a -h for help -o output -i for input

	flag.StringVar(&helpFlag, "-h", "help", "")
	flag.StringVar(&outputFlag, "-i", "needsinput", "Enter a directory or filename")
	flag.StringVar(&inputFlag, "-o", "needsoutput", "")
	flag.Parse()
	args := flag.Args()
	if len(args) == 0 {
		fmt.Printf("\nUsage: niktoReport.go [options]\n-h\thelp\n-i\tfilename or directory\n-o\toutput filename, if no path provided output willl be current working directory\n")
		flag.PrintDefaults()
		os.Exit(1)
	}

	switch os.Args[1] {
	case "-h":
		fmt.Printf("\n-i input file or directory\n -o output filename\n")
	case "-i":

	case "-o":

	default:
		flag.PrintDefaults()
		os.Exit(1)
	}
	db := buildDatabase()
	if checkExists() != true {
		fmt.Printf("\nProvided file or directory does not exist\n")
		flag.PrintDefaults()
		os.Exit(1)
	}
	directoryBool, err = isDirectory() 

	//
}

