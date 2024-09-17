# Birdly Data Scrapers
The scraping procedure consists of 3 phases: Retrieval, Link Scraping, and Data Scraping.

## Retrieval
In this phase, the names and their corresponding `eBird Taxon Codes` were retrieved for 1,250 birds of India. The names and codes were then split into batches and stored under the `batches` directory.

## Link Scraping
This phase utilizes the `selenium` library to visit the `Media` pages for all the birds in each batch. It scrolls down and clicks the `Load More` button until `1000` images are loaded. The links of all the loaded images are then stored in the `image_links` directory, with each file named after the bird.

## Data Scraping
This phase crawls all the links in the files under the `image_links` directory and stores the images in the `training_data` directory. Each bird's images are stored in their own subdirectory, named after the bird.
