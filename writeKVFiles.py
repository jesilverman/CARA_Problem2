#########################################################################
#
# Program to create user specified number of .kv files.
# If user does not specify will create 10,000
#



import argparse
import random


def randomSpaces():
    return " "*random.randrange(5)

def randomKey():
    keyValues=["Key", "Node", "node", "NODE", "Object", "object", "OBJECT_ID", "OBJECT_id", "object_id", "other", "Other"]
    rand = random.randrange(len(keyValues))
    if rand == 0:
        value = "Value"
    elif rand < 3:
        value = str(random.randrange(15))
    elif rand < 8:
        value = str(random.randrange(10000, 200000))
    else:
        value = "UNKNOWN "+ str(random.randrange(200, 3000))

    return keyValues[rand]+randomSpaces()+"="+randomSpaces()+value+"\n"

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--numFiles", type=int, default=10000) 
    args = parser.parse_args()

    for i in range(args.numFiles):
        filename = 'keyValuefile_'+str(i)+'.kv'
        with open(filename, 'w') as f:
            pass
            for j in range(random.randrange(1,15)):
                f.write(randomKey())

if __name__ == "__main__":
    main()



################
# TEst plan:
# checks that correct number of files are produced
# file matches expected format