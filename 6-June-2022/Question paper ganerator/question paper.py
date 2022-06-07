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
        