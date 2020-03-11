import pyinputplus as pyip
import random, time

prompt = 'Please enter the number of questions:\n'
default = '10'
try:
    number_of_questions = pyip.inputNum(prompt=prompt, default=default, min=1, timeout=8)
except pyip.TimeoutException:
    print('Out of time! Setting number of questions to default value: %d' % (default))

correct_answers = 0

for question_number in range(number_of_questions):
    num_1 = random.randint(0,9)
    num_2 = random.randint(0,9)
    prompt = 'Question %d/%d:\n%d x %d = ' % (question_number+1, number_of_questions, num_1, num_2)
    try:
        pyip.inputStr(prompt=prompt, allowRegexes=['^%d$' % (num_1 * num_2)], 
                        blockRegexes=[('.*', 'Incorrect!')], timeout=8, limit=3)
    except pyip.TimeoutException:
        print('Out of time!')
    except pyip.RetryLimitException:
        print('Out of tries!')
    else:
        print('Correct!')
        correct_answers += 1
    time.sleep(1)
print('Score: %d/%d' % (correct_answers, number_of_questions))