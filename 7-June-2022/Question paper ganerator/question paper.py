class Question:
    """

    """

 class QuestionPaper(Question):



readFile = str(fileInput.read()).split(',')

numberOfQuestions = int(readFile[0])

sliceQuestion = slice(1,numberOfQuestions*3+1)
questionData = readFile[sliceQuestion]

questionBankE = []
questionBankH = []
questionBankM = []
questions = {}

for i in range(numberOfQuestions):
    questions["Qid"] = questionData[3*i]
    questions["level"] = questionData[3*i+1]
    questions["Qmarks"] = int(questionData[3*i+2])
    if questions["level"]=='easy':
        questionBankE.append(questions.copy())
    if questions["level"]=='hard':
        questionBankH.append(questions.copy())
    if questions["level"]=='medium':
        questionBankM.append(questions.copy())

totalmarks =  int(readFile[numberOfQuestions*3+1])

percentageEasy = int(readFile[numberOfQuestions*3+2].split(" ")[1])
percentageMedium = int(readFile[numberOfQuestions*3+3].split(" ")[1])
percentageHard = int(readFile[numberOfQuestions*3+4].split(" ")[1])

easyMarks = int(percentageeasy/100*totalMarks)
mediumMarks = int(percentageMedium/100*totalMarks)
hardmarks = int(percentageHard/100*totalMarks)

easyQuestions = subsetsum(questionBankE,easyMarks)
mediumQuetions = subsetsum(questionBankM,mediumMarks)
hardQuestions = subsetsum(questionBankH,hardmarks)