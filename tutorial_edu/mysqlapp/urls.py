from django.urls import path

### 사용자의 페이지주소에 해당하는 처리함수는 모듈단위로 구성됩니다.
# - 해당 모듈 내에 함수로 정의되어 있습니다.
from . import views

urlpatterns = [
    ### http://127.0.0.1:8000/mysql/
    path('', views.index),
    
    ######## [회원관리 영역] #########
    ### /mysql/mem_list/
    path('mem_list/', views.getMemberList),
    ### /mysql/mem_view/
    path('mem_view/', views.getMemberView),
    ### /mysql/mem_update_view/
    path('mem_update_view/', views.getMemberUpdateView),
    ### /mysql/mem_update/
    path('mem_update/', views.getMemberUpdate),
    
    
    ######## [주문내역/장바구니 영역] ########
    ### /mysql/cart_list/
    path('cart_list/', views.getCartList),
    ### /mysql/cart_view/
    path('cart_view/', views.getCartView),
    ### /mysql/cart_update_view/
    path('cart_update_view/', views.getCartUpdateView),
    ### /mysql/cart_update/
    path('cart_update/', views.getCartUpdate),
    ### /mysql/cart_delete/
    path('cart_delete/', views.getCartDelete),
    ### /mysql/cart_insert_view/
    path('cart_insert_view/', views.getCartInsertView),
    ### /mysql/cart_insert/
    path('cart_insert/', views.getCartInsert),
    
    ########## [페이징 처리] ##########
    ### /mysql/cart_list_page/
    path('cart_list_page/', views.getCartListPaging),
    
    
    ######### [세션(session) 처리] ########
    ### /mysql/login_logout_view/
    path('login_logout_view/', views.login_logout_view),
    ### /mysql/login/
    path('login/', views.login),
    ### /mysql/logout/
    path('logout/', views.logout),
    
        
]
