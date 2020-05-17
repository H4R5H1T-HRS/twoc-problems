#Solution 5
score1 = int(input("Enter the run score by Player 1 in 60 Balls: "))
score2 = int(input("Enter the run score by Player 2 in 60 Balls: "))
score3 = int(input("Enter the run score by Player 3 in 60 Balls: "))
# To calculate the strike rate: SR = (runs/balls)*100 
sr1 = (score1/60)*100
sr2 = (score2/60)*100
sr3 = (score3/60)*100
print ("Strike Rate of Player 1: ",sr1)
print ("Strike Rate of Player 2: ",sr2)
print ("Strike Rate of Player 3: ",sr3)
#Runs score after 60 more Balls
new_score1 = (sr1/100)*60
new_score2 = (sr2/100)*60
new_score3 = (sr3/100)*60
print ("Run score by Player 1 after 60 more Balls : ",new_score1)
print ("Run score by Player 2 after 60 more Balls : ",new_score2)
print ("Run score by Player 3 after 60 more Balls : ",new_score3)
#If they score all there runs only by hitting sixes
print ("No. Six hit by Player 1 : ",score1//6)
print ("No. Six hit by Player 2 : ",score2//6)
print ("No. Six hit by Player 3 : ",score3//6)

