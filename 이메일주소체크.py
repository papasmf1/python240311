import re

# 정규표현식 패턴
email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
# 이메일 주소의 패턴은 사용자이름@도메인이름.확장자와 같은 형태입니다.
# 사용자 이름은 영문자(대소문자), 숫자, 특수문자('_','%','+','-','.')를 포함할 수 있습니다.
# 도메인 이름은 이메일 서비스를 제공하는 서버의 주소를 나타내며 영문자(대소문자)와 숫자로 구성됩니다.
# 확장자는 이메일 서비스의 종류를 나타냅니다. 일반적으로 두 글자로 이루어져 있습니다.

# 이메일 주소를 체크하는 함수
def check_email(email):
    if re.search(email_pattern, email):
        return True
    else:
        return False

# 샘플 데이터 생성
sample_emails = [
    "user@example.com",
    "user123@gmail.com",
    "user.name@example.co.kr",
    "info@company.org",
    "john.doe123@sub.domain.net",
    "invalid-email",
    "invalid-email@",
    "@invalid.com",
    "user@invalid.",
    "user123@.com"
]

# 샘플 데이터를 이메일 주소 형식에 맞게 출력
for email in sample_emails:
    if check_email(email):
        print(f"{email}: 유효한 이메일 주소입니다.")
    else:
        print(f"{email}: 유효하지 않은 이메일 주소입니다.")
