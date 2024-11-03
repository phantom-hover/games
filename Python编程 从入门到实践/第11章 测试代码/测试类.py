#各种断言:若该条件成立，则假设得到确认即无误，若实际上并不满足，则测试不能通过
"""
assert a == b  断言两个值相等
assert a != b  断言两个值不等
assert a       断言a的布尔求值为True
assert not a   断言a的布尔求值为False
assert element in list 断言元素在列表中
assert element not in list 断言元素不在列表中
"""

#编写一个survey程序
from survey import AnonymousSurvey

#定义一个问题,并创建一个表示调查的AnonymousSurvey对象
question = "What language did you first learn to speak?"
language_survey = AnonymousSurvey(question)

#显示问题并存储答案
language_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    language_survey.store_response(response)

#显示调查结果
print("\nThank you to everyone who participated in the survey!")
language_survey.show_results()

#测试AnonymousSurvey类:验证如果用户在面对调查问题时只提供一个答案，这个答案也能妥善地存储
def test_store_single_response():
    """测试单个答案会被妥善地存储"""
    question = "What language did you first learn to speak?"
    language_survey = AnonymousSurvey(question)
    language_survey.store_response('English')
    assert 'English' in language_survey.responses