from polls.models import Category
from django.contrib.auth.forms import AuthenticationForm

# ini sbnrnya kurang bagus sih dijadiin global variable. kalo personal project gpp sih
# tapi kalo udh team project gk boleh kyk gini ya. kl udh team project msti bikin segimana caranya org lain pas baca itu gmpang nyari dan mengertinya in case ada bug. meskipun bkl nambah bbrp line code
def categories(request):
    return {'categories': Category.objects.all()}


def login_form(request):
    return {'login_form': AuthenticationForm()}
