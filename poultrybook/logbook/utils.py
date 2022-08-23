from django.apps import apps

from .configs import RECORDS_TYPES
from .models import IntegerRecord, FloatRecord, TextRecord
from .forms import IntegerRecordForm, FloatRecordForm, TextRecordForm


def get_datatype_model(content_type):
    model_name = RECORDS_TYPES[content_type]
    return apps.get_model(model_name)


def get_datatype_form(content_type):
    model = get_datatype_model(content_type)
    if model == IntegerRecord:
        return IntegerRecordForm
    elif model == FloatRecord:
        return FloatRecordForm
    elif model == TextRecord:
        return TextRecordForm
    else:
        raise Exception('Record type does not supported')