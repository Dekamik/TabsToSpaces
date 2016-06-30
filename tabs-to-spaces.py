import sys


def convert_tabs(lines, tab_size):
    new_lines = list()
    
    # Create space tab
    i = 0
    tab = ""
    while i < tab_size:
        tab += " "
        i += 1
    # Replace all tabs
    for line in lines:
        new_lines.append(line.replace("\t", tab))
        
    return new_lines

def main():
    usage = "Usage: " + sys.argv[0] + " [-o] file_to_comment\n" \
            "\n" \
            "       -o:     Redirect output to stdout\n" \
            " --size=n:     No of spaces in a tab (default=4)"
    
    redirect_to_stdout = False
    size = 4
    
    # Minimum arguments = 1 (The file)
    if len(sys.argv) < 2:
        print("ERROR: No arguments provided\n")
        print(usage)
        exit(1)
    
    # Check arguments
    for arg in sys.argv:
        if arg == "-o":
            redirect_to_stdout = True
        elif "--size=" in arg:
            size = int(arg[arg.index("="):])
        elif arg == "-h" or arg == "--help":
            print(usage)
            exit(0)
    
    try:
        # Input
        with open(sys.argv[-1], "r") as fo:
            lines = fo.read().splitlines()
        
        # Action
        lines = "\n".join(convert_tabs(lines, size))
        
        # Output
        if redirect_to_stdout:
            sys.stdout.write(lines)
        else:
            with open(sys.argv[-1], "w") as fo:
                fo.writelines(lines)
    except FileNotFoundError:
        print("ERROR: \"" + sys.argv[-1] + "\" not found\n")
        print(usage)
        exit(1)

main()
