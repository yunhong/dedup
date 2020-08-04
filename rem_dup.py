
# given a list of documents, remove redudant ones
# if two files have the same filename, then delete one of them

target_dir_default = '/Users/yunhongz/Google Drive/'
target_dir_more = '/Users/yunhongz/Downloads/'

target_dir_list = [target_dir_default, target_dir_more]


#list_fn = 'list_filename.txt'

def is_dup(fn_full): 

    tokens = fn_full.split('.')
    if(len(tokens) < 2): return False

    fn_str_before_type = tokens[-2] # document type is the last token
    file_name = fn_str_before_type

    if(len(file_name) == 0): 
        return False

    if(file_name[-1] != ')'): # end with (n)
        return False

    # walk from the end backward, if it is a number, continue; if it is '(', return true
    index = len(file_name) - 2
    while(index >= 0): 
        c = file_name[index]
        if(c >= '0') and (c <= '9'): 
            index -= 1
            continue
        elif(c == '('): 
            if(index < len(file_name) - 2): 
                return True
            else: 
                return False
        else: 
            return False
    # end while
    return False
# end judge whether a file is redundant
    
import os

def remove_file(fn_full): 
    if(is_dup(fn_full)): 
        print('duplicate: ' + fn_full)
        

        fn_with_path = target_dir + fn_full
        
        if os.path.exists(fn_with_path):
            os.remove(fn_with_path)
            print('deleted: ' + fn_with_path)
        else:
            print('file doesn\'t exist: ' + fn_with_path)
# end remove_file

#fp = open(list_fn)
                  
def rem_dup_dir(target_dir = None): 
    files = []
    # r=root, d=directories, f = files
    if(target_dir == None): 
        target_dir = target_dir_default

    for r, d, f in os.walk(target_dir):
        for file in f:
            files.append(os.path.join(r, file))
    # end for
            
    for file in files:
        if(is_dup(file)): #print(file)
            os.remove(file)
            print('dup file removed: ' + file)
    # end for
# end def

import sys
def main():
    arg_len = len(sys.argv)
    print('argv: ' + str(sys.argv))
    if(arg_len == 1): 
        for target_dir in target_dir_list:
            rem_dup_dir(target_dir)
    else:
        target_dir = sys.argv[1]
        rem_dup_dir(target_dir)

if __name__ == '__main__':
    main()

