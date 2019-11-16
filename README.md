# 5-15-Test-Average-And-Grade
 Calculates the individual grades and average for 5 test scores.

## Scope
 Write a program that asks the user to enter five test scores. The program should display a letter grade for each score and the average test score. Write the following functions in the program:
 * **calc_average.** This function should accept five test scores as arguments and return the average of the scores.
 * **determine_grade.** This function should accept a test score as an argument and return a letter grade for the score based on the following grading scale:
        Score        Letter Grade
        -------------------------
        90-100            A
        80-89             B
        70-79             C
        60-69             D
        Below 60          F

## Sample Run
    Enter score 1:  88
    Enter score 2:  75
    Enter score 3:  68
    Enter score 4:  97
    Enter score 5:  99

    score		numeric grade	letter grade
    ----------------------------------------------------
    score 1:	 88.0 		 B
    score 2:	 75.0 		 C
    score 3:	 68.0 		 D
    score 4:	 97.0 		 A
    score 5:	 99.0 		 A
    ----------------------------------------------------
    Average score:	 85.4 		 B

## Pseudocode
### main function
    START
      SET score counter to 0
      WHILE score counter is less than 5
        INPUT a score into a list
        INCREMENT score counter by 1
      ENDWHILE
      CALL calc_average and pass score list as an argument
      SET average score to return value of calc_average
      PRINT table header
        score        numeric grade    letter grade
        ----------------------------------------------------
      FOR each score in the list
        PRINT score index + 1
        PRINT score value
        CALL determine_grade
        PRINT letter grade
      ENDFOR
      PRINT table foot
        ----------------------------------------------------
      PRINT average score
      CALL determine_grade
      PRINT letter grade
    END

### calc_average function
    START
      PASS IN: list of scores
      SET score accumulator to 0
      FOR each item in score list
        INCREMENT score accumulator by score
      ENDFOR
      CALCULATE average by dividing the score accumulator by the number of items in the list
      PASS OUT: average
    END

### determine_grade function
    START
      PASS IN: score
        IF score >= 90 AND <= 100 THEN
          letter grade = A
        ELSE IF score >= 80 AND <= 89 THEN
          letter grade = B
        ELSE IF score >= 70 AND <= 79 THEN
          letter grade = C
        ELSE IF score >=60 AND <= 69 THEN
          letter grade = D
        ELSE
          letter grade = F
        ENDIF
      PASS OUT: letter grade
    END
