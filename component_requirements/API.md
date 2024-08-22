# ImageScrappingService API

This document outlines the API endpoints for the `ImageScrappingService`. The API is built using FastAPI, providing endpoints to retrieve images and data based on various criteria. The following endpoints are available:

## Endpoints

### 1. **`GET /random`**

   - **Description**: This endpoint returns a random image from the database, including the associated metadata (e.g., region, area, year, species, etc.).
   - **Response**:
     - **Status Code**: `200 OK`
     - **Content-Type**: `application/json`
     - **Response Body**:
       ```json
       {
         "region": "RegionName",
         "area": "AreaName",
         "year": 2023,
         "code": "ABC123",
         "species": "SpeciesName",
         "img_url": "https://example.com/path/to/image.jpg"
       }
       ```

   - **Example Request**:
     ```
     GET /random
     ```

   - **Example Response**:
     ```json
     {
       "region": "Región de Magallanes",
       "area": "Torres del Paine",
       "year": 2022,
       "code": "XYZ789",
       "species": "Guanaco",
       "img_url": "https://example.com/images/guanaco.jpg"
     }
     ```

### 2. **`GET /images`**

   - **Description**: This endpoint allows users to query for specific images based on various parameters such as species, region, area, year, and more.
   - **Query Parameters**:
     - `region`: (Optional) The region to filter by (e.g., `Región de Magallanes`).
     - `area`: (Optional) The area within the region (e.g., `Torres del Paine`).
     - `year`: (Optional) The year to filter by (e.g., `2022`).
     - `species`: (Optional) The species to filter by (e.g., `Guanaco`).
     - `code`: (Optional) The specific code to filter by (e.g., `XYZ789`).

   - **Response**:
     - **Status Code**: `200 OK`
     - **Content-Type**: `application/json`
     - **Response Body**: A list of images and their associated metadata matching the query parameters.
       ```json
       [
         {
           "region": "RegionName",
           "area": "AreaName",
           "year": 2023,
           "code": "ABC123",
           "species": "SpeciesName",
           "img_url": "https://example.com/path/to/image.jpg"
         },
         ...
       ]
       ```

   - **Example Request**:
     ```
     GET /images?region=Región+de+Magallanes&area=Torres+del+Paine&species=Guanaco
     ```

   - **Example Response**:
     ```json
     [
       {
         "region": "Región de Magallanes",
         "area": "Torres del Paine",
         "year": 2022,
         "code": "XYZ789",
         "species": "Guanaco",
         "img_url": "https://example.com/images/guanaco.jpg"
       },
       {
         "region": "Región de Magallanes",
         "area": "Torres del Paine",
         "year": 2021,
         "code": "ABC123",
         "species": "Guanaco",
         "img_url": "https://example.com/images/guanaco_2021.jpg"
       }
     ]
     ```

## Error Handling

### **Common Errors**

- **`400 Bad Request`**: Returned if the query parameters are invalid.
- **`404 Not Found`**: Returned if no images are found matching the query parameters.
- **`500 Internal Server Error`**: Returned if there is an issue processing the request on the server side.

### **Error Response Example**:
   ```json
   {
     "detail": "No images found for the specified query parameters."
   }
   ```

## Implementation Notes

- **Pagination**: You may want to implement pagination for the `/images` endpoint to handle large datasets efficiently.
- **Caching**: Implement caching strategies to optimize performance, especially for frequently accessed queries.
- **Security**: Consider adding authentication and authorization if needed for specific endpoints.
- **Logging**: Implement logging for better monitoring and debugging of API requests.
