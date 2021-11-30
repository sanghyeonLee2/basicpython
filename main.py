Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

=========== RESTART: C:\Users\hyeon\OneDrive\사진\project\ch11\hw9_2.py ==========
0, 끝내기
1, 캐릭터 추가
2, 캐릭터 확인
3, 캐릭터 선택
4, 캐릭터 인벤토리 조작
메뉴를 선택해주세요.)1
캐릭터 이름을 입력하세요)홍길동
0, 끝내기
1, 캐릭터 추가
2, 캐릭터 확인
3, 캐릭터 선택
4, 캐릭터 인벤토리 조작
메뉴를 선택해주세요.)2
##############
1. 홍길동
##############
0, 끝내기
1, 캐릭터 추가
2, 캐릭터 확인
3, 캐릭터 선택
4, 캐릭터 인벤토리 조작
메뉴를 선택해주세요.)3
선택할 캐릭터의 이름을 입력해주세요.홍길동
홍길동이 선택되었습니다.
0, 끝내기
1, 캐릭터 추가
2, 캐릭터 확인
3, 캐릭터 선택
4, 캐릭터 인벤토리 조작
메뉴를 선택해주세요.)4
선택된 캐릭터는 홍길동 입니다.
0. 끝내기
1. 아이템 추가
2. 아이템 삭제
3. 아이템 확인
4. 아이템 사용
메뉴 번호를 입력하세요)3
{}
0. 끝내기
1. 아이템 추가
2. 아이템 삭제
3. 아이템 확인
4. 아이템 사용
메뉴 번호를 입력하세요)1
아이템을 입력하세요.)
수량을 입력하세요.)
= RESTART: C:\Users\hyeon\OneDrive\사진\project\ch11\hw9_2.py
0, 끝내기
1, 캐릭터 추가
2, 캐릭터 확인
3, 캐릭터 선택
4, 캐릭터 인벤토리 조작
메뉴를 선택해주세요.)
Traceback (most recent call last):
  File "C:\Users\hyeon\OneDrive\사진\project\ch11\hw9_2.py", line 89, in <module>
    option = int(input("메뉴를 선택해주세요.)"))
ValueError: invalid literal for int() with base 10: ''

= RESTART: C:\Users\hyeon\OneDrive\사진\project\ch11\hw9_2.py
0, 끝내기
1, 캐릭터 추가
2, 캐릭터 확인
3, 캐릭터 선택
4, 캐릭터 인벤토리 조작
메뉴를 선택해주세요.)1
캐릭터 이름을 입력하세요)이상현
0, 끝내기
1, 캐릭터 추가
2, 캐릭터 확인
3, 캐릭터 선택
4, 캐릭터 인벤토리 조작
메뉴를 선택해주세요.)2
##############
1. 이상현
##############
0, 끝내기
1, 캐릭터 추가
2, 캐릭터 확인
3, 캐릭터 선택
4, 캐릭터 인벤토리 조작
메뉴를 선택해주세요.)3
선택할 캐릭터의 이름을 입력해주세요.이상현
이상현이 선택되었습니다.
0, 끝내기
1, 캐릭터 추가
2, 캐릭터 확인
3, 캐릭터 선택
4, 캐릭터 인벤토리 조작
메뉴를 선택해주세요.)4
선택된 캐릭터는 이상현 입니다.
0. 끝내기
1. 아이템 추가
2. 아이템 삭제
3. 아이템 확인
4. 아이템 사용
메뉴 번호를 입력하세요)1
아이템을 입력하세요.)ㅁ
수량을 입력하세요.)1
Traceback (most recent call last):
  File "C:\Users\hyeon\OneDrive\사진\project\ch11\hw9_2.py", line 116, in <module>
    use_item(inventory)
  File "C:\Users\hyeon\OneDrive\사진\project\ch11\hw9_2.py", line 52, in use_item
    add_item(new_item, amount, inventory)
TypeError: add_item() takes 1 positional argument but 3 were given

======================== RESTART: C:\Users\hyeon\OneDrive\사진\project\ch11\hw9_2.py ========================
0, 끝내기
1, 캐릭터 추가
2, 캐릭터 확인
3, 캐릭터 선택
4, 캐릭터 인벤토리 조작
메뉴를 선택해주세요.)1
캐릭터 이름을 입력하세요)1
0, 끝내기
1, 캐릭터 추가
2, 캐릭터 확인
3, 캐릭터 선택
4, 캐릭터 인벤토리 조작
메뉴를 선택해주세요.)3
선택할 캐릭터의 이름을 입력해주세요.1
1이 선택되었습니다.
0, 끝내기
1, 캐릭터 추가
2, 캐릭터 확인
3, 캐릭터 선택
4, 캐릭터 인벤토리 조작
메뉴를 선택해주세요.)4
선택된 캐릭터는 1 입니다.
0. 끝내기
1. 아이템 추가
2. 아이템 삭제
3. 아이템 확인
4. 아이템 사용
메뉴 번호를 입력하세요)1
아이템을 입력하세요.)3
수량을 입력하세요.)3
Traceback (most recent call last):
  File "C:\Users\hyeon\OneDrive\사진\project\ch11\hw9_2.py", line 116, in <module>
    use_item(inventory)
  File "C:\Users\hyeon\OneDrive\사진\project\ch11\hw9_2.py", line 52, in use_item
    add_item(new_item, amount, inventory)
TypeError: add_item() takes 1 positional argument but 3 were given

= RESTART: C:\Users\hyeon\OneDrive\사진\project\ch11\hw9_2.py
0, 끝내기
1, 캐릭터 추가
2, 캐릭터 확인
3, 캐릭터 선택
4, 캐릭터 인벤토리 조작
메뉴를 선택해주세요.)File "C:\Users\hyeon\OneDrive\사진\project\ch11\h1
Traceback (most recent call last):
  File "C:\Users\hyeon\OneDrive\사진\project\ch11\hw9_2.py", line 89, in <module>
    option = int(input("메뉴를 선택해주세요.)"))
ValueError: invalid literal for int() with base 10: 'File "C:\\Users\\hyeon\\OneDrive\\사진\\project\\ch11\\h1'

= RESTART: C:\Users\hyeon\OneDrive\사진\project\ch11\hw9_2.py
0, 끝내기
1, 캐릭터 추가
2, 캐릭터 확인
3, 캐릭터 선택
4, 캐릭터 인벤토리 조작
메뉴를 선택해주세요.)1
캐릭터 이름을 입력하세요)1
0, 끝내기
1, 캐릭터 추가
2, 캐릭터 확인
3, 캐릭터 선택
4, 캐릭터 인벤토리 조작
메뉴를 선택해주세요.)2
##############
1. 1
##############
0, 끝내기
1, 캐릭터 추가
2, 캐릭터 확인
3, 캐릭터 선택
4, 캐릭터 인벤토리 조작
메뉴를 선택해주세요.)3
선택할 캐릭터의 이름을 입력해주세요.1
1이 선택되었습니다.
0, 끝내기
1, 캐릭터 추가
2, 캐릭터 확인
3, 캐릭터 선택
4, 캐릭터 인벤토리 조작
메뉴를 선택해주세요.)4
선택된 캐릭터는 1 입니다.
0. 끝내기
1. 아이템 추가
2. 아이템 삭제
3. 아이템 확인
4. 아이템 사용
메뉴 번호를 입력하세요)1
아이템을 입력하세요.)1
수량을 입력하세요.)1
Traceback (most recent call last):
  File "C:\Users\hyeon\OneDrive\사진\project\ch11\hw9_2.py", line 116, in <module>
    use_item(inventory)
  File "C:\Users\hyeon\OneDrive\사진\project\ch11\hw9_2.py", line 52, in use_item
    add_item(new_item, amount, inventory)
  File "C:\Users\hyeon\OneDrive\사진\project\ch11\hw9_2.py", line 5, in add_item
    if check_item(item):
TypeError: check_item() missing 1 required positional argument: 't_character'

= RESTART: C:\Users\hyeon\OneDrive\사진\project\ch11\hw9_2.py
0, 끝내기
1, 캐릭터 추가
2, 캐릭터 확인
3, 캐릭터 선택
4, 캐릭터 인벤토리 조작
메뉴를 선택해주세요.)1
캐릭터 이름을 입력하세요)1
0, 끝내기
1, 캐릭터 추가
2, 캐릭터 확인
3, 캐릭터 선택
4, 캐릭터 인벤토리 조작
메뉴를 선택해주세요.)3
선택할 캐릭터의 이름을 입력해주세요.1
1이 선택되었습니다.
0, 끝내기
1, 캐릭터 추가
2, 캐릭터 확인
3, 캐릭터 선택
4, 캐릭터 인벤토리 조작
메뉴를 선택해주세요.)4
선택된 캐릭터는 1 입니다.
0. 끝내기
1. 아이템 추가
2. 아이템 삭제
3. 아이템 확인
4. 아이템 사용
메뉴 번호를 입력하세요)1
아이템을 입력하세요.)1
수량을 입력하세요.)1
1이 추가되었습니다.
0. 끝내기
1. 아이템 추가
2. 아이템 삭제
3. 아이템 확인
4. 아이템 사용
메뉴 번호를 입력하세요)3
{'1': 1}
0. 끝내기
1. 아이템 추가
2. 아이템 삭제
3. 아이템 확인
4. 아이템 사용
메뉴 번호를 입력하세요)