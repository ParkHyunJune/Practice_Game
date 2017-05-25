# 맥도날드에 왔습니다 버거와 음료를 번호를 선택해서 주문하는 프로그램입니다.
from source import Burger, Beverage


def turn_on():
    print('========== 어서오세요 Mcdonald 입니다 ==========')

    sum = 0
    burger1 = Burger(4400, '빅맥')
    burger2 = Burger(5400, '1955')
    burger3 = Burger(4400, '상하이')
    burger4 = Burger(4000, '쉬림프')
    burger5 = Burger(4900, '쿼터파운더치즈')
    burger6 = Burger(5000, '베토디')

    beverage1 = Beverage(1000, '콜라')
    beverage2 = Beverage(1000, '스프라이트')
    beverage3 = Beverage(1500, '아메리카노')
    beverage4 = Beverage(1900, '카페라떼')
    beverage5 = Beverage(2400, '카라멜마끼야또')
    beverage6 = Beverage(2200, '쉐이크')

    while True:
        choice = input('무엇을 주문하시겠습니까?\n  1: Burger\n  2: Beverage\n  3: Confirm\n  0: Goodbye\n  선택번호 : ')
        if choice == '0':
            break
        elif choice == '1':
            burger_choice = input(
                '어떤 햄버거를 고르시겠습니까?\n 1: 빅맥\n 2: 1955\n 3: 상하이\n 4: 쉬림프\n 5: 쿼터파운더치즈\n 6: 베토디\n 0: Exit\n  선택번호 : ')
            if burger_choice == '0':
                break
            elif burger_choice == '1':
                print('버거 가격은 {}입니다.'.format(burger1.price))
                sum += burger1.price
            elif burger_choice == '2':
                print('버거 가격은 {}입니다.'.format(burger2.price))
                sum += burger2.price
            elif burger_choice == '3':
                print('버거 가격은 {}입니다.'.format(burger3.price))
                sum += burger3.price
            elif burger_choice == '4':
                print('버거 가격은 {}입니다.'.format(burger4.price))
                sum += burger4.price
            elif burger_choice == '5':
                print('버거 가격은 {}입니다.'.format(burger5.price))
                sum += burger5.price
            elif burger_choice == '6':
                print('버거 가격은 {}입니다.'.format(burger6.price1))
                sum += burger6.price

        elif choice == '2':
            beverage_choice = input('어떤 음료를 고르시겠습니까?\n 1: 콜라\n 2: 스프라이트\n 3: 아메리카노\n 4: 카페라떼\n  선택번호 : ')
            if beverage_choice == '1':
                print('음료 가격은 {}입니다.'.format(beverage1.price))
                sum += beverage1.price
            elif beverage_choice == '2':
                print('음료 가격은 {}입니다.'.format(beverage2.price))
                sum += beverage2.price
            elif beverage_choice == '3':
                print('음료 가격은 {}입니다.'.format(beverage3.price))
                sum += beverage3.price
            elif beverage_choice == '4':
                print('음료 가격은 {}입니다.'.format(beverage4.price))
                sum += beverage4.price
            elif beverage_choice == '5':
                print('음료 가격은 {}입니다.'.format(beverage5.price))
                sum += beverage5.price
            elif beverage_choice == '6':
                print('음료 가격은 {}입니다.'.format(beverage6.price))
                sum += beverage6.price
        elif choice == '3':
            print('주문하신 상품의 가격은 {}원 입니다.'.format(sum))

    print('========== 안녕히가세요 ==========')


if __name__ == '__main__':
    turn_on()
