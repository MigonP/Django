from django.forms import ModelForm
from .models import UploadVideoModel, UsrRegModel


class CrateVid(ModelForm):
    class Meta:
        model = UploadVideoModel
        fields = ['video_capition','video_file','video_tags']



