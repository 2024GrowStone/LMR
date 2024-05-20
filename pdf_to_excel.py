from dotenv import load_dotenv
import openai
import os
import pandas as pd
import pdfplumber
import requests
import urllib.parse

def download_pdf(url, save_dir):
    #parsed_url = urllib.parse.urlparse(f"https://sugang.inha.ac.kr/STD/SU_65002/{url}")
    #file_name = os.path.basename(parsed_url.path)
    #save_path = os.path.join(save_dir, file_name)
    #response = requests.get(f"https://sugang.inha.ac.kr/STD/SU_65002/{url}")
    base_url = "https://sugang.inha.ac.kr/STD/SU_65002/"
    full_url = f"{base_url}{url}"
    parsed_url = urllib.parse.urlparse(full_url)
    file_name = os.path.basename(parsed_url.path) + ".pdf"  # .pdf 확장자 추가
    save_path = os.path.join(save_dir, file_name)
    

    # save file as pdf
    response = requests.get(full_url)
    """
    save_path는 파일이 저장될 경로
    """
    with open(save_path,'wb') as file:
        file.write(response.content)

    
    return file_name


def pdf_to_excel(path: str) -> None:
    """
    convert pdf to excel

    :param path: file path
    """
    # df = pd.read_excel(f"{os.getcwd()}/{path}")

    file_path = f"{os.getcwd()}/{path}"
    pdf = pdfplumber.open(file_path)

    tables = []
    for page in pdf.pages:
        table = page.extract_table()
        if table:
            tables.extend(table)

    pdf.close()
    
    df = pd.DataFrame(tables[1:], columns=tables[0]) 

    excel_name = path.replace('.pdf', '.xlsx')
    excel_path = f"{os.getcwd()}/{excel_name}"
    df.to_excel("Algorithm07.xlsx")


    return {
        "excel path": excel_path,
    }
