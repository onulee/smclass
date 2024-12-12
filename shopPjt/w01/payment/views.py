from django.shortcuts import render
from board.models import Board
from member.models import Member
from comment.models import Comment
from django.db.models import F,Q
from django.core.paginator import Paginator
from django.http import JsonResponse
import requests
from django.conf import settings

def approval(request):
  return JsonResponse({"next_redirect_pc_url": result["next_redirect_pc_url"]})

def cancel(request):
  return JsonResponse({"next_redirect_pc_url"})

def fail(request):
  return JsonResponse({"next_redirect_pc_url"})
