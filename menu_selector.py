import file_manager as fm
import parking_spot_manager as psm

def start_process(path):
    """
    path로부터 파일 내용을 받아와서 각 원소가 딕셔너리인 리스트로 변환 후,
    사용자의 input에 맞게 print, filter, sort, exit하는 함수
    Args:
        path (string): 파일 경로
    Examples:
        input==1: parking_spot 객체의 출력 형식에 맞게 모든 spot을 출력
        input==2: 사용자가 입력한 value와 일치하는 spot을 찾아서 출력
        input==3: 사용자가 입력한 keyword를 기준으로 spot을 정렬하여 출력
        input==4: "Exit"를 출력하고, 반복을 종료
    """
    # 모든 case에서 사용 가능한 spots, update 가능
    str_list = fm.read_file(path)
    spots = psm.str_list_to_class_list(str_list)
    while True:        
        print("---menu---")
        print("[1] print")
        print("[2] filter")
        print("[3] sort")
        print("[4] exit")
        select = int(input('type:'))
        if select == 1:
            psm.print_spots(spots)
        elif select == 2:
            print("---filter by---")
            print("[1] name")
            print("[2] city")
            print("[3] district")
            print("[4] ptype")
            print("[5] location")
            select = int(input('type:'))
            if select == 1:
                keyword = input('type name:')
                spots = psm.filter_by_name(spots, keyword)
            elif select == 2:
                keyword = input('type city:')
                spots = psm.filter_by_city(spots, keyword)
            elif select == 3:
                keyword = input('type district:')
                spots = psm.filter_by_district(spots, keyword)
            elif select == 4:
                keyword = input('type ptype:')
                spots = psm.filter_by_ptype(spots, keyword)
            elif select == 5:
                min_lat = float(input('type min lat:'))
                max_lat = float(input('type max lat:'))
                min_long = float(input('type min long:'))
                max_long = float(input('type max long:'))
                keyword = (min_lat, max_lat, min_long, max_long)
                spots = psm.filter_by_location(spots, keyword)
            else:
                print("invalid input")
        elif select == 3:
            keywords = ['name', 'city', 'district', 'ptype', 'latitude', 'longitude']
            print("---sort by---")
            print(keywords)
            keyword = input('type keyword:')
            if keyword in keywords:
                print("not implemented yet")
                # fill this block
            else: print("invalid input")
        elif select == 4:
            print("Exit")
            break
        else:
            print("invalid input")