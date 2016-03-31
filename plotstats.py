def plotStats(fileName):
    # read in a playlist
    plist = plistlib.readPlist(fileName)
    # get the tracks from playlist
    tracks = plist['Tracks']
    # create lists of song ratings and track durations
    ratings=[]
    durations=[]
    # iterate through the tracks
    for trackID, track in tracks.items():
        try:
            ratings.append(track['Album Rating'])
            durations.append(track['Total Time'])
        except:
            pass

    # ensure that valid data was collected
    if ratings == [] or durations == []:
        print('No valid Album Rating/Total Time data in %s.' % fileName)
        return
        
