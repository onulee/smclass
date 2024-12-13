from django.shortcuts import render
from board.models import Board
from member.models import Member
from comment.models import Comment
from django.db.models import F,Q
from django.core.paginator import Paginator
from django.http import JsonResponse
import requests
from django.conf import settings
import json

KAKAO_API_KEY='DEV09ED661AF03847802D5A5F38EC59AC08698DD'
KAKAOPAY_BASE_URL = 'https://open-api.kakaopay.com/online/v1/payment/ready'

# 1. 카카오페이 연결을 위한 페이지
def kakaopay(request):
  return render(request,"kakaopay.html")


# 2. 카카오페이 결제 준비 API 호출
def prepare_payment(request):
    
  headers = {
      "Authorization":f"SECRET_KEY {KAKAO_API_KEY}",
      "Content-Type":"application/json",
  }
  print("headers : ",headers)
  data = {
      "cid": "TC0ONETIME",  # 테스트용 CID, 상용은 발급받은 CID 사용
      "partner_order_id": "order_id_12345",  # 고유 주문 ID
      "partner_user_id": "user_id_67890",  # 고유 사용자 ID
      "item_name": "Test Product",  # 상품명
      "quantity": "1",  # 수량 (0이 아닌 양수)
      "total_amount": "1000",  # 총 결제 금액 (0보다 커야 함)
      "vat_amount": "100",  # 부가세 금액 (총 금액보다 작거나 같아야 함)
      "tax_free_amount": "0",  # 비과세 금액 (생략 가능)
      "approval_url": "http://127.0.0.1:8000/payment/paySuccess",
      "cancel_url": "http://127.0.0.1:8000/payment/payFail",
      "fail_url": "http://127.0.0.1:8000/payment/payCancel",
  }
  print("data : ",data)
  print("KAKAOPAY_BASE_URL : ",KAKAOPAY_BASE_URL)
  response = requests.post(KAKAOPAY_BASE_URL, headers=headers, data=data)
  result = response.json()
  print("결과 : ",result)
  
  
  request.session["tid"] = result["tid"]

  if response.status_code == 200:
      return JsonResponse({"next_redirect_pc_url": result["next_redirect_pc_url"]})
  else:
      return JsonResponse({"error": result}, status=400)

# 3. 성공    
def paySuccess(request):
    tid = request.session.get('tid')
    pg_token = request.GET.get('pg_token')

    if not tid or not pg_token:
        return JsonResponse({'error': 'Missing tid or pg_token'}, status=400)

    approval_url = 'https://kapi.kakao.com/v1/payment/approve'

    data = {
        'cid': 'TC0ONETIME',
        'tid': tid,
        'partner_order_id': 'order_id_12345',
        'partner_user_id': 'user_id_67890',
        'pg_token': pg_token,
    }

    headers = {
        'Authorization': f'KakaoAK {KAKAO_API_KEY}',
        'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8'
    }

    response = requests.post(approval_url, headers=headers, data=data)

    if response.status_code == 200:
        result = response.json()
        return JsonResponse({'success': result})
    else:
        return JsonResponse({'error': response.json()}, status=response.status_code)  


def payFail(request):
  return JsonResponse({"next_redirect_pc_url"})

def payCancel(request):
  return JsonResponse({"next_redirect_pc_url"})

