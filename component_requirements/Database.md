# Database Schema

This document describes the database schema that supports the `ImageScrappingService`. The database is managed using SQLAlchemy as the ORM (Object-Relational Mapping) framework and follows a model-based approach to support CRUD (Create, Read, Update, Delete) operations.

## Database Structure

### **Table: RegionAreaYear**

This table is the primary table for storing data points based on the combination of Region, Area, Year, and additional parameters. It is structured as follows:

| Column Name | Data Type | Description                    |
|-------------|------------|--------------------------------|
| `id`        | `Integer`  | Primary Key (Auto-incremented) |
| `Region`    | `String`   | Represents the geographical region |
| `Area`      | `String`   | Represents the specific area within the region |
| `Year`      | `Integer`  | Year associated with the data point |
| `Code`      | `String`   | Code related to the specific entry |
| `Link`      | `String`   | Link to the associated data (if applicable) |

- **Primary Key**: `id`

### **Table: Img**

This table stores images fetched by the `ImageScrappingService`, along with their metadata and foreign key relationships.

| Column Name | Data Type   | Description                                |
|-------------|-------------|--------------------------------------------|
| `id`        | `Integer`   | Primary Key (Auto-incremented)             |
| `Fk_Code`   | `String`    | Foreign Key referencing `Code` from `RegionAreaYear` |
| `Animal`    | `String`    | Describes the animal or subject in the image (if applicable) |
| `URN`       | `String`    | Unique Resource Name or identifier for the image |
| `img`       | `Bytea`     | Binary data of the image                   |
| `year`      | `Integer`   | Year associated with the image             |

- **Foreign Key**: `Fk_Code` references `Code` in the `RegionAreaYear` table.

## SQLAlchemy Framework

### **Model**

The database structure will be modeled using SQLAlchemy, ensuring that the relationships between tables are defined, and constraints such as primary keys and foreign keys are enforced. The models will be defined in Python and mapped to the respective tables.

### **CRUD Operations**

The following CRUD operations will be implemented:

- **Create**: Insert new entries into both `RegionAreaYear` and `Img` tables.
- **Read**: Query data based on specific Region, Area, Year, or image attributes.
- **Update**: Modify existing entries in the database, particularly for updating image metadata or adding new regions/areas/years.
- **Delete**: Remove entries from the tables based on specific conditions or identifiers.
