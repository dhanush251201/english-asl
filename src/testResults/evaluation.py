import json

def getCounts(input:list)->dict:
    RESULTS ={
        "tokenCount":0,
        "found":0,
        "missing":0,
        "searchFound":0,
        "searchMissing":0,
    }
    for i in input:
        RESULTS['tokenCount']=RESULTS["tokenCount"] + i["tokenCount"]
        RESULTS['found'] = RESULTS['found'] + len(i['found'])
        RESULTS['missing'] = RESULTS['missing'] + len(i['missing'])
        RESULTS['searchFound'] = RESULTS['searchFound'] + len(i['SimilarityFound'])
        RESULTS['searchMissing'] = RESULTS['searchMissing'] + len(i['SimilarityMissing'])

    return RESULTS

def main():
    before = open("resultsbefore.json",'r')
    after = open("resultsafter.json",'r')

    BEFORE = json.load(before)
    AFTER = json.load(after)
    RESBEFORE = getCounts(BEFORE)
    RESAFTER = getCounts(AFTER)
    print("BEFORE : ")
    print(RESBEFORE)
    print("AFTER : ")
    print(RESAFTER)
    RESULTS = {
        "Before Enhancements":RESBEFORE,
        "After Enhancements":RESAFTER
    }
    resfile = open("compiled.json",'w')
    resfile.write(json.dumps(RESULTS, indent=4))

if __name__ == '__main__':
    main()
