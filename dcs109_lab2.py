################################################################################
# Yuhao Zhao
# DCS 109
# Lab 2: Toward Ranked Choice Voting
################################################################################
# YOUR SOLUTIONS GO HERE
import math
import random

def declareWinner(name:str, name_vote_for:int, name_votes_total:int):
    '''
    function should print (not return) a message indicating the candidate by name
    and that the candidate won with an appropriatelycomputed percentage of the
    votes based on num_votes_for and num_votes_total

    Parameters:
       name: a string describing the candidate name
       name_vote_for: an integer of votes for specific candidate
       name_votes_total: an integer of votes for all candidates

    Returns:
       None

    '''


    win_percent=(name_vote_for/name_votes_total)*100
    print(f"candidate {name} wins with {win_percent:.3f}% of the vote")


################################################################################
def findCandidateIndex(candidate:"list[str]", which_candidate:str)-> "int | None":
    '''
    The function find which candidate within the candidates list and return the
    corresponding index where they are found. Return the special value None if not found.

    Parameters:
       candidate: a list of strings contained all candidates' names
       which_candidate: a string indicates the specific name of a candidate

    Returns:
       the corresponding index of specific candidate or None if not found


    '''

    for index in range(len(candidate)):
        if candidate[index]==which_candidate:
            return index


################################################################################
def countTheVotes(candidate:"list[str]", votes:"list[str]")-> "list[int]":
    '''
    The function should create a new list of vote counts for each candidate (all initialized to zero).

    The function should then count the number of votes for each candidate,
    keeping track of the vote count for each candidate within that new list.

    Parameters:
       candidate: a list of strings corresponding to the unique possible candidates
       votes: a list of strings corresponding to cast votes, one vote per voter

    Returns:
        a list of length len(candidates) containing the number of votes cast for each
        corresponding candidate

    '''
    counting=[]
    for i in range(len(candidate)):
        counting.append(0)

    for k in range(len(candidate)):
        for j in range(len(votes)):
            if candidate[k]==votes[j]:
                counting[findCandidateIndex(candidate, candidate[k])]+=1
    return counting

################################################################################
def areALLEqual(vote_counts:"list[int]")-> bool:
    '''
    This function should return True if all of the entries in the list
    are exactly the same value, False otherwise.

    Parameter:
       vote_counts: a list of integers return the votes count of each candidate

    Return:
       a boolean value indicates whether the votes of candidates are all equal or not

    '''
    int_1=vote_counts[0]
    check = True
    for i in vote_counts:
        if i!=int_1:
            check = False
    if check == True:
        return True
    else:
        return False

################################################################################
def findSimpleMajorityWinner(vote_counts:"list[int]")-> " int | None ":
    '''
    This function should first determine whether the given list of vote counts contains all the same value
    (call the helper function you wrote and tested above) —
    if so, choose a winner (index) at random and return that winner.
    If no winner is being chosen at random, your function must instead
    return the index of the candidate having more than 50% of the total vote
    (note: strictly greater than 50%), or None if there is no such winner.

    Parameter:
       vote_counts: a list of integers return the votes count of each candidate

    Returns:
       the index of winner or None

    '''
    first=areALLEqual(vote_counts)
    print(first)

    if first==True:

        return random.randint(0, len(vote_counts)-1)
    elif first==False:
        sum=0
        for i in range(len(vote_counts)):
            sum= sum+ vote_counts[i]


        for i in range(len(vote_counts)):
            if (vote_counts[i]/sum)>0.5 or (vote_counts[i]/sum)==0.5:
                return findCandidateIndex(vote_counts, vote_counts[i])
    else:
        return None

################################################################################
def runElection(candidates: list[str], votes:list[str], debug: bool = True)-> None:
    '''
    function must:
    • count the votes for each candidate (just use your helper function from above); then
    • if your debug parameter is True, use an f-string approach to print the list of candidates and the corresponding
      vote counts that you just computed; then
    • find the winner of a simple majority vote (just use your helper function from above); then
    • if there was a winner, declare that winner (again, use your helper function from above) or, if no winner, just
      print a message indicating that there was no simple-majority winner.

    Parameters:
      candidates: a list of strings contained the candidates' name
      votes: a list of integers return the votes count of each candidate
      debug: boolean value default is true

    Return:
      None

    '''
    vote_counts_list= countTheVotes(candidates, votes)
    print(f"the list of candidates: {candidates} and the corresponding vote counts: {vote_counts_list}")
    sum=0
    for i in vote_counts_list:
        sum= sum+i
    winner= findSimpleMajorityWinner(vote_counts_list)
    if winner!= None:
        declareWinner(candidates[winner], vote_counts_list[winner], sum)
    else:
        print("there was no simple majority winner !")



################################################################################
def printTest(fcn_call: str, result: int, expected: int) -> None:
	''' This function prints a full description of a given test of a function
		call.
	Parameters:
		fcn_call: a string describing the function call being made
		result:   the integer result of the actual function call
		expected: the integer result expected, which should match result
	Returns:
		None -- just prints
	'''
	print(f"Testing {fcn_call}:")
	print(f"   Result:   {repr(result)}")  # repr() will cause quotes to appear if str
	print(f"   Expected: {expected}")





################################################################################
def main():
    # INCLUDE YOUR TESTS HERE

    #################################################################
    # Test for declareWinner
    declareWinner('Barry', 70, 100)
    declareWinner('Carrie', 1390, 2300)
    declareWinner('Anelise', 209, 230)
    declareWinner('lilo', 10, 15)
    #################################################################

    a = 'Anelise'; b = 'Barry'; c = 'Carrie'
    candidates = [a, b, c]
    # Test for findCandidateIndex
    result= findCandidateIndex(candidates, 'Anelise')
    expected=0
    printTest("findCandidateIndex(candidates, 'Anelise')", result, expected)

    result= findCandidateIndex(candidates, 'Carrie')
    expected=2
    printTest("findCandidateIndex(candidates, 'Carrie')", result, expected)

    result= findCandidateIndex(candidates, 'Frankie')
    expected= None
    printTest("findCandidateIndex(candidates, 'Frankie')", result, expected)
    #################################################################
    #Test for countTheVotes
    votes1 = [a, a, a, a, a, a, a, b, c, c, c, c]
    result1 = countTheVotes(candidates, votes1)
    expected=[7, 1, 4]
    printTest("countTheVotes(candidates, votes1)", result1, expected)

    votes2 = [a, a, a, a, b, b, b, b, c, c, c, c]
    result2 = countTheVotes(candidates, votes2)
    expected = [4, 4, 4]
    printTest("countTheVotes(candidates, votes2)", result2, expected)
    votes3 = [a, a, a, a, a]
    result3 = countTheVotes(candidates, votes3)
    expected = [5, 0, 0]
    printTest("countTheVotes(candidates, votes3)", result3, expected)
    #################################################################
    #Test for areALLEqual
    result = areALLEqual(result1)
    expected = False
    printTest("areALLEqual(votes1)", result, expected)

    result = areALLEqual(result2)
    expected = True
    printTest("areALLEqual(votes2)", result, expected)

    result = areALLEqual(result3)
    expected = False
    printTest("areALLEqual(votes3)", result, expected)
    #################################################################
    #Test for findSimpleMajorityWinner
    result = findSimpleMajorityWinner(result1)
    expected = 0
    printTest("findSimpleMajorityWinner(result1)", result, expected)

    random.seed(8675309)
    result = findSimpleMajorityWinner(result2)
    expected = 1
    printTest("findSimpleMajorityWinner(result2)", result, expected)

    result = findSimpleMajorityWinner(result3)
    expected = 0
    printTest("findSimpleMajorityWinner(result3)", result, expected)

    #################################################################
    # Test for runElection
    # TESTS FOR CLEAR WINNER

    votes = [a, a, b, b, a, a, a, c, c]
    runElection(candidates, votes)


    #My test
    votes_again = [a, a, a, a, a, a, b, b, c, c, c,]
    runElection(candidates, votes_again)

    votes_another_one = [a, a, b, b, b, b, b, b, b, c]
    runElection(candidates, votes_another_one)

    votes_a_third_one = [a, a, b, b, b, c, c, c, c, c, c, c]
    runElection(candidates, votes_a_third_one)

    #################################################################
    # TESTS FOR TIE ACROSS THE BOARD -- WINNER CHOSEN AT RANDOM
    #
    # seed chosen to have Anelise win at random
    random.seed(5551212)
    votes = [a, a, b, b, c, c]
    runElection(candidates, votes)


    # seed chosen to have Barry win at random
    random.seed(8675309)
    votes = [a, a, b, b, c, c]
    runElection(candidates, votes)


    # seed chosen to have Carrie win at random
    random.seed(2121212)
    votes = [a, a, b, b, c, c]
    runElection(candidates, votes)

    #My test
    # seed chosen to have Carrie win at random
    random.seed(3333333)
    votes_e1 = [a, a, a, a, a, b, b, b, b, b, c, c, c, c, c]
    runElection(candidates, votes_e1)

    # seed chosen to have Carrie win at random
    random.seed(3232323232)
    vote_e2 = [a, a, a, a, a, a, b, b, b, b, b, b, c, c, c, c, c, c]
    runElection(candidates, vote_e2)

    # seed chosen to have Carrie  win at RANDOM
    random.seed(55555555)
    vote_e3 = [a, a, a, a, b, b, b, b, c, c, c, c]
    runElection(candidates, vote_e3)
    #################################################################
    # TESTS FOR NO WINNER ON THIS ROUND OF VOTING
    #
    votes = [a, a, b, b, c, c, a]
    runElection(candidates, votes)

    #My test
    votes_no1 =[a, a, a, b, b, b, c, c, c, c]
    runElection(candidates, votes_no1)

    votes_no2 = [a, a, a, a, a, a, b, b, b, b, b, b, c, c, c, c ,c ,c, c, c]
    runElection(candidates, votes_no2)

    votes_no3 = [a, a, a, a, a, a, a, a, a, a, a, a, b, b, b, b, b, b, b, c, c, c, c, c, c, c]
    runElection(candidates, votes_no3)






main()
