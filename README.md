# Birdly
Birdly is a bird image classifier capable of identifying up to 1000 species of Indian birds.

## Training Scripts
Birdly was trained using Google's Cloud TPUs, available on Kaggle. Due to the 9-hour time limit on Kaggle Notebooks, the training was divided into phases, with each phase consisting of 12 to 24 epochs. The notebooks for these phases can be found in the `training-scripts` directory.

> [!NOTE]
> All model and data loading variables are set according to their usage on Kaggle.

## TFRecords
To fully utilize the power of TPUs, the dataset was converted into TFRecords. For easier data management, this conversion was done in batches of 250 classes. The notebooks for these conversions can be found in the `tfrecords` directory.

## Model and List of Birds
Due to the large size of the model, it is not included in this repository. However, it can be found in the [`birdly-backend`](https://github.com/ArjunBasandrai/birdly-backend/tree/main/model) repository, along with the list of birds it can identify.

## Data Scraping
The dataset for this project was scraped from the Macaulay Library over a period of 2 months, collecting an estimated total of 1.2 million images. The scraping scripts can be found in the `data-scraping-scripts` directory.
