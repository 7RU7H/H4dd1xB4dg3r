package main

import (
    "bufio"
    "bytes"
    "fmt"
    "log"
    "os"
)


type report struct {

}


type template struct {

}

//important greppable map[int]string of Nikto output
//Either make another tool to parse source code, probably
//or find all the possible unique USEFUL output

func parse_args() (file, pat string) {
    if len(os.Args) < 3 {
        log.Fatal("usage: petergrep <file_name> <pattern>")
    }
    file = os.Args[1]
    pat = os.Args[2]
    return
}

func grepFile(file string, pat []byte) int64 {
    patCount := int64(0)
    artifacts := make(map[int]string)
    f, err := os.Open(file)
    if err != nil {
        log.Fatal(err)
    }
    defer f.Close()
    scanner := bufio.NewScanner(f)
    for scanner.Scan() {
        if bytes.Contains(scanner.Bytes(), pat) {
            patCount++
	    artifacts[patCount] = //
	    builder.Reset()
        }
    }
    if err := scanner.Err(); err != nil {
        fmt.Fprintln(os.Stderr, err)
    }
    return patCount
}

func (directory string)
 
    file, pat := parse_args()
    r.total += grepFile(file, []byte(pat))

//channels!! all the channels




//reportNikto.go is Nitko scan output report compiler
//Takes a directory, parses files to generate a report


//https://stackoverflow.com/questions/26709971/could-this-be-more-efficient-in-go#26716116
func main() {
	fmt.Printf("\n")
	//CLI stuff is very minimal, need a -h for help -o output -i for input
	



}
