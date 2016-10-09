# -*- coding: utf-8 -*-
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions


class MessageForm(forms.Form):
    text_input = forms.CharField()

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

    appended_text = forms.CharField(
        help_text="Here's more help text"
    )

    appended_text2 = forms.CharField(
        help_text="And a bigger appended text field"
    )

    prepended_text = forms.CharField()

    prepended_text_two = forms.CharField()

    multicolon_select = forms.MultipleChoiceField(
        choices=(('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')),
        help_text=(
            'This strange option climbing out of the box is in the examples too '
            'Only without Flexbox '
            'https://v4-alpha.getbootstrap.com/components/forms/#form-controls'),
    )

    boolean_field = forms.BooleanField()

    # Bootstrap4
    helper = FormHelper()
    helper.layout = Layout(
        Field('text_input', css_class='form-control-lg'),
        Field('textarea', rows="3", css_class='form-control-lg'),
        'radio_buttons',
        Field('checkboxes', style="background: #FAFAFA"),
        AppendedText('appended_text', '.00'),
        AppendedText('appended_text2', '.00', css_class='form-control-lg'),
        PrependedText('prepended_text',
                      '<input type="checkbox" checked="checked" value="" id="" name="">',
                      active=True),
        PrependedText('prepended_text_two', '@'),
        'multicolon_select',
        'boolean_field',
        FormActions(
            Submit('save_changes', 'Save changes', css_class="btn-primary"),
            Submit('cancel', 'Cancel'),
        )
    )

class HorizontalMessageForm(forms.Form):
    text_input = forms.CharField()

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

    appended_text = forms.CharField(
        help_text="Here's more help text"
    )

    appended_text2 = forms.CharField(
        help_text="And a bigger appended text field"
    )

    prepended_text = forms.CharField()

    prepended_text_two = forms.CharField()

    multicolon_select = forms.MultipleChoiceField(
        choices=(('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')),
        help_text=(
            'This strange option climbing out of the box is in the examples too '
            'Only without Flexbox '
            'https://v4-alpha.getbootstrap.com/components/forms/#form-controls'),
    )

    boolean_field = forms.BooleanField()

    # Bootstrap4
    helper = FormHelper()
    helper.layout = Layout(
        Field('text_input', css_class='form-control-lg'),
        Field('textarea', rows="3", css_class='form-control-lg'),
        Field('radio_buttons'),
        Field('checkboxes', style="background: #FAFAFA"),
        AppendedText('appended_text', '.00'),
        AppendedText('appended_text2', '.00', css_class='form-control-lg'),
        PrependedText('prepended_text',
                      '<input type="checkbox" checked="checked" value="" id="" name="">',
                      active=True),
        PrependedText('prepended_text_two', '@'),
        Field('multicolon_select'),
        Field('boolean_field'),
        Div(
            Div(
                Submit('save_changes', 'Save changes', css_class="btn-primary"),
                Submit('cancel', 'Cancel'),
                css_class='col-8 ml-auto'
            ),
            css_class='form-group row'
        )
    )
    helper.form_group_wrapper_class = 'row'

    helper.label_class = 'col-4'
    helper.field_class = 'col-8'
