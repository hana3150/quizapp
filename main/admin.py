from django.contrib import admin

from .models import User, Quiz, Question, Choice, QuizAnswer,QuizInformation # Quiz, Question, Choice を追加

admin.site.register(User)
admin.site.register(Quiz) # 追加
admin.site.register(Question) # 追加
admin.site.register(Choice) # 追加
admin.site.register(QuizAnswer) # 追加
admin.site.register(QuizInformation) # 追加
