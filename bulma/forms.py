# -*- coding: utf-8 -*-
import datetime

from django import forms
from django.forms import modelform_factory
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, HTML, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, PrependedAppendedText
from django.utils import timezone

from crispy_bulma.bulma import InlineCheckboxes, InlineRadios
from crispy_bulma.layout import Button, Column, IconField, FormGroup, Row, Submit
from crispy_bulma.widgets import FileUploadInput

from bulma.models import WithFileField


class MessageForm(forms.Form):
    text_input = forms.CharField(
        help_text="help on a text_input",
    )
    text_input_a = forms.CharField()
    text_input_b = forms.CharField()
    text_input_c = forms.CharField()

    integer_input = forms.IntegerField()
    decimal_input = forms.DecimalField()
    url_input = forms.URLField()
    time_input = forms.TimeField()
    date_input = forms.DateField()
    datetime_input = forms.DateTimeField()
    password_input = forms.CharField(widget=forms.PasswordInput, label="Password")

    textarea = forms.CharField(
        widget=forms.Textarea(),
        help_text="help on a textarea",
    )

    radio_buttons = forms.ChoiceField(
        choices=(
            ('option_one',
             "Option one is this and that be sure to include why it's great"),
            ('option_two',
             "Option two can is something else and selecting it will deselect option one")
        ),
        widget=forms.RadioSelect,
        initial='option_two',
        help_text="help on a radio_buttons",
    )

    inline_radio_buttons = forms.ChoiceField(
        choices=(
            ('option_one', 'option_one'),
            ('option_two', 'option_two')
        ),
        widget=forms.RadioSelect,
        initial='option_two',
        help_text="help on a inline_radio_buttons",
    )

    checkboxes = forms.MultipleChoiceField(
        choices=(
            ('option_one',
             "Option one is this and that be sure to include why it's great"),
            ('option_two',
             'Option two can also be checked and included in form results'),
            ('option_three',
             'Option three can yes, you guessed it also be checked and included in form results')
        ),
        initial='option_one',
        widget=forms.CheckboxSelectMultiple,
        help_text="<strong>Note:</strong> Labels surround all the options for much larger click areas and a more usable form.",
    )

    inline_checkboxes = forms.MultipleChoiceField(
        choices=(
            ('bird',
             "it's a bird"),
            ('plane',
             "it's a plane"),
            ('dunno',
             "it's something else !")
        ),
        initial='option_one',
        widget=forms.CheckboxSelectMultiple,
        help_text="help on a inline_checkboxes",
    )

    grouped_checkboxes = forms.MultipleChoiceField(
        choices=(
            ('Group 1',
                ((1, "Option one"),
                 (2, "Option two"),
                 (3, "Option three"))),
            ('Group 2',
                ((4, "Option four"),
                 (5, "Option five"),
                 (6, "Option six"))),
        ),
        initial=(1,),
        widget=forms.CheckboxSelectMultiple,
        help_text="help on a grouped_checkboxes",
    )

    icon_field = forms.CharField(
        help_text="Here's more help text this time on an icon field"
    )

    appended_text = forms.CharField(
        help_text="Here's more help text"
    )

    appended_text2 = forms.CharField(
        help_text="And a bigger appended text field"
    )

    appended_select = forms.ChoiceField(
        label="Select field with appended text",
        choices=[(1, "Choice 1"), (2, "Choice 2")],
        help_text="Some help text"
    )

    prepended_appended_select = forms.ChoiceField(
        label="Select field with both preprended and appended text",
        choices=[(1, "Choice 1"), (2, "Choice 2")],
        help_text="Some help text"
    )

    prepended_select = forms.ChoiceField(
        label="Select field with prepended text",
        choices=[(1, "Choice 1"), (2, "Choice 2")],
        help_text="Some help text"
    )

    prepended_text = forms.CharField()

    prepended_text_two = forms.CharField()

    select = forms.ChoiceField(
        choices=(('1', 'North'), ('2', 'South'), ('3', 'East'), ('4', 'West')),
         help_text='Direction to go'
    )

    multicolon_select = forms.MultipleChoiceField(
        choices=(('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')),
        help_text=(
            'This strange option climbing out of the box is in the examples too '
            'Only without Flexbox '
            'https://v4-alpha.getbootstrap.com/components/forms/#form-controls'),
    )

    split_datetime_field = forms.SplitDateTimeField(
        initial=timezone.now()
    )
    boolean_field = forms.BooleanField()

    file_field = forms.FileField(
        label="file_field",
        widget=FileUploadInput(),
        help_text='with widgets.FileInput()'
    )

    file_field_raw = forms.FileField(
        label="file_field_raw",
        help_text='with default widget',
    )

    # Bulma
    helper = FormHelper()
    helper.layout = Layout(
        Field('text_input', css_class='form-control-lg'),
        Field('textarea', rows="3", css_class='is-primary is-large'),
        'radio_buttons',
        InlineRadios('inline_radio_buttons'),
        Field('checkboxes', style="background: #FAFAFA"),
        InlineCheckboxes('inline_checkboxes'),
        IconField("icon_field", icon_prepend="fa fa-user"),
        'select',
        Field('multicolon_select', size="5"),
        'boolean_field',
        Field('file_field', css_class='is-primary is-large'),
        'file_field_raw',
        # TODO
        # 'grouped_checkboxes',
        Row(
            Column('text_input_a','text_input_b'),
            Column('text_input_c'),
        ),
        "integer_input",
        "decimal_input",
        "url_input",
        "time_input",
        "date_input",

        # TODO
        #'split_datetime_field',
        FormGroup(
            Submit('save_changes', 'Save changes', css_class="is-primary is-large"),
            Button('Cancel'),
        ),
        "datetime_input",
        "password_input",

        FormGroup(
            Submit('save_changes', 'Save changes', css_class="is-primary"),
            Button('Cancel'),
        ),

    )


class HorizontalMessageForm(forms.Form):
    text_input = forms.CharField()
    text_input_a = forms.CharField()
    text_input_b = forms.CharField()
    text_input_c = forms.CharField()

    textarea = forms.CharField(
        widget=forms.Textarea(),
    )

    radio_buttons = forms.ChoiceField(
        choices=(
            ('option_one',
             "Option one is this and that be sure to include why it's great"),
            ('option_two',
             "Option two can is something else and selecting it will deselect option one")
        ),
        widget=forms.RadioSelect,
        initial='option_two',
        help_text="help on a radio_buttons",
    )

    inline_radio_buttons = forms.ChoiceField(
        choices=(
            ('option_one', 'option_one'),
            ('option_two', 'option_two')
        ),
        widget=forms.RadioSelect,
        initial='option_two',
        help_text="help on a inline_radio_buttons",
    )

    checkboxes = forms.MultipleChoiceField(
        choices=(
            ('option_one',
             "Option one is this and that be sure to include why it's great"),
            ('option_two',
             'Option two can also be checked and included in form results'),
            ('option_three',
             'Option three can yes, you guessed it also be checked and included in form results')
        ),
        initial='option_one',
        widget=forms.CheckboxSelectMultiple,
        help_text="<strong>Note:</strong> Labels surround all the options for much larger click areas and a more usable form.",
    )

    inline_checkboxes = forms.MultipleChoiceField(
        choices=(
            ('bird',
             "it's a bird"),
            ('plane',
             "it's a plane"),
            ('dunno',
             "it's something else !")
        ),
        initial='option_one',
        widget=forms.CheckboxSelectMultiple,
        help_text="help on a inline_checkboxes",
    )

    appended_text = forms.CharField(
        help_text="Here's more help text"
    )

    appended_text2 = forms.CharField(
        help_text="And a bigger appended text field"
    )

    prepended_text = forms.CharField()

    prepended_text_two = forms.CharField()

    select = forms.ChoiceField(
        choices=(('1', 'North'), ('2', 'South'), ('3', 'East'), ('4', 'West')),
         help_text='Direction to go'
    )

    multicolon_select = forms.MultipleChoiceField(
        choices=(('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')),
        help_text=(
            'This strange option climbing out of the box is in the examples too '
            'Only without Flexbox '
            'https://v4-alpha.getbootstrap.com/components/forms/#form-controls'),
    )

    boolean_field = forms.BooleanField()
    file_field = forms.FileField(
        widget=FileUploadInput(),
        help_text='with FileInput widget',
        required=True,
    )

    file_field_raw = forms.FileField(
        help_text='with default widget',
        required=True,
    )

    # Bulma
    helper = FormHelper()
    helper.layout = Layout(
        Field('text_input', css_class='form-control-lg'),
        Field('textarea', rows="3", css_class='form-control-lg'),
        Field('radio_buttons'),
        InlineRadios('inline_radio_buttons'),
        Field('checkboxes', style="background: #FAFAFA"),
        InlineCheckboxes('inline_checkboxes'),
        Field('select'),
        Field('multicolon_select'),
        Field('boolean_field'),
        Field('file_field'),
        Field('file_field_raw'),
        FormGroup(
            Submit('save_changes', 'Save changes', css_class="is-primary"),
            Button('Cancel'),
        ),
    )
    helper.form_horizontal = True




class WithFileForm(forms.ModelForm):
    class Meta:
        fields = ['my_file', 'my_char']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['my_file'].widget = FileUploadInput()


FormWithFileField = modelform_factory(WithFileField, form=WithFileForm)
class HorizontalModelForm(forms.ModelForm):
    class Meta:
        model = WithFileField
        fields = '__all__'
    helper = FormHelper()
    helper.form_horizontal = True
