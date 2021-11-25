def sortDict(dictionary):
    # Obtain the tuples by sorting the dictionary in decrescent order.
    sortedTuples = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)

    # Get only the first value of every tuple. This value equals the player. Return the final result.
    result = [tup[0] for tup in sortedTuples]
    return result

def getOtherInfoFromList(matches, matchesLen):
    # Initialize both as dictionary.
    rankings, sums = {}, {}

    # Iterate every play. 
    for i in range(matchesLen):
        # Set the total win in the ranking as 0 for the current play.
        rankings[i] = 0

        # Remove useless whitespace and tab.
        matches[i] = matches[i].replace(" ", "").replace("\t", "")

        sums[i] = sum(ord(elt) for elt in matches[i])
    
    # Return everything.
    return rankings, matches, sums

def convertPointsToRanks(rankings, i, j, pointsI, pointsJ, sumsA, sumsB, strA, strB):
    # Set both plays at 0 wins.
    winA, winB = 0, 0
    # First check if who scored more points, and assign a win based on this.
    if(pointsI > pointsJ):
        winA += 1
    elif(pointsI < pointsJ): 
        winB += 1
        # If tie continue checking with other rules.
    elif(pointsI == pointsJ):
        # Check who has the greates sum of characters, and assign a win based on this.
        if(sumsA < sumsB):
            winA += 1
        elif(sumsA > sumsB):
            winB += 1
            # If a tie again continue checking with other rules.
        elif(sumsA == sumsB):
            # Check who comes first in lexicographic order, and assign a win based on this.
            if(strA < strB):
                winA += 1
            elif(strA > strB):
                winB += 1

    # Add the win to the temporary rankings and return it.
    rankings[i] += winA
    rankings[j] += winB
    return rankings

def execute(k, strA, strB, pointsI, pointsJ):
    # Check character by character.
    for char in range(len(strA)):
        # Obtain the UTF-8 value of the character
        charA, charB = ord(strA[char]), ord(strB[char])
        # Calculate the difference
        difference = charA - charB
        # Get the absolute value. Since I can't use Math.abs I made it my self. Don't check if it's already > 0 because it's useless in this case.
        if(difference < 0):
            difference = difference * -1

        # Assign the points based on the rules of the game.
        if difference != 0:
            if difference <= k:
                if charA > charB:
                    pointsI += 1
                else:
                    pointsJ += 1
            else:
                if charA < charB:
                    pointsI += 1
                else:
                    pointsJ += 1
    
    # Return the match result.
    return pointsI, pointsJ

def ex(matches, k):
    # Retrieve the number of plays.
    newMatches = matches.copy()
    matchesLen = len(newMatches)
    # Initialize the rankings, fix the plays removing withespace and \t.
    rankings, newMatches, sums = getOtherInfoFromList(newMatches, matchesLen)

    # Iterate in every play and execute a match against all other plays.
    for i in range(matchesLen):
        for j in range(i + 1, matchesLen):
            # Execute the match.
            pointsI, pointsJ = execute(k, newMatches[i], newMatches[j], 0, 0)
            # Converts the points of the match in some temporary rankings.
            rankings = convertPointsToRanks(rankings,  i, j, pointsI, pointsJ, sums[i], sums[j], newMatches[i], newMatches[j])
    
    # Sort the rankings by the total win and return it.
    return sortDict(rankings)

if __name__ == "__main__":
    pass
