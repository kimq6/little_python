# matches:
#   - trigger: ".,alp"
#     replace: "α"
#   - trigger: ".,bet"
#     replace: "β"
#   - trigger: ".,gam"
#     replace: "γ"

# 위의 형태를

# <array>
# 	<dict>
# 		<key>phrase</key>
# 		<string>α</string>
# 		<key>shortcut</key>
# 		<string>.,alp</string>
# 	</dict>
# 	<dict>
# 		<key>phrase</key>
# 		<string>β</string>
# 		<key>shortcut</key>
# 		<string>.,bet</string>
# 	</dict>
# 	<dict>
# 		<key>phrase</key>
# 		<string>γ</string>
# 		<key>shortcut</key>
# 		<string>.,gam</string>
# 	</dict>
# </array>

# 이와같이 바꾸기

# ---

# 입력 데이터
raw_text = """
  - trigger: ".,alp"
    replace: "α"
  - trigger: ".,bet"
    replace: "β"
  - trigger: ".,gam"
    replace: "γ"
  - trigger: ".,del"
    replace: "δ"
  - trigger: ".,eps"
    replace: "ε"
  - trigger: ".,zet"
    replace: "ζ"
  - trigger: ".,eta"
    replace: "η"
  - trigger: ".,the"
    replace: "θ"
  - trigger: ".,iot"
    replace: "ι"
  - trigger: ".,kap"
    replace: "κ"
  - trigger: ".,lam"
    replace: "λ"
  - trigger: ".,mu"
    replace: "μ"
  - trigger: ".,nu"
    replace: "ν"
  - trigger: ".,xi"
    replace: "ξ"
  - trigger: ".,omi"
    replace: "ο"
  - trigger: ".,pi"
    replace: "π"
  - trigger: ".,rho"
    replace: "ρ"
  - trigger: ".,sig"
    replace: "σ"
  - trigger: ".,tau"
    replace: "τ"
  - trigger: ".,ups"
    replace: "υ"
  - trigger: ".,phi"
    replace: "φ"
  - trigger: ".,chi"
    replace: "χ"
  - trigger: ".,psi"
    replace: "ψ"
  - trigger: ".,ome"
    replace: "ω"

  # --- 그리스 대문자 (3글자 버전) ---
  - trigger: ".,Alp"
    replace: "Α"
  - trigger: ".,Bet"
    replace: "Β"
  - trigger: ".,Gam"
    replace: "Γ"
  - trigger: ".,Del"
    replace: "Δ"
  - trigger: ".,Eps"
    replace: "Ε"
  - trigger: ".,Zet"
    replace: "Ζ"
  - trigger: ".,Eta"
    replace: "Η"
  - trigger: ".,The"
    replace: "Θ"
  - trigger: ".,Iot"
    replace: "Ι"
  - trigger: ".,Kap"
    replace: "Κ"
  - trigger: ".,Lam"
    replace: "Λ"
  - trigger: ".,Mu"
    replace: "Μ"
  - trigger: ".,Nu"
    replace: "Ν"
  - trigger: ".,Xi"
    replace: "Ξ"
  - trigger: ".,Omi"
    replace: "Ο"
  - trigger: ".,Pi"
    replace: "Π"
  - trigger: ".,Rho"
    replace: "Ρ"
  - trigger: ".,Sig"
    replace: "Σ"
  - trigger: ".,Tau"
    replace: "Τ"
  - trigger: ".,Ups"
    replace: "Υ"
  - trigger: ".,Phi"
    replace: "Φ"
  - trigger: ".,Chi"
    replace: "Χ"
  - trigger: ".,Psi"
    replace: "Ψ"
  - trigger: ".,Ome"
    replace: "Ω"

  # 화살표
  - trigger: ".,up"
    replace: "↑"
  - trigger: ".,dn"
    replace: "↓"
  - trigger: ".,lt"
    replace: "←"
  - trigger: ".,rt"
    replace: "→"

  # 원형 숫자
  - trigger: ".,0"
    replace: "⓪"
  - trigger: ".,1"
    replace: "①"
  - trigger: ".,2"
    replace: "②"
  - trigger: ".,3"
    replace: "③"
  - trigger: ".,4"
    replace: "④"
  - trigger: ".,5"
    replace: "⑤"
  - trigger: ".,6"
    replace: "⑥"
  - trigger: ".,7"
    replace: "⑦"
  - trigger: ".,8"
    replace: "⑧"
  - trigger: ".,9"
    replace: "⑨"

  # 기본 연산
  - trigger: ".,+-"
    replace: "±"
  - trigger: ".,-+"
    replace: "∓"
  - trigger: ".,**"
    replace: "×"
  - trigger: ".,//"
    replace: "÷"
  - trigger: ".,!="
    replace: "≠"
  - trigger: ".,?="
    replace: "≈"
  - trigger: ".,<="
    replace: "≤"
  - trigger: ".,>="
    replace: "≥"
  - trigger: ".,dot"
    replace: "·"
  - trigger: ".,cdot"  # 내적
    replace: "⋅"

  # 심화 기호
  - trigger: ".,sqrt"
    replace: "√"
  - trigger: ".,nabla"
    replace: "∇"
  - trigger: ".,partial"
    replace: "∂"
  - trigger: ".,hbar"
    replace: "ℏ"
  - trigger: ".,inf"
    replace: "∞"
  - trigger: ".,prop"
    replace: "∝"

  # 논리 및 집합
  - trigger: ".,tf"
    replace: "∴"
  - trigger: ".,bc"
    replace: "∵"
  - trigger: ".,forall"
    replace: "∀"
  - trigger: ".,exists"
    replace: "∃"

  # 단위
  - trigger: ".,degree"
    replace: "°"
  - trigger: ".,ang"
    replace: "Å"
  
  # 일상
  - trigger: ".,star"
    replace: "☆"
  - trigger: ".,Star"
    replace: "★"
  - trigger: ".,circle"
    replace: "○"
  - trigger: ".,Circle"
    replace: "●"
  - trigger: ".,square"
    replace: "□"
  - trigger: ".,Square"
    replace: "■"
  - trigger: ".,heart"
    replace: "♡"
  - trigger: ".,Heart"
    replace: "♥"

  # 삼각형
  - trigger: ".,tu"
    replace: "△"
  - trigger: ".,td"
    replace: "▽"
  - trigger: ".,tl"
    replace: "◁"
  - trigger: ".,tr"
    replace: "▷"
  
  - trigger: ".,Tu"
    replace: "▲"
  - trigger: ".,Td"
    replace: "▼"
  - trigger: ".,Tl"
    replace: "◀"
  - trigger: ".,Tr"
    replace: "▶"

  # 개인정보
  - trigger: ".,tel"
    replace: "58056449"
"""

def convert(text):
    lines = text.strip().split('\n')
    results = []
    current_trigger = ""

    for line in lines:
        line = line.strip()
        
        # trigger 추출
        if 'trigger:' in line:
            # 큰따옴표(") 사이의 내용만 가져옴
            current_trigger = line.split('"')[1]
            
        # replace 추출 및 dict 생성
        elif 'replace:' in line:
            replace_val = line.split('"')[1]
            
            # XML 블록 생성(replace: 를 만난 뒤)
            dict_block = f"""    <dict>
        <key>phrase</key>
        <string>{replace_val}</string>
        <key>shortcut</key>
        <string>{current_trigger}</string>
    </dict>"""
            results.append(dict_block)

    return "\n".join(results)

# 실행 및 출력
print(convert(raw_text))