#!/usr/bin/env python3

def display_welcome():
    print("The Test Scores program")
    print("Enter 'x' to exit")
    print("")

def get_scores():
    scores = []
    while True:
        score = input("Enter test score: ")
        if score == "x":
            return  scores
        else:
            score = int(score)
            if score >= 0 and score <= 100:
                scores.append(score)
            else:
                print("Test score must be from 0 through 100. " +
                      "Score discarded. Try again.")

def process_scores(scores):
    total_scores = 0
    count = len(scores)
    # calculate total score
    for score in scores:

    average = total_scores / len(scores)

    # # format and display the result
    # print()
    # print("Score total:       ", score_total)
    # print("Number of Scores:  ", count)
    # print("Average Score:     ", average)

def main():
    display_welcome()
    score_total, count = get_scores()
    process_scores(score_total, count)
    print("")
    print("Bye!")

# if started as the main module, call the main function
if __name__ == "__main__":
    main()


