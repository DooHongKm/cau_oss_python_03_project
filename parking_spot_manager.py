class parking_spot:
    """
    주차장의 이름, 위치 등을 나타내는 클래스
    """ 
    def __init__(self, name, city, district, ptype, longitude, latitude):
        """
        parking_spot 객체를 초기화하는 생성자 메서드
        Args:
            name      (str)  : 주차장의 자원명
            city      (str)  : 주차장이 위치한 시 or도
            district  (str)  : 주차장이 위치한 시 or 군 or 구
            ptype     (str)  : 주차장의 유형
            longitude (float): 주차장의 경도
            latitude  (float): 주차장의 위도
        """
        self.__item = {
            'name': name,
            'city': city,
            'district': district,
            'ptype': ptype,
            'longitude': longitude,
            'latitude': latitude
        }    
    def __str__(self):
        """
        parking_spot 객체의 반환 형식을 지정하고 해당 형식으로 반환하는 메서드
        Returns:
            str: 객체의 반환 형식
        """    
        item = self.__item
        s  = f"[{item['name']}({item['ptype']})] "
        s += f"{item['city']} {item['district']}"
        s += f"(lat:{item['latitude']}, long:{item['longitude']})"
        return s
    def get(self, keyword='name'):
        """
        parking_spot 객체에서 입력한 keyword의 value를 반환하는 메서드
        Args:
            keyword (str): name, city 등의 keyword
        Returns:
            str, float: 입력받은 keyword의 value
        """
        return self.__item[keyword]

def str_list_to_class_list(str_list):
    """
    매개변수로 받은 문자열을 줄마다 파싱하여 딕셔너리 리스트로 만드는 함수
    Args:
        str_list (list): 파일로부터 받은 파일 내용, 여러 줄의 문자열
    Returns:
        list: 각 원소가 딕셔너리인 리스트로 모든 spot 정보를 반환
    """
    class_list = []
    for str in str_list:
        items = str.split(',')
        name = items[1].strip()
        city = items[2].strip()
        district = items[3].strip()
        ptype = items[4].strip()
        longitude = float(items[5].strip())
        latitude = float(items[6].strip())
        ps = parking_spot(name, city, district, ptype, longitude, latitude)
        class_list.append(ps)
    return class_list

def print_spots(spots):
    """
    spot 정보가 들어있는 딕셔너리 리스트에서 각 딕셔너리를 출력 형식에 맞게 출력하는 함수
    Args:
        spots (list): 각 원소가 딕셔너리인 리스트
    """
    print(f"---print elements({len(spots)})---")
    for spot in spots:
        print(spot)

# value를 입력받아 해당 keyword의 value가 일치하는 모든 spot의 리스트를 반환하는 함수
def filter_by_name(spots, name):
    return [spot for spot in spots if name in spot.get('name')]
def filter_by_city(spots, city):
    return [spot for spot in spots if city in spot.get('city')]
def filter_by_district(spots, district):
    return [spot for spot in spots if district in spot.get('district')]
def filter_by_ptype(spots, ptype):
    return [spot for spot in spots if ptype in spot.get('ptype')]
def filter_by_location(spots, locations):
    min_lat, max_lat, min_long, max_long = locations
    return [spot for spot in spots if min_lat < spot.get('latitude') < max_lat and min_long < spot.get('longitude') < max_long]    

def sort_by_keyword(spots, keyword):
    """
    매개변수로 받은 keyword를 기준으로 spot을 정렬하는 함수
    Args:
        spots   (list): 각 원소가 딕셔너리인 리스트
        keyword (str) : name, city 등의 keyword
    Returns:
        list: 각 원소가 딕셔너리인 리스트로 정렬된 spot 정보를 반환
    """
    return sorted(spots, key = lambda spot: spot.get(keyword))

# 각 단계별로 테스트 (테스트할때 주석해제 후 사용)
if __name__ == '__main__':
    
    print("Testing the module...")
    
    # version#2
    import file_manager
    str_list = file_manager.read_file("./input/free_parking_spot_seoul.csv")
    spots = str_list_to_class_list(str_list)
    print_spots(spots)
    
    # version#3
    spots = filter_by_district(spots, '동작')
    print_spots(spots)
    
    # version#4
    spots = sort_by_keyword(spots, 'name')
    print_spots(spots)