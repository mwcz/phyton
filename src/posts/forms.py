from django import forms
from src.photos.models import Post
from src.photos.cs import palette
from src.settings import IMAGE_SIZE_BOUNDS, MEDIA_ROOT
from custom_widgets import *
from PIL import Image

