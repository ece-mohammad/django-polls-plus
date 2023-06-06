from django.contrib import admin


from .models import Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    # customize questions display in admin page
    list_display = ["question_text", "pub_date", "was_published_recently"]

    # add filter based on pub_date
    list_filter = ["pub_date"]
    
    # search field
    search_fields = ["question_text"]

    # question input fields (form)
    fieldsets = [
            (
                # title
                None,

                # input fields
                {
                    "fields": ["question_text"]
                }
            ),
            (
                # title
                "Date information",

                # input fields
                {
                    "fields": ["pub_date"],
                    "classes": ["collapse"]
                }
            )
    ]

    inlines = [ChoiceInline]



# admin.site.register(Question)
#admin.site.register(Choice)

admin.site.register(Question, QuestionAdmin)


