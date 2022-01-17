from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.



# # abc = "qwer1234"
# def func1(abcde) :
#     return HttpResponse()


# def func1(abcde) :
#     return HttpResponse("zzzz")
#     # 장고의 함수는 무조건 매개변수를 필요로 함 안하면 에러뜸
#     # 반활해줄때도 일반 문자열을 그대로 반환해주면 안되고
    # HttpResponse() 로 응답해줘야함 그안에 zzzz가 abcde에 저장되서 전달되는거

def func1(abcde) :

    # var1 = abcde.POST.get("var1", None)
    # var2 = abcde.POST.get("var2", None)
    #
    # print(var1)
    # print(var2)

    return render(abcde, 'abc/def.html')

# def func2(abcde) :
#
#     var1 = abcde.GET.get('var1',None)   # 변수 = 함수의 매개변수.GET.get('키에 해당하는 값',기본값)
#     #매개변수에 저장된 데이터 중 get방식의 데이터만 가져오겠다.
#     #뒤에 None은 안써줘도 됨 안썼을때 데이터를 안보내면 에러가 날 수 있기 때문에
#     # var1에 기본값에 해당하는 값을 입력
#     var2 = abcde.GET.get('var2', None)
#
#     print(int(var1)+ int(var2) + 10)
#
#     return render(abcde, 'ex01/func2.html')

def func2(abcde) :




    return render(abcde, 'ex01/func2.html')
def func3(abcde) :

    # 서버에서 데이터를 보낼때는 무조건 딕셔너리 형태
    context = {"var1" : 10 , "var2" : 20 }

    return render(abcde, 'ex01/func3.html', context)
#                                               위의 context를 ex01/func3.html로 포함시켜 보내겠다는 뜻
#                                               클라이언트도 저걸 받아와야함
# render라는 함수가 context를 받아와 ex01/func3.html을 완성시킨다는 개념

#abc폴더 밑에 def.html을 실행한다는 뜻



