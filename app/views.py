from django.shortcuts import render
from django.conf import settings
from datetime import datetime
from django.http import JsonResponse


def index(request):
    """view of list"""
    settings.ES.index(
        index="my-index",
        doc_type="test-type",
        id=42,
        body={"any": "data", "timestamp": datetime.now()},
    )
    {
        u"_id": u"42",
        u"_index": u"my-index",
        u"_type": u"test-type",
        u"_version": 1,
        u"ok": True,
    }
    return JsonResponse({'foo':'bar'})
