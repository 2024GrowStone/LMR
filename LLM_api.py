from dotenv import load_dotenv
import openai
import os
import pandas as pd
import pdfplumber
import pdf_to_excel as pex



def generate_prompt(df):
    course_dates=df['이수시기'].dropna().tolist()
    course_names=df['교과목명'].dropna().tolist()
    prompt = "이수시기와 교과목명:\n"
    for date, name in zip(course_dates, course_names):
        prompt += f"{date}: {name}\n"
    return prompt


def get_text(prompt) -> str:
    # load api key
    load_dotenv()
    OPENAI_YOUR_KEY = os.getenv("API_KEY")

    openai.api_key = OPENAI_YOUR_KEY

    # set LLM model
    MODEL = "gpt-3.5-turbo"
    INSTRUCTION = """
    
    # 교수님 성함, 과목
    
    # 리뷰 3가지
        수강날짜, 내용 형식
    
    # 리뷰 요약
        좋았던 점(강의력, 학점), 아쉬웠던 점 형식




    위 형식을 기반으로 다음 내용을 작성해줘
    """

    PROMPT = """
    교수: ㅇㅇㅇ, 과목: 객체지향프로그래밍1

    # 23년 1학기 수강자
    힘들긴 했지만 수업 열심히 듣고 복습 열심히 하니까 따라갈 수 있었고 실력도 많이 늘었어요 성적도 노력한 만큼 받은듯
        
    # 22년 1학기 수강자
    제대로 코딩을 공부할 생각이라면 추천, 적은 노력으로 좋은 학점을 얻기 원하면 그다지 추천하지 않음.
    # 23년 1학기 수강자
    학점이 짜심, 처음하는 사람한테는 코딩할때 벽이 느껴질 수 있다.
    잘 하는 사람한테는 좋지만, 처음한다면 매우 비추천
    # 22년 1학기 수강자
    약간 버벅거리시긴 하셔서 가끔 못알아 들을때가 있지만, 꽤 친절하십니다.
    """

    response = openai.ChatCompletion.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": INSTRUCTION},
            {"role": "user", "content": PROMPT}, 
            {"role": "assistant", "content": "Who's there?"},
        ],
        temperature=0,
    )

    return response.choices[0].message["content"]

if __name__=="__main__":
    # prompt=generate_prompt(df)
    pex.download_pdf("LecPlan_Rpt.aspx?Value=Imq78pbqdXJCErQvQN5jFE80ropkxQbAEsq2w%2f6tbTbGxBrvcZLuLA%3d%3d","/home/simonslave/Projects/LMR/pdf_file")
   
   
    # print(prompt)
    # print(get_text(prompt))