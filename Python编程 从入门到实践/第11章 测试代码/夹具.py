#夹具可以帮助我们搭建测试环境
#创建夹具，可以编写一个使用装饰器(放在函数定义前面的指令)@pytest.fixture装饰的函数
import pytest
from survey import AnonymousSurvey

@pytest.fixture
def language_survey():
    """一个可供所有测试函数使用的AnnoymousSurvey"""
    question = "What language did you first learn to speak?"
    language_survey = AnonymousSurvey(question)
    return language_survey

def test_store_single_response(language_survey):
    """测试单个答案会被妥善的存储"""
    language_survey.store_response('English')
    assert 'English' in language_survey.responses

def test_store_three_responses(language_survey):
    """测试三个答案会被妥善地存储"""
    responses = ['English', 'Spanish', 'Mandarin']
    for response in responses:
        language_survey.store_response(response)
    
    for response in responses:
        assert response in language_survey.responses