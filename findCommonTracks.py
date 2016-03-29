def findCommonTracks(fileNames):
    # a list of sets of track names
    trackNameSets = []
    for fileName in fileNames:
        #create a new sets
        trackNames = set()
        #read in playlist
        plist = plistlib.readPlist(fileName)
