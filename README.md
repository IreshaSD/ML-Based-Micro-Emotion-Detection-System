# ML-Based-Micro-Emotion-Detection-System
### Micro-Expression Detection System Based on Machine Learning," focuses on automatically detecting brief and subtle facial expressions that reveal hidden emotions 

Micro-expressions are brief, involuntary facial expressions, lasting between 0.04 and 0.2 seconds, often too subtle for the naked eye to detect. These fleeting expressions are crucial in high-stakes scenarios, such as criminal interrogations, security screenings, and psychological evaluations, where individuals might suppress their true emotions.

## Feature Extraction Techniques
Local Binary Pattern on Three Orthogonal Planes (LBP-TOP): A spatiotemporal method analyzing video frames.
Custom Approach: Extracting features from onset, apex, and offset micro-expression frames by calculating landmark coordinate differences.

## Classification Method
I utilized a Support Vector Machine (SVM) model for classification, chosen for its proven performance in prior research. My findings demonstrated that combining temporal and static features with a machine learning algorithm yields moderate accuracy in automatic micro-expression recognition.

## Results
Using the CASME II dataset, which includes both temporal and static data samples, I implemented two recognition schemes:
#### 1. Static-only method: Achieved an accuracy of 65.38%
#### 2. Temporal method: Achieved an accuracy of 52.17%
While these results highlight areas for improvement, they underscore the potential for future research to enhance accuracy and reliability.

## Conclusion
This project was an invaluable learning experience, reinforcing my enthusiasm for machine learning and its applications. I continue to explore and work on various machine learning and deep learning projects, which you can find on my profile.
