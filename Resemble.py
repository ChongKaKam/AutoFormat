import re

# function:
def check_name( A, B, NameList):
    # print("CHECK_NAME: ",A_name, B)
    for i in range(len(NameList)):
        if A == NameList[i]+':':
            for j in range(len(NameList)):
                if B == NameList[j]+":" :
                    return -1
                else:
                    return i
    return -2

#
def format_punctuation(words):
    if words == '': return words
    if words[-1]==' ':
        words = words[:-1]
    end = words[-1]
    if (end!='?')and(end!='!')and(end!='.'):
        words = words+'.'
    return words

#
def Sentence_Resemble(NameList,line):
    sentence = line.split('_')
    # print("SENTENCE:")
    # print(sentence)

    # Define speaker words set
    Speakers = []
    for i in range(len(NameList)):
        Speakers.append([])
    
    # classify words
    for i in range(1, len(sentence)):
        j = check_name(sentence[i-1], sentence[i], NameList)
        # print("check input:",sentence[i-1], sentence[i], j)
        if (j == -1)or(j == -2): continue
        else:
            temp = format_punctuation(sentence[i])
            Speakers[j].append(temp)
    # print("\n-----\n")
    C_insert = ' '
    speakers_joined = []
    for i in range(len(Speakers)):
        temp = C_insert.join(Speakers[i])
        temp = NameList[i]+': ' + temp
        speakers_joined.append(temp)
    #print("SPEAKERS_JOINED:\n",speakers_joined)
    line_joined = C_insert.join(speakers_joined)
    #print("LINE_JOINED:",line_joined)
    return line_joined


# TEST
if __name__=="__main__":
    
    import Format
    import NameToken

    file = open("test.txt", "r")
    line = file.readline()
    file.close()

    line = Format.FormatLine(line)

    NameList, line = NameToken.GetNameToken(line)
    # print(NameList)
    # print(line)
    line_joined = Sentence_Resemble(NameList, line)

    print('RESULT:\n',line_joined)