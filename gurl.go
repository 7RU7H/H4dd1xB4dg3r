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


func openFile(){
	filePtr, err := os.Open("./test/creating.txt");
	if err != nil {
		log.Fatal(err);
	}
	defer filePtr.Close(); // close the file
	// We can read from and write to the file
}


func createFile(filepath string){
	filePtr, err := os.Create("");
	if err != nil {
		log.Fatal(err);
	}
	defer filePtr.Close(); // close the file
	// We can read from and write to the file
}


func appendToFile(content string){
	file, err := os.OpenFile("append.txt", os.O_APPEND | os.O_WRONLY, 0644);
  	defer file.Close();
	if err != nil {
		log.Fatal(err);
	}
	file.Write([]byte(content));
}



func checkFileExists(path string) bool {
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

func printAndExit() {
	usage := "\nUsage: gurl.go [options]\n-h\thelp\n-u\tEnter a Url type: \"domain\", \"subdomain\", \"url-noproto\", \"url-full\"\n\t-i\tfilepath to tool output\n-o\toutput filepath\n")
	fmt.Printf("%s", usage)
	flag.PrintDefaults()
        os.Exit(1)

}


func checkArgs() bool {
}

func main() {

        var collectFileExists bool = false
        var toolOutputFileExists bool = false

	var firstFlagArgCorrect bool= false
	var secondFlagArgCorrect bool= false
	var thirdFlagArgCorrect bool= false
	var firstInputArgCorrect bool= false
	var secondInputArgCorrect bool= false
	var thirdFInputArgCorrect bool = false

	var userArgumentsCorrect bool = false 


        var helpFlag string
	var urltypeFlag string
        var inputFileFlag string
        var outputFileFlag string
        fmt.Printf("\n")
        //CLI stuff is very minimal, need a -h for help -o output -i for input

        flag.StringVar(&helpFlag, "-h", "help", "")
	flag.StringVar(&urltypeFlag, "-u", "needsurltype", "Enter a Url type: \"domain\", \"subdomain\", \"url-noproto\", \"url-full\"")
	flag.StringVar(&inputFileFlag, "-i", "needsinputfilepath", "")
        flag.StringVar(&outputFileFlagFlag, "-o", "needsoutputfilepath", "")
        flag.Parse()
        args := flag.Args()
        if len(args) == 0 {
		//Argument length 0
        	printAndExit()
	}

        switch os.Args[1] {
        case "-h":

        case "-u":
		firstArgCorrect bool= true

	case "-i":

        case "-o":

        default:
		//Invalid positioning
                flag.PrintDefaults()
                os.Exit(1)
        }
	switch os.Args[1] {
        case "-h":

        case "-u":
		firstArgCorrect bool= true

	case "-i":

        case "-o":

        default:
		//Invalid positioning
                flag.PrintDefaults()
                os.Exit(1)
        }
        switch os.Args[1] {
        case "-h":

        case "-u":
		firstArgCorrect bool= true

	case "-i":

        case "-o":

        default:
		//Invalid positioning
                flag.PrintDefaults()
                os.Exit(1)
        }


	userArgumentsCorrect = 
	if userArgumentsCorrect != true {
	//invalid arguments 
	}


	collectFileExists = checkFileExist()
	if collectFileExists != true {
		 
	}

	toolOutputFileExists = 
	if toolOutputFileExists != true { 
	//invalid input file path  provided
i	}	
}




