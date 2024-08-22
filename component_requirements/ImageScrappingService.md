# ImageScrappingService

The `ImageScrappingService` is responsible for scraping images based on specific points defined by Region, Area, and Year. The service operates through a series of components that work together to collect and cache data, scrape drive links, and fetch images. Below is an explanation of each component and its requirements.

## Components

### 1. **Available Data Scrapper**
   - **Description**: This component is responsible for scrapping available data related to Region, Area, and Year. It gathers data and structures it into an area tree.
   - **Input**: 
     - `nothing`: The scrapper initiates without any input parameters.
   - **Output**:
      - `area tree (JSON)`: The result is an area tree which will be stored in JSON format. The JSON will include the following fields:
        - `Region`: The region name.
        - `Area`: The area name.
        - `Year`: The year of the data.
        - `Code`: The grid code.
        - `Link`: The link to the drive containing the images.

### 2. **Cache System (Optional)**
   - **Description**: The cache system checks for new data points that have been added or updated. It compares the local area tree with the newly scrapped data.
   - **Input**: 
     - `area tree (local + new)`: The component takes in the local area tree along with the newly obtained area tree from the scrapper.
   - **Output**:
     - `list[new points]`: It outputs a list of new data points (combinations of Region, Area, and Year) that have been identified, which need to be processed further.

### 3. **Fetch Images with Drive API**
   - **Description**: The final component fetches the images from the drive using the API, based on the scraped links.
   - **Input**: 
     - `link drive`: The drive links obtained from the previous component.
   - **Output**:
    - `JSON`: The output is a JSON list of dictionaries, each containing the following fields:
      - `Code`: The grid code.
      - `Species`: The species name.
      - `Image`: The image file in binary format.
      - `Date`: The date of the image (Chile).
