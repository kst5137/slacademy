from django import forms
from .models import Board



class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ('title', 'contents')



# html에서 다음과 같이 폼에다가 input넣는게 귀찮으면 그냥 forms.py를 만들고 위에서 fields값만 잘 지정해 주면됨
# fields값 안에 title과 contents가  input name에 해당
# <!--<form method="post" action="/board/register">-->
# <!--	{% csrf_token %}-->
# <!--	<input type="text" name="title">-->
# <!--	<input type="text" name="content">-->
# <!--	<input type="submit">-->
# <!--</form>-->
