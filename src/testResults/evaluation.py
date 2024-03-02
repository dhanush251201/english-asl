import json

def getCounts(input:list)->dict:
    RESULTS ={
        "tokenCount":0,
        "found":0,
        "missing":0,
        "searchFound":0,
        "searchMissing":0,
        "foundPercent":0.0,
        "missingPercent":0.0,
        "searchFoundPercent":0.0,
        "searchMissingPercent":0.0,
        "after":0,
    }

    for i in input:
        RESULTS['tokenCount']=RESULTS["tokenCount"] + i["tokenCount"]
        RESULTS['found'] = RESULTS['found'] + len(i['found'])
        RESULTS['missing'] = RESULTS['missing'] + len(i['missing'])
        RESULTS['searchFound'] = RESULTS['searchFound'] + len(i['SimilarityFound'])
        RESULTS['searchMissing'] = RESULTS['searchMissing'] + len(i['SimilarityMissing'])

    RESULTS["foundPercent"] = str((round(RESULTS['found']/RESULTS["tokenCount"] , 5))*100) + "%"
    RESULTS["missingPercent"] = str((round(RESULTS['missing']/RESULTS["tokenCount"], 5))*100) + "%"
    try:
        RESULTS["searchFoundPercent"] = str((round(RESULTS['searchFound']/RESULTS["missing"], 5))*100) + "%"
    except:
        pass
    try:
        RESULTS["searchMissingPercent"] = str((round(RESULTS['searchMissing']/RESULTS["missing"], 5))*100) + "%"
    except:
        pass
    try:
        RESULTS["after"] = str((round((RESULTS['found'] + RESULTS['searchFound'])/RESULTS["tokenCount"], 5))*100) + "%"
    except:
        pass
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
    resfile.write(json.dumps(RESULTS, indent=2))

if __name__ == '__main__':
    main()
