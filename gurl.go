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
	//put all cli checks here for less clutter
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
	flag.StringVar(&urltypeFlag, "-u", "needsurltype", "Enter a Url type: \"domain\", \"subdomain\", \"noproto\", \"full\"")
	flag.StringVar(&inputFileFlag, "-i", "needsinputfilepath", "")
        flag.StringVar(&outputFileFlag, "-o", "needsoutputfilepath", "")
        flag.Parse()
        args := flag.Args()
	argsLen := len(args)
        if argsLen != 6 {
		//Argument length != 6
        	printAndExit()
	}

        switch os.Args[1] {
        case "-h":
		printAndExit()
        case "-u":
		firstArgCorrect bool= true
        default:
		//Invalid positioning
               printAndExit()
        }
	switch os.Args[3] {
	case "-i":
		secondArgCorrect bool= true
        default:
		//Invalid positioning
                printAndExit()
        }
        switch os.Args[5] {
        case "-o":
		thirdArgCorrect bool= true

        default:
		//Invalid positioning
               printAndExit()
        }

	//
	switch  {
        case "domain":

        case "subdomain":

	case "noproto":

        case "full":
	default:
		printAndExit()
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
	}	



	greppedResultsMap := grepFile(file,//pattern) 
	selectByUrlType( ,greppedResultsMap)

}


func selectByUrlType(urlTypeSwitch int, urls map[int]string) {
	//refactor into 
	//http in bytes
	//common .tld in bytes
	
//	"domain": -> regex [.tld]'/' -> '.'
//	"subdomain": -> regex [.tld]'/' -> '//'
//	"noproto": delimiteer '//'
//	"full": raw grep


//TODO refactor out
//
//edit map

//write into file

switch urlTypeSwitch
case 0:
case 1:
case 2:
case 3:
	domainFormatting

	subdomainFormating
	noprotoFormatting
	fullFormatting
default:	
	
	

}

