from django.shortcuts import redirect


class RedirectToHomePage:
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home page')

        return super().dispatch(request, *args, **kwargs)
