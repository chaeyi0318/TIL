from django.urls import path
from . import views

app_name='games'

urlpatterns = [
    # 1. 게임화면 출력 url
    path('start/', views.start_game, name='start_game'),
    # 2. 정답을 체크할 수 있는 url
    path('make-guess/<int:game_session_id>/', views.make_guess, name='make_guess')
]