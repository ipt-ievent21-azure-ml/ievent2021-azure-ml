# i-Event 2021 - Hitchhiker's Guide to Azure Machine Learning

- [Einführung](#einführung)
- [Custom Vision](#custom-vision)
- [Azure Machine Learning](#azure-machine-learning)
- [MLOps](#mlops)
- [Ressourcen aufräumen](#ressourcen-aufräumen)
- [Weiterführende Informationen und Zertifizierungen](#weiterführende-informationen-und-zertifizierungen)

## Einführung

Willkommen zum "Hitchhiker's Guide to Azure Machine Learning" Repository für die Technology Session am i-Event 2021.

Auf [Happeo](https://app.happeo.com/pages/1e1oopl952ukqf9e0h/AzureAmpDu/1e5g766dso0ms8i9mp) findest du Informationen zum Azure Login und [Sign-up](https://ipt-sandbox-selfservice.azurewebsites.net/signup).

![Don't Panic](./images/dont_panic.jpg)

Die Tutorials sind nach Schwierigkeitsstufen aufgeteilt:

|                      |                                                |
| -------------------- | ---------------------------------------------- |
| **Einsteiger**       | ![Einsteiger](./images/beginner.png)           |
| **Fortgeschrittene** | ![Fortgeschrittene](./images/intermediate.png) |
| **Experten**         | ![Experten](./images/expert.png)               |

Je nach deiner Erfahrung kannst du dir auswählen, welches Tutorial du gerne machen möchtest. Für jedes Tutorial ist auch angegeben, wie lange es ungefähr dauert. Die Dauer ist jeweils inklusive der Bereitstellung der Infrastruktur in Azure und dem Training der Machine Learning Modelle. Bei den Tutorial Schritten ist ebenfalls vermerkt, wenn das Ausführen länger dauert. Du kannst diese Zeit nutzen um ein anderes Tutorial zu beginnen.

## Custom Vision

Azure Custom Vision ist ein Bilderkennungsdienst, mit dem du deine eigenen Bilderkennungsmodelle erstellen, einsetzen und verbessern kannst. Ein Bilderkennungsmodell versieht Bilder mit Labels (die Klassifizierungen oder Objekte darstellen), die auf den erkannten visuellen Merkmalen basieren. Im Gegensatz zum Computer Vision Service kannst du bei Custom Vision deine eigenen Labels angeben und eigene Modelle trainieren, um sie zu erkennen.

Die Custom Vision-Funktionalität lässt sich in zwei Bereiche unterteilen:
* Bei der Bildklassifizierung werden einem Bild eine oder mehrere Labels zugewiesen
* Die Objekterkennung ist ähnlich, gibt aber auch die Koordinaten im Bild zurück, an denen die angewandte(n) Labels zu finden sind

Die folgenden Tutorials benutzen Bildklassifizierung und je nach deiner Erfahrung kannst du aus den folgenden zwei Methoden auswählen:

|                      |                                                |                                                              |            |
| -------------------- | ---------------------------------------------- | ------------------------------------------------------------ | ---------- |
| **Einsteiger**       | ![Einsteiger](./images/beginner.png)           | [Custom Vision: Website](01_custom_vision/website/README.md) | 20 Minuten |
| **Fortgeschrittene** | ![Fortgeschrittene](./images/intermediate.png) | [Custom Vision: SDK](01_custom_vision/sdk/README.md)         | 20 Minuten |

Du kannst auch beide Methoden ausprobieren.

## Azure Machine Learning

Azure Machine Learning ist ein Cloud Service zur Beschleunigung und Verwaltung des Lebenszyklus von Machine Learning Projekten. Spezialisten für maschinelles Lernen, Data Scientists und Engineers können ihn für ihre täglichen Arbeitsabläufe nutzen: Modelle trainieren und deployen und MLOps managen.

Du kannst ein Modell in Azure Machine Learning erstellen oder ein Modell verwenden, das auf einer Open Source Plattform wie Pytorch, TensorFlow oder scikit-learn erstellt wurde. MLOps Tools helfen dir, Modelle zu überwachen, neu zu trainieren und bereitzustellen.

Je nach Erfahrung kannst du aus den folgenden drei Tutorials auswählen:

|                      |                                                |                                                                       |            |
| -------------------- | ---------------------------------------------- | --------------------------------------------------------------------- | ---------- |
| **Einsteiger**       | ![Einsteiger](./images/beginner.png)           | [Azure Machine Learning: Automated ML](02_azure_ml/auto_ml/README.md) | 45 Minuten |
| **Fortgeschrittene** | ![Fortgeschrittene](./images/intermediate.png) | [Azure Machine Learning: Designer](02_azure_ml/designer/README.md)    | 60 Minuten |
| **Experten**         | ![Experten](./images/expert.png)               | [Azure Machine Learning: Code](02_azure_ml/code/README.md)            | 60 Minuten |

Du kannst auch mehrere Methoden ausprobieren.

## MLOps

MLOps unterstützt Data Scientists und App Entwickler dabei, Machine Learning Modelle in die Produktion zu bringen. MLOps ermöglicht es dir, jedes Asset in deinem Machine Learning Lifecycle zu verfolgen, zu versionieren, zu prüfen, zu zertifizieren und wiederzuverwenden und bietet Orchestrierungsdienste, um die Verwaltung dieses Lifecycles zu optimieren.

Azure ML enthält eine Reihe von Asset-Management- und Orchestrierungsdiensten, die dir helfen, den Lifecycle deiner Modelltrainings- und Deployment-Workflows zu verwalten.

![ML Lifecycle](./images/ml-lifecycle.png)

In diesem Tutorial wirst du einen MLOps Lifecycle mit GitHub Actions implementieren:

|              |                                  |                                             |            |
| ------------ | -------------------------------- | ------------------------------------------- | ---------- |
| **Experten** | ![Experten](./images/expert.png) | [MLOps: GitHub Actions](03_mlops/README.md) | 90 Minuten |

## Ressourcen aufräumen

Wenn deine Ressourcengruppe nicht mehr benötigt wird, löschst du die Ressourcen, die du erstellt hast, indem du die Ressourcengruppe löschst.

## Weiterführende Informationen und Zertifizierungen

Die Dokumentation der AI und Machine Learning Services von Azure kannst du in der [Azure Dokumentation](https://docs.microsoft.com/en-us/azure/?product=ai-machine-learning) finden.

Microsoft bietet die folgenden AI und Machine Learning Zertifizierungen an:

* [Azure AI Fundamentals](https://docs.microsoft.com/en-us/learn/certifications/azure-ai-fundamentals/) (siehe auch [Microsoft Virtual Training Days](https://www.microsoft.com/en-us/trainingdays))
* [Azure AI Engineer Associate](https://docs.microsoft.com/en-us/learn/certifications/azure-ai-engineer/)
* [Azure Data Scientist Associate](https://docs.microsoft.com/en-us/learn/certifications/azure-data-scientist/)

In der Azure Dokumentation findest du auch Lernpfade zum Erwerb der für die Zertifizierung erforderlichen Fähigkeiten.
