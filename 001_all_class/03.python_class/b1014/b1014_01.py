# 함수정의
def shop_caution():
  print("[ 주의 사항 ]")
  print("전자상거래 등에서의 소비자보호법에 관한 법률에 의거하여 미성년자가 물품을 구매하는 경우,")
  print("법정대리인이 동의하지 않으면 미성년자 본인 또는 법정대리인이 구매를 취소할 수 있습니다.")
  print("G마켓에 등록된 판매 상품과 상품의 내용, 거래 정보 및 가격은 판매자가 등록한 것으로")
  print("G마켓은 해당 내용에 대하여 일체의 책임을 지지 않습니다.")
  print("G마켓의 결제시스템을 이용하지 않고 판매자와 직접 거래하실 경우 상품을 받지 못하거나 구매한 상품과 상이한 상품을 받는 등")
  print("피해가 발생할 수 있으니 유의 바랍니다. 직거래로 인해 발생한 피해에 대해 G마켓은 책임을 지지 않습니다.")

# 자바스크립트 함수
# function shop_caution(매개변수){
#   return 
# }



while True:
  print("[ 쇼핑몰 프로그램 ]")
  print("1. 가방")
  print("2. 식품")
  print("3. 신발")
  print("4. 의류")
  choice = input("번호를 입력하면 원하는 상품이 구매 됩니다. 번호를 입력하세요.>> ")

  if choice == "1":
    print("가격 : 100만원")
    print("브랜드 : 구찌")
    print("구매장소 : 롯데백화점")
    shop_caution() # 함수호출
    
  elif choice == "2":
    print("가격 : 10만원")
    print("브랜드 : 신세계")
    print("구매장소 : 신세계백화점")
    shop_caution() # 함수호출
  elif choice == "3":
    print("가격 : 20만원")
    print("브랜드 : 나이키")
    print("구매장소 : 현대백화점")
    shop_caution() # 함수호출
  elif choice == "4":
    print("가격 : 200만원")
    print("브랜드 : 샤넬")
    print("구매장소 : 갤러리아")
    shop_caution() # 함수호출
