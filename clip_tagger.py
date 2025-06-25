import clip
import torch
from PIL import Image

device = "cuda" if torch.cuda.is_available() else "cpu"
model, preprocess = clip.load("ViT-B/32", device=device)

def get_clip_tags(image_path, candidate_tags):
    image = preprocess(Image.open(image_path)).unsqueeze(0).to(device)
    text = clip.tokenize(candidate_tags).to(device)

    with torch.no_grad():
        image_features = model.encode_image(image)
        text_features = model.encode_text(text)
        logits_per_image, _ = model(image, text)
        probs = logits_per_image.softmax(dim=-1).cpu().numpy()

    tag_scores = list(zip(candidate_tags, probs[0]))
    return sorted(tag_scores, key=lambda x: x[1], reverse=True)

