package main

import (
        "bufio"
        "bytes"
        "flag"
        "fmt"
        "log"
        "os"
)

//make optional http or dotTLDMap
func grepFile(file string, patterns []byte) (int64 map[int]string) {
//pattersMap http, dotTLDmap

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


func createFile(filepath string){
        filePtr, err := os.Create("");
        if err != nil {
                log.Fatal(err);
        }
        defer filePtr.Close(); // close the file
        // We can read from and write to the file
}


func appendToFile(content, filename string){
        file, err := os.OpenFile(filename, os.O_APPEND | os.O_WRONLY, 0644);
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
        //put all cli checks here for less clutter
}

func main() {

        var collectFileExists bool = false
        var toolOutputFileExists bool = false

        var firstFlagArgCorrect bool = false
        var secondFlagArgCorrect bool = false
        var thirdFlagArgCorrect bool = false
	var fourthFlagArgCorrect bool = false
        var firstInputArgCorrect bool = false
        var secondInputArgCorrect bool = false
        var thirdFInputArgCorrect bool = false
        var userArgumentsCorrect bool = false 


        var helpFlag string
        var urltypeFlag string
        var inputFileFlag string
        var outputFileFlag string

	var collectFile string
	var outputFile string
        

	fmt.Printf("\n")
        flag.StringVar(&helpFlag, "-h", "help", "")
        flag.StringVar(&urltypeFlag, "-u", "needsurltype", "Enter a Url type: \"domain\", \"subdomain\", \"noproto\", \"full\"")
        flag.StringVar(&inputFileFlag, "-i", "needsinputfilepath", "")
        flag.StringVar(&outputFileFlag, "-o", "needsoutputfilepath", "")
        flag.Parse()
       
	args := flag.Args()
        argsLen := len(args)


        if argsLen != 6 || argsLen != 7 {
                printAndExit()
        }

        switch os.Args[1] {
        case "-h":
                printAndExit()
        case "-u":
                firstFlagArgCorrect bool= true
        default:
                //Invalid positioning
               printAndExit()
        }
	
	urlTypeValue := 0
	
        switch os.Args[2] {
        case "domain":
		urlTypeValue = 1
        case "subdomain":
		rlTypeValue = 2
        case "noproto":
		urlTypeValue = 3
	case "full":
        	urlTypeValue = 4
        default:
 		//Invalid argument url type
                printAndExit()
        }

	firstInputArgCorrect = true

        switch os.Args[3] {
        case "-i":
                secondFlagArgCorrect bool= true
        default:
                //Invalid positioning
                printAndExit()
        }

        switch os.Args[5] {
        case "-o":
                thirdFlagArgCorrect bool= true

        default:
                //Invalid positioning
               printAndExit()
        }

	


        collectFileExists = checkFileExist(os.Args[4])
        if collectFileExists != true {
        //invalid input file it does not exist
	printAndExit()
        }
	collectFile = os.Args[4]

        toolOutputFileExists = checkFileExist(os.Args[6])
	//Check if append_flag and set 
	if argsLen == 7 {
		switch os.Args[7] {
        		case "-a":
                		fourthFlagArgCorrect bool= true
        		default:
                	//Invalid 7th argument passed
                	printAndExit()
		}

        }

	if (toolOutputFileExists != false && fourthFlagArgCorrect != true) || (toolOutputFileExists == false && fourthFlagArgCorrect == true) { 
        //invalid output file exists, but append flag not parsed
	printAndExit()
        }
	outputFile = os.Args[6]

	userArgumentsCorrect = collectFileExists && firstFlagArgCorrect && secondFlagArgCorrect && thirdFlagArgCorrect
        if userArgumentsCorrect != true {
		//invalid arguments
        }

	
	baseUrlPattern := ""
	
        greppedResultsMap := grepFile(file,baseUrlPattern) 
        mapReadyForIO := selectFormatByUrlType(urlTypeValue, greppedResultsMap)
	if fourthFlagArgCorrect != true {
		createFile(outputFile)
	}
	formattedDataToFile(mapReadyForIO, outputFile)

}


func selectFormatByUrlType(urlTypeSwitch int, urls map[int]string) (result map[int]string) {
        //refactor into 
        //http in bytes
        //common .tld in bytes
	switch urlTypeSwitch {
	case 1:
	 result	= domainFormatting(urls)
	case 2:
	 result	= subdomainFormating(urls)
	case 3:
	 result	= noprotoFormatting(urls)
	case 4:
	 result	= fullFormatting(urls)
	default:
	//invalid urlTypeValue	
	printAndExit()
	}
	return result
}

//      "domain": -> regex [.tld]'/' -> '.'
func domainFormatting(unformatted map[int]string) map[int]string  {
	for i,url := range unformatted {
	
	}
}

//      "subdomain": -> regex [.tld]'/' -> '//'
func subdomainFormating(unformatted map[int]string) map[int]string {
	for i,url := range unformatted {
	
	}

}

//      "noproto": delimiteer '//'
func noprotoFormatting(unformatted map[int]string) map[int]string  {
	for i,url := range unformatted {
	
	}
}

//      "full": raw grep
func fullFormatting(unformatted map[int]string) map[int]string {
	for i,url := range unformatted {
	
	}
}
//Probably better to .wait the file IO on open and append?
func formattedDataToFile(formatted map[int]string, outputFile string) {
	for _,url := range formatted {
		appendToFile(url, outputFile)
	}
}
