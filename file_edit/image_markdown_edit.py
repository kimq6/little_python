import os
import re

def modify_md():
    current_dir = os.path.dirname(os.path.abspath(__file__))  # current_dir: 현재 스크립트 파일이 있는 디렉토리 경로
    count = 0  # 처리된 파일 개수 저장
    for filename in os.listdir(current_dir):  # filename: 현재 디렉토리의 모든 파일명
        full_path = os.path.join(current_dir, filename)  # full_path: 파일의 전체 경로
        if filename.lower().endswith('.md'):  # lower(): 대소문자 무시, .md로 끝나는지 확인
            try:
                with open(full_path, 'r', encoding='utf-8') as file:  # file: 파일 객체 
                    content = file.read()  # content: 파일 내용 전체(str)
                # 파일 내용 찾기
                # content에서 정규식에 맞는 모든 내용 찾기
                search = re.findall(r"(?<=\n)https://i\.pixiv\.re/.*", content)  # search: 찾은 내용(list)
                print(f"imageURL: {search[0]}\t", f"개수: {len(search)}")

                # 파일 내용 수정
                # re.sub(정규식, 문자열 or 함수, 원본 문자열, count=교체 횟수): 찾은 {정규식} 부분을 {문자열}로 교체

                content = re.sub(r"https://i\.pixiv\.re/.*\n?", "", content)  # search된 URL 부분을 삭제

                replace = "\n".join([f"  - {url}" for url in search])
                replace = f"\nimageURL:\n{replace}\n---"
                content = re.sub(r"\n---", replace, content, count=1)  # imageURL에 주소 추가

                content = content.rstrip()  # content의 뒤 공백 제거

                add_html = '\n\n<div style="text-align: center; color: w; letter-spacing: 10px; margin: 20px 0;">•••</div>\n\n'
                content += add_html  # 마지막 부분에 구분선 추가
                
                add_dataview = '```dataviewjs\ndv.array(dv.current().imageURL).forEach(url => dv.el("img", "", {attr:{src: url}}))\n```\n'
                content += add_dataview  # 마지막 부분에 dataviewjs 코드 블록 추가
                
                # 파일에 반영
                with open(full_path, 'w', encoding='utf-8') as file:  # file: 파일 객체
                    file.write(content)
                print(f"성공: {filename}\n")
                count += 1
            except Exception as e:
                print(f"오류: {filename} - {e}\n")

    print(f"\n총 {count}개의 파일 작업을 완료했습니다.")

if __name__ == "__main__":
    modify_md()

    print("\n창을 닫으려면 아무 키나 누르세요...")
    input()
