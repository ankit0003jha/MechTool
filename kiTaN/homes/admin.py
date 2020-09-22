from django.contrib import admin
from .models import tools
from .models import contact
from .models import Handtool1
from .models import Powertool1
from .models import Measuringtool1
from .models import Machinetool1
from .models import Automotivetool1
# Register your models here.


admin.site.register(tools)
admin.site.register(contact)
admin.site.register(Handtool1)
admin.site.register(Powertool1)
admin.site.register(Measuringtool1)
admin.site.register(Machinetool1)
admin.site.register(Automotivetool1)