def print_reserve_menu():
    print("[메인 메뉴] 실행할 메뉴를 선택하세요.")
    print("1. 영화예매하기")
    print("2. 영화조회하기")
    print("3. 로그아웃")
    print("4. 종료하기")
    while True:
        choice = int(input("입력: "))
        if choice == 1:
            print("영화 예매")
        elif choice == 2:
            print("영화 조회")
            print_check_reservation_menu()
        elif choice == 3:
            print("로그아웃이 완료되었습니다.")
            break
        elif choice == 4:
            print("프로그램을 종료합니다.")
            sys.exit(0)
        else: # 비정상 입력
            print("화면에 출력된 숫자 내에서 입력해주세요")

def reserve():
    # 상영 스케쥴 출력
    schedule_list = get_Schedule_list()
    print(schedule_list)
    # 영화목록
    # 시간표아이디 영화제목  날짜/상영시간     예약인원/최대예약인원   상영관
    #     1      파묘   04.04/08-10        25 / 25명       1관
    # 예매할 영화 번호 입력
    while True:
        print("예매할 시간표 아이디를 입력해주세요")
        choice = int(input("시간표아이디 입력 : "))
        if choice: # 가능한 시간표 아이디 범위 내이면
            if True: # 여석이 모자르면(매진이면)
                print("여석이 없습니다")
            else: # 정상 입력 + 여석 존재면
                break
            # 좌석 출력
        elif choice: # 그 밖의 범위이면
            print("영화가 존재하지 않습니다")
        else: # 문법적으로 올바르지 않을 때
            print("시간표아이디는 숫자로 이루어진 길이가 1 이상인 문자열입니다.")
    
    # 인원 입력
    # 좌석 출력
    #   | 0 1 2 3 4
    #   -----------
    # A | X O X O X
    # B | X O X O X

    while True:
        print("예약인원수를 입력해주세요")
        choice = int(input("예약인원수 입력: "))
        if choice < 1 or choice > 5:
            print("예약인원수는 1~5 사이 숫자로 이루어진 길이가 1인 문자열입니다.")
        else: # 문법이 맞은 경우
            if True: # 예약인원수를 만족하는 연속으로 배치된 좌석이 부족
                print("예약인원수를 만족하는 연속으로 배치된 좌석이 부족합니다.")
            else:
                break

    
    # 좌석 입력
    # 좌석 출력
    #   | 0 1 2 3 4
    #   -----------
    # A | X O X O X
    # B | X O X O X

    while True:
        print("예매할 좌석번호를 입력해주세요")
        print("(좌석번호를 기준으로 오른쪽 방향으로 예약인원수 만큼 예매를 진행합니다.)")
        choice = int(input("좌석번호 입력: "))
        if True: # 문법 규칙에 부합하지 않는 경우
            print("올바른 좌석번호를 입력해 주시기 바랍니다.")
        else: # 문법이 맞은 경우
            if True: # 오른쪽으로 예약인원수만큼 부족하거나 이미 예약된 좌석인 경우
                print("예약이 불가능한 좌석입니다.")
            else:
                break
    
    print("예매가 완료되었습니다")

def print_check_reservation_menu():    
    if False: # 예매한 영화가 없는 경우
        print("예매한 영화가 없습니다")
        return
    
    # 예매내역
    # 예매아이디  영화제목   날짜/상영시간     상영관  예약인원수 시작좌석 시간표아이디
    #    1       파묘   04.04/08-10      1관     2       A3      1


    while True:    
        print("※(예매 취소를 원할 시 '1', 이전 화면으로 돌아가려면 '2'를 눌러주세요)")
        print("1. 영화 예매 취소")
        print("2. 돌아가기")
        choice = int(input("입력: "))

        if choice == 1:
            print("예매 취소")
            print_cancel_reservation_menu()
        elif choice == 2:
            print("메인메뉴로 돌아갑니다.")
            return
        # 왜 비정상 입력에 대한 게 없지

def print_cancel_reservation_menu():

    # 예매내역
    # 예매아이디  영화제목   날짜/상영시간     상영관  예약인원수 시작좌석 시간표아이디
    #    1       파묘   04.04/08-10      1관     2       A3      1

    while True:
        print("예매취소할 예매아이디를 입력해주세요")
        choice = int(input("예매아이디 입력: "))

        if choice: # 문법 규칙 위배
            print("올바른 예매아이디를 입력해 주시기 바랍니다.")
        elif choice: # 의미 규칙 위배(없는 아이디)
            print("예매한 올바른 예매아이디를 입력해주시기 바랍니다.")
            return
        
    print("영화 예매취소가 완료되었습니다. 메인메뉴로 돌아갑니다.")