from dotenv import load_dotenv
import openai
import os

def get_text() -> str:
    # load api key
    load_dotenv()
    OPENAI_YOUR_KEY = os.getenv("API_KEY")

    openai.api_key = OPENAI_YOUR_KEY

    # set LLM model
    MODEL = "gpt-3.5-turbo"
    INSTRUCTION = """
    # 과목 정보
    교수: [교수님 성함]
    과목: [과목]
    
    # 리뷰 [숫자]
        [수강날짜]
        [내용]

    # 리뷰 요약
        좋았던 점
        [좋았던 점(강의력, 학점)]
        
        아쉬웠던 점
        [아쉬웠던 점]

    - (조건1) 위 형식에서 [](대괄호)안에 작성된 내용은 변경할 수 있어
    - (조건2) [내용]에서 욕설이 포함되면 해당 문장을 제거해줘 (예: 시발, 지랄, 병신, 애미, 개세끼)
    - 리뷰는 3개 작성해줘
    - 위 형식과 조건들에 맞게 작성해줘
    """

    PROMPT = """
    # 과목 정보
    교수: 한경숙 
    과목: 객체지향프로그래밍1

    # 23년 1학기 수강자
    힘들긴 했지만 수업 열심히 듣고 복습 열심히 하니까 따라갈 수 있었고 실력도 많이 늘었어요 성적도 노력한 만큼 받은듯

    # 22년 1학기 수강자
    제대로 코딩을 공부할 생각이라면 추천, 적은 노력으로 좋은 학점을 얻기 원하면 그다지 추천하지 않음.

    # 23년 1학기 수강자
    학점이 짜심, 처음하는 사람한테는 코딩할때 벽이 느껴질 수 있다.
    잘 하는 사람한테는 좋지만, 처음한다면 매우 비추천 개 시발롬임

    # 22년 1학기 수강자
    약간 버벅거리시긴 하셔서 가끔 못알아 들을때가 있지만, 꽤 친절하십니다.
    """

    response = openai.ChatCompletion.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": INSTRUCTION},
            {"role": "user", "content": PROMPT}, 
        ],
        temperature=0,
    )

    return response.choices[0].message["content"]


if __name__=="__main__":
    print(get_text())
