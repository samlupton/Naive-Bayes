# README

    ## Naive Bayes Classifier for Sentiment Analysis

    This project implements a simple Naive Bayes classifier to determine whether a given message is "nice" or "mean." The classifier is trained on labeled datasets of nice and mean messages and evaluates its performance on test datasets.

    ### Features

    - **Training**: The model learns word frequencies from `nice_messages.txt` and `mean_messages.txt`.
    - **Prediction**: Classifies messages as "nice" or "mean" using the Naive Bayes algorithm.
    - **Evaluation**: Calculates the accuracy of the model on test datasets (`test_nice_messages.txt` and `test_mean_messages.txt`).

    ### How It Works

    1. **Preprocessing**: 
        - Messages are converted to lowercase.
        - Punctuation (`!` and `.`) is removed.
        - Messages are split into words.

    2. **Training**:
        - Word frequencies are calculated for both "nice" and "mean" messages.
        - Prior probabilities for "nice" and "mean" messages are computed.

    3. **Prediction**:
        - For a given message, the likelihood of it being "nice" or "mean" is calculated using word frequencies and prior probabilities.
        - The message is classified based on the higher probability.

    4. **Evaluation**:
        - The model's accuracy is tested on separate datasets for "nice" and "mean" messages.

    ### File Structure

    - `naive_bayes.py`: Main script containing the implementation.
    - `nice_messages.txt`: Training data for nice messages.
    - `mean_messages.txt`: Training data for mean messages.
    - `test_nice_messages.txt`: Test data for nice messages.
    - `test_mean_messages.txt`: Test data for mean messages.

    ### Usage

    1. Clone the repository:
        ```bash
        git clone https://github.com/your-username/naive-bayes-classifier.git
        cd naive-bayes-classifier
        ```

    2. Prepare your training and test datasets:
        - Place your `nice_messages.txt`, `mean_messages.txt`, `test_nice_messages.txt`, and `test_mean_messages.txt` files in the same directory as `naive_bayes.py`.

    3. Run the script:
        ```bash
        python naive_bayes.py
        ```

    4. View the results:
        - The script will output the accuracy of the model on the test datasets.

    ### Example Output
