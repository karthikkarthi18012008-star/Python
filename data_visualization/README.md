# Missing Value Handling in Pandas

## 📌 Concepts Covered

* Loading the Titanic dataset using `seaborn`
* Viewing the first few rows with `head()`
* Detecting missing values using `isnull().sum()`
* Checking dataset shape with `shape`
* Removing missing values using `dropna()`
* Dropping rows vs. dropping columns (`axis=0` and `axis=1`)
* Mean Imputation for normally distributed numerical data
* Median Imputation for numerical data with outliers
* Mode Imputation for categorical features
* Visualizing data distribution using `sns.histplot()` with KDE

## 📚 Learning Outcomes

* Understand how to identify missing values in a dataset.
* Learn different techniques to handle missing data.
* Know when to use **Mean**, **Median**, and **Mode** imputation.
* Differentiate between dropping rows and dropping columns containing missing values.
* Visualize feature distribution before choosing an imputation method.
* Prepare datasets for data analysis and machine learning preprocessing.
# Handling Imbalanced Dataset - Upsampling & Downsampling

## 📌 Concepts Covered

* Creating an imbalanced dataset using **NumPy** and **Pandas**
* Generating data with `np.random.normal()`
* Setting a random seed using `np.random.seed()`
* Creating majority and minority classes
* Combining DataFrames using `pd.concat()`
* Separating classes based on the target variable
* Random **Upsampling** using `sklearn.utils.resample()`
* Random **Downsampling** using `sklearn.utils.resample()`
* Sampling with and without replacement (`replace=True` / `replace=False`)
* Shuffling the dataset using `sample()`
* Resetting index with `reset_index()`
* Checking class distribution using `value_counts()`
* Comparing Upsampling and Downsampling techniques

## 📚 Learning Outcomes

* Understand what an imbalanced dataset is and why it is a problem in machine learning.
* Learn how to create a synthetic imbalanced dataset for experimentation.
* Balance datasets using **Random Upsampling** by increasing minority class samples.
* Balance datasets using **Random Downsampling** by reducing majority class samples.
* Understand the purpose of `replace`, `n_samples`, and `random_state` in `resample()`.
* Learn when to use Upsampling and Downsampling based on dataset size and requirements.
* Compare the advantages, disadvantages, and use cases of both balancing techniques.
* Prepare datasets for building more reliable and unbiased machine learning models.

