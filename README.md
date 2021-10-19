# i-Event 2021 - Hitchhiker's Guide to Azure Machine Learning

- [Einführung](#einführung)
- [Custom Vision](#custom-vision)
- [Azure Machine Learning](#azure-machine-learning)
- [MLOps](#mlops)
- [Weiterführende Informationen und Zertifizierungen](#weiterführende-informationen-und-zertifizierungen)

## Einführung

Dies ist das Repository für die "Hitchhiker's Guide to Azure Machine Learning" Technology Session am i-Event 2021.

Auf [Happeo](https://app.happeo.com/pages/1e1oopl952ukqf9e0h/AzureAmpDu/1e5g766dso0ms8i9mp) findest du Informationen zum Azure Login und Sign-up.

![Don't Panic](./images/dont_panic.jpg)

Die Übungen sind nach Schwierigkeitsstufen aufgeteilt:


|                      |                                                |
| -------------------- | ---------------------------------------------- |
| **Einsteiger**       | ![Einsteiger](./images/beginner.png)           |
| **Fortgeschrittene** | ![Fortgeschrittene](./images/intermediate.png) |
| **Experten**         | ![Experten](./images/expert.png)               |

## Custom Vision

Azure Custom Vision ist ein Bilderkennungsdienst, mit dem du deine eigenen Bilderkennungsmodelle erstellen, einsetzen und verbessern kannst. Ein Bilderkennungsmodell versieht Bilder mit Kennzeichnungen (die Klassifizierungen oder Objekte darstellen), die auf den erkannten visuellen Merkmalen basieren. Im Gegensatz zum Computer Vision Service kannst du bei Custom Vision deine eigenen Labels angeben und eigene Modelle trainieren, um sie zu erkennen.

Die Custom Vision-Funktionalität lässt sich in zwei Bereiche unterteilen. Bei der Bildklassifizierung werden einem Bild eine oder mehrere Kennzeichnungen zugewiesen. Die Objekterkennung ist ähnlich, gibt aber auch die Koordinaten im Bild zurück, an denen die angewandte(n) Kennzeichnung(en) zu finden sind.

Die folgenden Beispiele verwenden Bildklassifizierung und je nach Erfahrung könnt ihr aus den folgenden zwei Methoden auswählen:

|                      |                                                |                                                             |
| -------------------- | ---------------------------------------------- | ----------------------------------------------------------- |
| **Einsteiger**       | ![Einsteiger](./images/beginner.png)           | [Custom Vision Website](01_custom_vision/website/README.md) |
| **Fortgeschrittene** | ![Fortgeschrittene](./images/intermediate.png) | [Custom Vision SDK](01_custom_vision/sdk/README.md)         |

Ihr könnt natürlich auch eure eigene Objekterkennung implementieren:

* [Quickstart: Build an object detector with the Custom Vision website](https://docs.microsoft.com/en-us/azure/cognitive-services/custom-vision-service/get-started-build-detector)
* [Quickstart: Create an object detection project with the Custom Vision client library](https://docs.microsoft.com/en-us/azure/cognitive-services/custom-vision-service/quickstarts/object-detection?tabs=visual-studio&pivots=programming-language-python)

## Azure Machine Learning

Azure Machine Learning ist ein Cloud-Service zur Beschleunigung und Verwaltung des Lebenszyklus von Machine Learning-Projekten. Spezialisten für maschinelles Lernen, Data Scientists und Engineers können ihn für ihre täglichen Arbeitsabläufe nutzen: Modelle trainieren und bereitstellen und MLOps verwalten.

Du kannst ein Modell in Azure Machine Learning erstellen oder ein Modell verwenden, das auf einer Open-Source-Plattform wie Pytorch, TensorFlow oder scikit-learn erstellt wurde. MLOps-Tools helfen dir, Modelle zu überwachen, neu zu trainieren und bereitzustellen.

Je nach Erfahrung könnt ihr aus den folgenden drei Methoden auswählen:

|                      |                                                |                                                                      |
| -------------------- | ---------------------------------------------- | -------------------------------------------------------------------- |
| **Einsteiger**       | ![Einsteiger](./images/beginner.png)           | [Azure Machine Learning Automated ML](02_azure_ml/auto_ml/README.md) |
| **Fortgeschrittene** | ![Fortgeschrittene](./images/intermediate.png) | [Azure Machine Learning Designer](02_azure_ml/designer/README.md)    |
| **Experten**         | ![Experten](./images/expert.png)               | [Azure Machine Learning Code](02_azure_ml/code/README.md)            |

## MLOps

MLOps unterstützt Data Scientists und App-Entwickler dabei, ML-Modelle in die Produktion zu bringen. MLOps ermöglicht es dir, jedes Asset in deinem ML-Lifecycle zu verfolgen, zu versionieren, zu prüfen, zu zertifizieren und wiederzuverwenden und bietet Orchestrierungsdienste, um die Verwaltung dieses Lifecycles zu optimieren.

Azure ML enthält eine Reihe von Asset-Management- und Orchestrierungsdiensten, die dir helfen, den Lifecycle deiner Modelltrainings- und Deployment-Workflows zu verwalten.

![ML Lifecycle](./images/ml-lifecycle.png)

Wir werden einen MLOps Lifecycle mit Github Actions implementieren:

|              |                                  |                                                |
| ------------ | -------------------------------- | ---------------------------------------------- |
| **Experten** | ![Experten](./images/expert.png) | [MLOps mit Github Actions](03_mlops/README.md) |

## Weiterführende Informationen und Zertifizierungen

Die Dokumentation der AI und Machine Learning Services von Azure kannst du in der [Azure Dokumentation](https://docs.microsoft.com/en-us/azure/?product=ai-machine-learning) finden.

Microsoft bietet die folgenden AI und Machine Learning Zertifizierungen an:

* [Azure AI Fundamentals](https://docs.microsoft.com/en-us/learn/certifications/azure-ai-fundamentals/) (siehe auch [Microsoft Virtual Training Days](https://www.microsoft.com/en-us/trainingdays))
* [Azure AI Engineer Associate](https://docs.microsoft.com/en-us/learn/certifications/azure-ai-engineer/)
* [Azure Data Scientist Associate](https://docs.microsoft.com/en-us/learn/certifications/azure-data-scientist/)

In der Azure Dokumentation findest du auch Lernpfade zum Erwerb der für die Zertifizierung erforderlichen Fähigkeiten.
