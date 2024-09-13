# Online Used Car Sales System - Star Schema Design
A system to manage car sales, inventory, and customer data using a star schema model. Optimized for data warehousing and reporting, featuring SQL scripts for querying and analysis. Includes fact and dimension tables for efficient reporting on transactions and inventory.

This repository contains the data model and schema design for an Online Used Car Sales System, leveraging a Star Schema for efficient data organization and retrieval. The design focuses on optimizing data analysis and reporting for a used car e-commerce platform, supporting detailed and aggregated queries.

Overview
In this project, we develop a Star Schema for a used car sales system that enables flexible reporting and analysis. This design helps organize data in a structured way to simplify queries regarding sales transactions, customers, and inventory, providing both detail-level and high-level reporting capabilities.

Key Components:
Fact Tables: These tables contain transactional data, such as sales records and financial information.
Dimension Tables: These tables store the descriptive data, such as car models, sellers, customers, and locations.

Star Schema Entities:
Fact Car Invoice: Records all car sales, including information on seller, buyer, and vehicle sold.
Dim Product: Stores data related to vehicles, including brand, model, and other relevant details.
Dim Seller: Contains seller details like name, store, and contact information.
Dim Customer: Stores customer details, facilitating segmentation and detailed analysis.
Dim City: Provides information on cities for geographical analysis.
Schema Design
The Star Schema is designed to centralize transactional data while linking it to descriptive dimensions for easier querying. This design enables fast aggregation of data for sales reporting, product performance, and customer insights.

Fact Tables
fact_car_invoice: Stores car sale transactions.
fact_application: Records application details linked to car sales.
Dimension Tables
dim_product: Contains detailed information on the cars available for sale.
dim_seller: Details about the sellers.
dim_customer: Customer-related data, essential for personalized marketing and service.
dim_city: Used for regional and geographical analysis.
ERD (Entity-Relationship Diagram)
The ERD visualizes how the fact and dimension tables relate to one another, enabling clear and efficient data retrieval for reporting and analysis.
