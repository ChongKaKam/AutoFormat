# import module
from cgitb import text
import emoji
import re

# function: replace matched string, and output a formatted line
def remove_space(matched):
    # print("MATCH: ",(matched))
    # print(matched.group())
    temp = matched.group()
    # print('temp:'+temp)
    s = temp[0]
    c = temp[-1]
    # print('s:',s)
    if(s=='?')or(s=='!')or(s=='.')or(s==':'):
        c_up = c.upper()
        # print('c_ip',c_up)
        temp = temp.replace(c, c_up)
    # print('TEMP_'+temp)
    return temp

def correct_abbreviation(matched):
    # print(matched.group())
    return matched.group().replace(' ', '')

def link_word(matched):
    return matched.group().replace(' ', '')
def add_space(matched):
    return matched.group()+' '

def FormatLine(line):
    line = emoji.demojize(line)
    line = re.sub(':\S+?', ' ', line)
    line = re.sub(r'[,.?!:] ([a-z]|[A-Z])', remove_space, line)
    # print("Remove space:  ",line)

    line = re.sub('([a-z]|[A-Z])\ \'([a-z]|[A-Z])', correct_abbreviation, line)
    # print("Correct abbreviation:  ",line)

    line = re.sub('([a-z]|[A-Z])\ ([a-z]|(A-Z))\'', link_word, line)
    # print("Link word:  ", line)
    line = line.replace(r'<3','')
    # line = re.sub('<[a-z_]+>',add_space,line)
    line = re.sub('[!?.]',add_space, line)

    line = line.replace(r':)',"")
    line = line.replace(r';-)',"")
    # line = line.replace('  ',"")
    return line

def FormatLine_target(line):
    line = FormatLine(line)
    # line = re.sub('')
    line = line[0].upper() + line[1:]
    return line



# TEST
if __name__=="__main__":
    # open file and read line
    file = open("test.txt", "r")
    line = file.readline()
    # line = file.readline()
    # line = file.readline()
    # line = file.readline()
    print("Row line:  ", line)

    # use FormatLine()
    line = FormatLine(line)
    print("--> FORMATTED LINE:  ", line)

    # close file 
    file.close()