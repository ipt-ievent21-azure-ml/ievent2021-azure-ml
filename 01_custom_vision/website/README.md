# Custom Vision: Erstellen einer Klassifizierung mit der Custom Vision-Website

|              |                                  |
| ------------ | -------------------------------- |
| **Einsteiger** | ![Einsteiger](../../images/beginner.png) |

- [Einführung](#einführung)
- [Projekt und Resource erstellen](#projekt-und-resource-erstellen)
- [Bilder hochladen und taggen](#bilder-hochladen-und-taggen)
- [Classifier trainieren und evaluieren](#classifier-trainieren-und-evaluieren)
- [Referenzen](#referenzen)

## Einführung

In dieser Übung erstellst du auf der Custom Vision Website ein Modell zur Bildklassifizierung. Sobald du ein Modell erstellt hast, kannst du es mit neuen Bildern testen.

Als Beispiel kannst du die Bilder der Simpsons im [dataset](../dataset) Ordner benutzen.

## Projekt und Resource erstellen

Gehe zur [Custom Vision Website](https://www.customvision.ai/) und logge dich mit deinen ipt Credentials ein:

![Sign in](images/sign_in.png)

Erstelle ein neues Projekt:

![Create new project](images/create_new_project.png)

Erstelle eine neue Custom Vision Resource. Dazu musst du zuerst eine neue Resource Group in "West Europe" erstellen und dann die neue Custom Vision Resource dieser Gruppe zuweisen:

![Create new resource](images/create_new_resource.png)

Danach kannst du den Projekttyp, Klassifizierungstyp und die [Domain](https://docs.microsoft.com/en-us/azure/cognitive-services/custom-vision-service/select-domain) konfigurieren:

![Configure new project](images/configure_new_project.png)

## Bilder hochladen und taggen

Nun können Bilder hochgeladen und getaggt werden:

![Upload and tag images](images/upload_images.png)

## Classifier trainieren und evaluieren

Nachdem die Bilder hochgeladen und getaggt wurden, kann das Modell trainiert werden:

![Model training](images/model_training_1.png)

Das Training dauert circa 10 Minuten:

![Model training](images/model_training_2.png)

Wenn das Training fertig ist, zeigt Custom Vision Precision, Recall und die Performance:

![Precision, recall and performance](images/precision_recall_ap.png)



## Referenzen

* [Custom Vision Dokumentation](https://docs.microsoft.com/en-us/azure/cognitive-services/custom-vision-service/)
* [The Simpsons Characters Data](https://www.kaggle.com/alexattia/the-simpsons-characters-dataset)
* [Prediction API](https://docs.microsoft.com/en-us/azure/cognitive-services/custom-vision-service/use-prediction-api)
* [Custom Vision Domains](https://docs.microsoft.com/en-us/azure/cognitive-services/custom-vision-service/select-domain)
