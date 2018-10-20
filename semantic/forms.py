# -*- coding: utf-8 -*-
from django import forms

from crispy_forms.bootstrap import AppendedText, FormActions, PrependedText
from crispy_forms.helper import FormHelper
from crispy_forms.layout import HTML, Button, Div, Field, Layout
from crispy_forms_semantic_ui.semantic import StrictButton


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

    multicolon_select = forms.MultipleChoiceField(
        choices=(('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')),
    )

    # Bootstrap4
    helper = FormHelper()
    helper.layout = Layout(
        Field('text_input'),
        Field('textarea'),
        'radio_buttons',
        Field('checkboxes', style="background: #FAFAFA"),
        FormActions(
            StrictButton('Save changes'),
            StrictButton('Cancel'),
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
    )

    # Semantic UI
    helper = FormHelper()
    helper.layout = Layout(
        Field('text_input'),
        Field('textarea', rows="6"),
        'radio_buttons',
        Field('checkboxes'),
        AppendedText('appended_text', '.00'),
        AppendedText('appended_text2', '.00'),
        PrependedText('prepended_text',
                      '<i class="tags icon"></i>',
                      active=True),
        PrependedText('prepended_text_two', '@'),
        'multicolon_select',
        FormActions(
            StrictButton('Save changes'),
            StrictButton('Cancel')
        )
    )

    helper.label_class = ''
    helper.field_class = ''
