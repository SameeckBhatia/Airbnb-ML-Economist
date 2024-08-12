# Airbnb ML Economist

## Research Question

"Economic Drivers of Airbnb Pricing in Los Angeles: An Examination of Crime, Demographics, and Geography"

## Inside Airbnb

| Field                            | Description                                                             |
|----------------------------------|-------------------------------------------------------------------------|
| `id`                             | Unique identifier for the listing                                       |
| `name`                           | The name of the listing                                                 |
| `host_id`                        | Unique identifier for the host                                          |
| `host_name`                      | The name of the host                                                    |
| `neighbourhood_group`            | The neighbourhood group as defined by open or public digital shapefiles |
| `neighbourhood`                  | The neighbourhood as defined by open or public digital shapefiles       |
| `latitude`                       | Uses the WGS84 projection for latitude and longitude                    |
| `longitude`                      | Uses the WGS84 projection for latitude and longitude                    |
| `room_type`                      | The type of room being offered                                          |
| `price`                          | Daily price in local currency                                           |
| `minimum_nights`                 | Minimum number of nights required for a stay in the listing             |
| `number_of_reviews`              | The number of reviews the listing has                                   |
| `last_review`                    | The date of the last review                                             |
| `calculated_host_listings_count` | The number of listings the host has                                     |
| `availability_365`               | The availability of the listing 365 days in the future                  |
| `number_of_reviews_ltm`          | The number of reviews the listing has received in the last 12 months    |
| `license`                        | The license number associated with the listing, if applicable           |


## United States Census

### File: census.csv

| Field           | Description                                              |
|-----------------|----------------------------------------------------------|
| `zip_code`      | The postal code representing a specific geographic area  |
| `population`    | The total number of people living in the ZIP code        |
| `median_income` | The median household income (in US dollars)              |
| `num_bachelors` | The number of people with a Bachelor's degree            |
| `num_masters`   | The number of people with a Master's degree              |
| `num_doctorate` | The number of people with a Doctorate degree             |
| `num_white`     | The number of people identifying as 'White'              |
| `pct_tertiary`  | The percentage of the population with tertiary education |
| `pct_white`     | The percentage of the population identifying as 'White'  |

## TripAdvisor

### File: attractions.csv

| Field         | Description                              |
|---------------|------------------------------------------|
| `attraction`  | Name of the attraction                   |
| `num_reviews` | Number of reviews received by attraction |
| `latitude`    | Latitude coordinate of the attraction    |
| `longitude`   | Longitude coordinate of the attraction   |

## City of Los Angeles

### File: crime.csv

| Field             | Description                                       |
|-------------------|---------------------------------------------------|
| `record_num`      | Unique identifier for each crime record           |
| `date`            | Date when the crime occurred                      |
| `time`            | Time when the crime occurred                      |
| `crime_code`      | Code representing the type of crime               |
| `crime_code_desc` | Description of the crime associated with the code |
| `victim_sex`      | Sex of the victim                                 |
| `victim_descent`  | Ethnic descent of the victim                      |
| `latitude`        | Latitude coordinate of the crime location         |
| `longitude`       | Longitude coordinate of the crime location        |
