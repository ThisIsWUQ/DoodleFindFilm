# Set up and test an image-to-text model from  HuggingFace
# reference: https://huggingface.co/tasks/image-to-text
# ---------------------------------------------------------------------------------
from transformers import pipeline

# Load pretrained model
pipe = pipeline("image-to-text", model="Salesforce/blip-image-captioning-large")
print("model loaded successfully")
# ---------------------------------------------------------------------------------
