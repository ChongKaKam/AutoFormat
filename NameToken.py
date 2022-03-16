# import module
import re

# function: get names of speakers, and out put a list contain names

def GetNameToken(line):
    # make a regular pattern for name
    NamePattern = re.compile(r'[a-z]+:', re.I)

    # use pattern to match names
    # line = re.sub(r'[a-z]+:', name_upper, line, re.I)
    # print("UP:  ",line)
    ## FirstNamePos = NamePattern.search(line).span()
    rowNameList = NamePattern.findall(line)
    ##NameIter = NamePattern.finditer(line)
    ##for i in NameIter:
    ##    print('>>>',i.group())
    ##    NameList.append(i.group())
    # print('NAMELIST:',NameList)
    # line = re.sub(r' ?[a-z]+: ',set_split,line)
    # erase ":"
    ##for i in range(len(NameList)):
    ##    NameList[i] = (NameList[i])[:-1]

    # remove duplicate names 
    # NameList = list(set(rowNameList))
    for i in range(len(rowNameList)):
        rowNameList[i] = rowNameList[i].capitalize()[:-1]
    NameList = list(set(rowNameList))
    NameList.sort(key=rowNameList.index)
    # print('------NAME-----:',NameList)
    # correct the format of names
    for i in NameList:
        line = line.replace(i.lower()+':', i+':')
    #print("TEST:  ",line)
    for i in range(len(NameList)):
        line = line.replace(NameList[i]+": ","##"+NameList[i]+":"+"##")
    return NameList, line


# TEST
if __name__=="__main__":

    import Format
    # open file and process
    file = open("test.txt","r")
    line = file.readline()
    print("ROW LINE:  ", line)
    line = Format.FormatLine(line)

    print("FORMAT LINE:  ", line)

    NameList, line= GetNameToken(line)
    print("NameList:  ",NameList)
    print("AFTER GET TOKEN:  ",line)

    # show results
    print("Name List: ")

    for i in NameList: print(i)

    file.close()
        
