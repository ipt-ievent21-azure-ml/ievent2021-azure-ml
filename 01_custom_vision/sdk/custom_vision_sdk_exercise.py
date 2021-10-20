#!/usr/bin/python

from azure.cognitiveservices.vision.customvision.training import CustomVisionTrainingClient
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from azure.cognitiveservices.vision.customvision.training.models import ImageFileCreateBatch, ImageFileCreateEntry, Region
from msrest.authentication import ApiKeyCredentials
import os
import time
import uuid

# Azure endpoint and subscription keys: Replace with valid values
ENDPOINT = "PASTE_YOUR_CUSTOM_VISION_TRAINING_ENDPOINT_HERE"
training_key = "PASTE_YOUR_CUSTOM_VISION_TRAINING_SUBSCRIPTION_KEY_HERE"
prediction_key = "PASTE_YOUR_CUSTOM_VISION_PREDICTION_SUBSCRIPTION_KEY_HERE"
prediction_resource_id = "PASTE_YOUR_CUSTOM_VISION_PREDICTION_RESOURCE_ID_HERE"

# Authenticate the client
credentials = ApiKeyCredentials(in_headers={"Training-key": training_key})
trainer = CustomVisionTrainingClient(ENDPOINT, credentials)
prediction_credentials = ApiKeyCredentials(
    in_headers={"Prediction-key": prediction_key})
predictor = CustomVisionPredictionClient(ENDPOINT, prediction_credentials)

# Configure the iteration name
publish_iteration_name = "classifyModel"

credentials = ApiKeyCredentials(in_headers={"Training-key": training_key})
trainer = CustomVisionTrainingClient(ENDPOINT, credentials)

# Create a new project
print("Creating project...")
project_name = "The Simpsons Classifier (SDK)"
project = trainer.create_project(
    project_name,
    description="Classify your favorite characters from The Simpsons",
    domain_id="2e37d7fb-3a54-486a-b4d6-cfc369af0018",
    classification_type="Multiclass")

# Upload and tag images
base_image_location = os.path.join(os.path.dirname(
    __file__), "..", "dataset", "simpsons_dataset")

print("Adding images...")

image_list = []

for dir in os.listdir(base_image_location):
    # Create tags
    tag = trainer.create_tag(project.id, dir)

    for image_num in range(0, 100):
        file_name = f"pic_{str(image_num).zfill(4)}.jpg"
        with open(os.path.join(base_image_location, dir, file_name), "rb") as image_contents:
            image_list.append(ImageFileCreateEntry(
                name=file_name, contents=image_contents.read(), tag_ids=[tag.id]))

for i in range(0, len(image_list), 64):
    batch = image_list[i:i+64]
    upload_result = trainer.create_images_from_files(
        project.id, ImageFileCreateBatch(images=batch))
    if not upload_result.is_batch_successful:
        print("Image batch upload failed.")
        for image in upload_result.images:
            print("Image status: ", image.status)
        exit(-1)

# Train the project
print("Training...")
iteration = trainer.train_project(project.id)
while (iteration.status != "Completed"):
    iteration = trainer.get_iteration(project.id, iteration.id)
    print("Training status: " + iteration.status)
    print("Waiting 10 seconds...")
    time.sleep(10)

# Publish the current iteration
trainer.publish_iteration(project.id, iteration.id,
                          publish_iteration_name, prediction_resource_id)
print("Done!")

# Test the prediction endpoint
prediction_credentials = ApiKeyCredentials(
    in_headers={"Prediction-key": prediction_key})
predictor = CustomVisionPredictionClient(ENDPOINT, prediction_credentials)

test_image_location = os.path.join(os.path.dirname(
    __file__), "..", "dataset", "simpsons_testset")

with open(os.path.join(test_image_location, "maggie_simpson_0.jpg"), "rb") as image_contents:
    results = predictor.classify_image(
        project.id, publish_iteration_name, image_contents.read())

    # Display the results.
    for prediction in results.predictions:
        print("\t" + prediction.tag_name +
              ": {0:.2f}%".format(prediction.probability * 100))

# # Unpublish the project
# print("Unpublishing project...")
# trainer.unpublish_iteration(project.id, iteration.id)

# # Delete the project
# print("Deleting project...")
# trainer.delete_project(project.id)
