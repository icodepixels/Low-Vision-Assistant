import torch
from transformers import DetrImageProcessor, DetrForObjectDetection
from PIL import Image
import numpy as np

class ObjectDetector:
    def __init__(self):
        self.processor = DetrImageProcessor.from_pretrained("facebook/detr-resnet-50")
        self.model = DetrForObjectDetection.from_pretrained("facebook/detr-resnet-50")

    def detect_objects(self, image_path):
        # Load and process image
        image = Image.open(image_path)
        inputs = self.processor(images=image, return_tensors="pt")

        # Perform inference
        outputs = self.model(**inputs)

        # Convert outputs to detections
        target_sizes = torch.tensor([image.size[::-1]])
        results = self.processor.post_process_object_detection(
            outputs, target_sizes=target_sizes, threshold=0.7)[0]

        detections = []
        for score, label, box in zip(results["scores"], results["labels"], results["boxes"]):
            box = [round(i, 2) for i in box.tolist()]
            detections.append({
                'label': self.model.config.id2label[label.item()],
                'confidence': round(score.item(), 3),
                'box': box
            })

        return detections