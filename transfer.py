import Format
import NameToken
import Resemble
import sys

def Transfer_Source(line):
    line = Format.FormatLine(line)
    NameList, line = NameToken.GetNameToken(line)
    line_joined = Resemble.Sentence_Resemble(NameList, line)
    return line_joined

def Transfer_Target(line):
    line = Format.FormatLine_target(line)
    return line

def error_print():
    print('ERROR: there is a unknown type file. Please check it')
    print(' INFO '.center(70,'-'))
    print('the format is: python3 transfer.py [path] [type]')
    print('path: the path of text')
    print('type: s for source; t for target')
    print('you can only type path if the file name is \'xxx.source\' or \'xxx.target\'')
    print('this script can detect it automatically.')

if __name__=="__main__":
    # check argv
    num_argv = len(sys.argv)
    if num_argv < 2:
        error_print()
        sys.exit()
    # get text path
    # cmd: python3 transfer.py [type] [path]
    if num_argv == 2:
        path = sys.argv[1]
        pos = path.rfind('.')
        temp = path[pos+1:]
        if(temp=='source'):
            file_type = 's'
        elif (temp=='target'):
            file_type = 't'
        else:
            file_type = 'UNKNOWN'
            error_print()
            sys.exit()
    if num_argv == 3:
        path = sys.argv[1]
        file_type = sys.argv[2][0]
    print('path:',path)
    print('type:',file_type)
    # set output path
    out_dir = './output/'+ path[path.rfind('/')+1:]
    # file type
    # read lines and close file
    file = open(path,'r')
    lines = file.readlines()
    file.close()
    
    # get lines
    total_line = len(lines)

    # open output file
    out_file = open(out_dir, 'w')
    print(' Welcome '.center(20)+'\n')
    print('the total lines are\n', total_line)
    print('Start transferring...\n')

    if file_type == 's':
        # transfer as source file
        for i in range(total_line):
            line = lines[i]
            out_line = Transfer_Source(line)
            print('Current Process: [{0}/{1}]\n'.format(str(i+1),total_line))
            out_file.write(out_line+"\n")
            out_file.flush()
        print("Done! Please check the output file in: \""+ path +"\"")
    elif file_type == 't':
        # transfer as target file
        for i in range(total_line):
            line = lines[i]
            out_line = Transfer_Target(line)
            print('Current Process: [{0}/{1}]\n'.format(str(i+1),total_line))
            out_file.write(out_line+"\n")
            out_file.flush()
        print("Done! Please check the output file in: \""+ path +"\"")
    else:
        error_print()

    sys.exit()