import json
import sys
import emoji
import re

keylist = {'key1':'summary','key2':'dialogue'}

if __name__ == "__main__":
    json_name = sys.argv[1]
    jsonfile = open(json_name, 'r')
    # print(jsonfile.name)
    filename = jsonfile.name
    json_str = json.load(jsonfile)
    jsonfile.close()

    filename = filename[filename.find('/')+1:filename.rfind('.')]
    # print(filename)
    data_directory = './dataset/'
    filename_source = data_directory+filename+'.source'
    filename_target = data_directory+filename+'.target'
    file_source = open(filename_source, 'w')
    file_target = open(filename_target, 'w')
    total_line = len(json_str)
    for i in range(total_line):
        print('>> current process [{0}/{1}]'.format(i+1,total_line))
        temp_key1 = json_str[i][keylist['key1']]
        temp_key2 = json_str[i][keylist['key2']]
        file_target.write(temp_key1+'\n')
        file_source.write(temp_key2+'\n')
        #print(temp_key1)
        #print(temp_key2)
    print('>> Done! Run Successfully!')
    file_source.close()
    file_target.close()