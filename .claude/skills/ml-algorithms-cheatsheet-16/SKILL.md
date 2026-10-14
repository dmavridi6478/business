---
name: ml-algorithms-cheatsheet-16
description: A 16-algorithm machine-learning cheatsheet (linear and logistic regression, decision tree, random forest, gradient boosting, SVM, KNN, naive Bayes, k-means, hierarchical clustering, PCA, MLP, CNN, RNN, transformer, autoencoder, DBSCAN) with type, best use, key formula, assumptions, pros, cons, when not to use and a real-world example, plus the entries that are loose or wrong and a selection order. Use when the user asks which algorithm fits a problem, wants a quick comparison, or wants to check a claim from this cheatsheet.
---

# Machine Learning Algorithms cheatsheet (16 rows)

Source: one infographic attached in chat, "Cheatsheet: Machine Learning Algorithms", with a creator watermark across the table. Read 14 October 2026. Transcribed row by row; typos on the slide are corrected here ("noise veduction" is "noise reduction").

| Algorithm | Type | Best use | Key formula or logic | Assumptions | Pros | Cons | When not to use | Example |
|---|---|---|---|---|---|---|---|---|
| Linear Regression | Supervised | Predicting continuous values | Y = b0 + b1X1 + b2X2 + ... | Linearity, independence | Simple, interpretable, fast | Sensitive to outliers, non-linear limits | Data with strong non-linearity | House price prediction |
| Logistic Regression | Supervised | Binary classification | P = 1 / (1 + e^-(b0 + b1X + ...)) | Log-odds linearity | Probabilistic, interpretable | Weak with non-linear boundaries | Data is highly non-linear | Spam detection |
| Decision Tree | Supervised | Classification and regression | Recursive binary split | None | Easy to interpret | Overfitting, unstable | Noisy or complex datasets | Loan default prediction |
| Random Forest | Supervised | Ensemble accuracy | Bagging plus averaging trees | Tree independence | High accuracy, robust | Slower, less interpretable | Need real-time results | Fraud detection |
| Gradient Boosting | Supervised | High-performance modeling | Additive trees minimizing loss | Sequential dependency | State-of-the-art accuracy | Overfitting, needs tuning | When interpretability matters | Credit scoring |
| SVM | Supervised | Max-margin classification | Maximize margin using kernel trick | Separability, scaling | Works in high dimensions | Slow on large data | Large noisy datasets | Facial recognition |
| KNN | Supervised | Few-shot classification | Distance-based majority vote | Feature scaling | Simple, no training phase | Slow, noise sensitive | High-dimensional noisy data | Recommender systems |
| Naive Bayes | Supervised | Text classification | Bayes theorem plus feature independence | Independent features | Fast, good with text data | Fails with correlated features | Feature dependency present | Sentiment analysis |
| K-Means | Unsupervised | Customer segmentation | Minimize intra-cluster distance | Spherical, equal clusters | Fast, easy to implement | Needs K, sensitive to scale | Non-spherical data | Customer segmentation |
| Hierarchical Clustering | Unsupervised | Data structure understanding | Nested dendrogram | Distance metric | No need for K, visual | Memory and compute intensive | Very large datasets | Gene expression analysis |
| PCA | Dimensionality reduction | Reducing feature dimensionality | Eigenvectors of covariance matrix | Large variance important | Noise reduction, speed-up | Hard to interpret | All features are important | Image compression |
| Neural Networks (MLP) | Supervised | Complex pattern modeling | Weighted sums plus activation functions | Enough data, scaling | Non-linear learning power | Needs large data and tuning | Small data, low compute | Image classification |
| CNN | Supervised | Image, video, spatial data | Convolution plus pooling layers | Grid-like spatial data | Excellent for images | High resource demand | Sequence or text data | Self-driving vision |
| RNN | Supervised | Sequence modeling | Feedback loops over time | Sequential structure | Time-series and text ready | Vanishing gradient | Long sequences | Stock prediction |
| Transformer (BERT, GPT) | Supervised or self-supervised | NLP tasks, chat, translation | Attention mechanism plus position encoding | Large training data | Long context, fast | Heavy compute, large model | Small projects | ChatGPT, translation tools |
| Autoencoders | Unsupervised | Compression and anomaly detection | Encoder-decoder plus reconstruction loss | Symmetric network | Effective denoising | Can overfit, black-box | When no compression needed | Fraud detection |
| DBSCAN | Unsupervised | Arbitrary shape clustering | Density-based region growing | Cluster density | Noise tolerant, shape-flexible | Fails on varying density | Sparse high-dimensional data | Geo-spatial clustering |

## Where the sheet is loose or wrong (my reading, standard textbook points)

- **Random Forest, "Tree independence":** not an assumption of the method. Bagging and random feature selection make the trees less correlated; they are not independent. [Likely]
- **KNN, "Few-shot classification":** KNN is a lazy learner that needs labelled neighbours, not few-shot learning in the modern sense. [Likely]
- **Naive Bayes, "Fails with correlated features":** it can still classify well, but its probability estimates become poor. [Likely]
- **Transformer, "Long context, fast":** self-attention cost grows with the square of the sequence length, and the model is heavy. "Fast" holds for parallel training, not for long inputs. [Likely]
- **RNN, "Stock prediction":** a common demo, not a reliable application. Do not read it as a recommendation.
- **CNN and MLP, "Supervised":** both are also trained in self-supervised and unsupervised settings.
- **DBSCAN, "Fails on varying density":** correct. Add that results depend heavily on the radius and minimum-points settings.
- A cheatsheet row cannot carry the data size, noise level or cost of an error. Those decide the choice more than the row does.

## Selection order (mine, a common starting practice, not from the sheet)

1. Start with a simple baseline: linear or logistic regression. If it is good enough, stop.
2. Tabular data: try gradient boosting or random forest next. Use a held-out test set and cross-validation.
3. Images or video: CNN. Text or sequences: a transformer. Sequence data on a small budget: consider simpler models first.
4. No labels: k-means or hierarchical clustering for round groups, DBSCAN for odd shapes and noise.
5. Too many features: PCA first, then the model.
6. When the decision affects people (credit, hiring, health), prefer a model you can explain, and measure errors by group.

## Prompt (copy and paste)

```
I have [describe the data: rows, columns, types, missing values] and I want to [predict X / group Y / detect Z]. Using the ml-algorithms-cheatsheet-16 skill, name the baseline I should try first, one stronger option, and one I should avoid, each with its assumption that my data might break. Say what test I should run to check each assumption. Do not recommend a deep network unless my data size justifies it.
```

Command: `/ml-algo-pick <your problem, data size, how much you must explain the result>`.
