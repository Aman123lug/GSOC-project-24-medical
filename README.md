# Analytics Edge Ecosystem Workloads Project

## Abstract
Edge Computing has become immensely beneficial for running analytics at the edge, thereby reducing the amount of data sent to servers and storage at the core or cloud, which in turn increases latency. The Analytics Edge Ecosystem Workloads project aims to bring about a digital transformation strategy by focusing on cloud-native containerization to improve business analytics.

In this project, AI/ML and Generative AI (GenAI) workloads will be developed to address the challenges faced in the healthcare/medical industry. The development of this project includes the open-source deployment of AI/ML and GenAI workloads as well as deployments on Kubernetes using Rancher by SUSE, with openSUSE Leap as the base layer operating system. Additionally, K3s will be utilized as a lightweight Kubernetes designed for the Edge.

The project implementation will involve several tech stacks such as DataOps to manage data pipelines, MLOps, and LLMOps to manage ML and LLM pipelines, as well as Platform Engineering and ITOps to manage platforms.

## Problem Statement
**Vertical: Medical/Healthcare**

Many individuals face various challenges when dealing with their prescription medications. These challenges include unfamiliar medical terminology, misinterpreted prescriptions, unclear dosage and usage instructions, missed expiration dates, unexpected side effects, and drug interactions. These issues can lead to overdosing, accidents, and even death.

## Proposed Solution
This project aims to leverage machine learning and generative AI to help address some of the challenges that patients and doctors face with medical prescriptions. This will involve the four features outlined below:

1. **Medicine Scanner:** Scans medicine to inform about the medicine, dosage, side effects, and date of expiry.
2. **Medical Report Scanner:** Scans and simplifies test reports to help patients understand their medical reports.
3. **Prescription Scanner:** Scans and interprets handwritten prescriptions to help patients, pharmacists, and others properly interpret a doctor’s instructions.
4. **Prescription Generator:** Enables doctors to more quickly and easily generate accurate, understandable prescriptions.

## Detailed Explanation
### Data Extraction and Transformation
- **Data Sources:** Medical data from UCIML repositories, Kaggle, and other trusted sources.
- **Data Processing:** Feature engineering and data cleaning will be performed after extraction.
- **Data Storage:** Data will be converted to embeddings and stored in a vector database for Retrieval-Augmented Generation (RAG).

### Retrieval-Augmented Generation (RAG)
- **Model Utilization:** Leverage open-source Large Language Models (LLMs) to power RAG.
- **Model Fine-tuning:** Fine-tune the model for the medication use case.

### User Interface and LLMOps
- **User Interface:** Create a user-friendly interface.
- **LLMOps Pipeline:** Define an end-to-end LLMOps pipeline to enable additional training and fine-tuning.

## User Friendly Interface
![alt text](image-2.png)

## Ask About your Medicines
![alt text](image-1.png)


This project encompasses GenAI, MLOps, and LLMOps tech stacks.

## How to Setup the Project
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/analytics-edge-ecosystem.git
   cd analytics-edge-ecosystem

## Set API keys
2. **Setting all required API keys**
- **Create a .env file**
```
HUGGINGFACEHUB_API_TOKEN="API key"
PINECONE_API_KEY = "API key"
PINECONE_INDEX = "medcial-rag-chatbot"
GENAI_API_KEY = "Gemini key"
GROQ_API_KEY = "Lama3-7b"
```
### Add your APi keys

## Create Virtual Environment
3. **Install all the required packages**
```
pip install -r requirements.txt
```

## Run Command
4. **Run app.py**
```
steamlit run app.py
```



## Acknowledgments
- Thanks to the open-source community for providing various tools and frameworks.
- Special thanks to UCIML, Kaggle, and other trusted sources for providing the datasets.
- Gratitude to SUSE, openSUSE Leap, and Rancher for their powerful tools enabling Kubernetes deployments.

## Future Work
The project aims to continually improve and expand its features. Future work includes:
- **Enhanced Model Training:** Continuously improve the accuracy and efficiency of AI/ML models.
- **Integration with More Data Sources:** Expand the data sources to include more comprehensive and diverse medical data.
- **User Feedback Mechanism:** Implement a feedback system for users to report issues and suggest improvements.
- **Mobile Application:** Develop a mobile application to make the solution more accessible to patients and healthcare providers.

## Data Sources
- [Government medical data source](https://medlineplus.gov)
- [Advance medical data Gov source](https://www.nlm.nih.gov/databases) -> Licensed required
- [Medical Encyclopedia](https://medlineplus.gov/encyclopedia.html)
- [Journal lists](https://www.ncbi.nlm.nih.gov/pmc/journals/)



### [Steps]
- Initial project setup
- Implementation of Medicine Scanner, Medical Report Scanner, Prescription Scanner, and Prescription Generator
- Deployment on Kubernetes using Rancher and K3s
- Development of LLMOps pipelines

### [1.0.0] - YYYY-MM-DD
- Initial release

## Authors
- [Aman Kumar](https://github.com/Aman123lug) - Initial work

## Support
If you need support, please open an issue on the [GitHub repository](https://github.com/yourusername/analytics-edge-ecosystem/issues).

---

This README file provides a comprehensive overview of the project, including setup instructions, contribution guidelines, license information, acknowledgments, future work, references, FAQs, code of conduct, changelog, and support details. Make sure to update the placeholders with actual information and links specific to your project.
