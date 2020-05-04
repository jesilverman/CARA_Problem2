import glob
import concurrent.futures

def get_files():
    return glob.glob('*.kv')

def read_file(fname):
    kv_pairs={}
    with open(fname, "r") as currFile:
        for line in currFile.readlines():
                l=line.split('=')
                key = l[0].strip()
                value = l[1].strip()
                if key not in kv_pairs:
                    kv_pairs[key]=[value]
                else:
                    kv_pairs[key].append(value)
    return kv_pairs
    

def main():
    keyValuePairs={}
   
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        next_file = {executor.submit(read_file, f) for f in get_files()}
        for future in concurrent.futures.as_completed(next_file):
            temp_kv = future.result()
            for key, value in temp_kv.items():
                if key not in keyValuePairs:
                    keyValuePairs[key]=value
                else:
                    keyValuePairs[key].extend(value)
        
    print(keyValuePairs)

if __name__ == "__main__":
    main()

    
###########
# TEstplan
#
# Dictionary looks as expected
# TEst with number of workers and multiple files