# 🚇 Delhi-NCR Transit Analytics & Route Optimization

## 📌 Project Overview
An end-to-end Data Analytics project analyzing commute patterns, transit bottlenecks, and peak-hour delays across the Delhi-NCR (Noida-Faridabad) route. The primary objective of this project is to process raw transit data and extract actionable business insights to optimize commuter efficiency.

## 🛠️ Tech Stack Used
- **Data Engineering:** Python (Pandas, NumPy)
- **Database & Analytics:** MySQL (CTEs, Aggregations, Time-Series Analysis)
- **Data Visualization:** Power BI (KPIs, Trend Analysis, Interactive Dashboards)

## 📊 Key Business Insights
1. **Peak-Hour Bottlenecks:** Identified critical delay spikes during morning (08:00 - 10:00) and evening (18:00+) rush hours using SQL time-series analysis.
2. **Busiest Transit Hubs:** Pinpointed Sector-52 Noida and Botanical Garden as the highest-volume boarding stations (averaging 1,200+ trips each).
3. **Transport Mode Efficiency:** Evaluated average delays across Uber Shuttle, Delhi Metro, and City Bus to determine the most reliable transit modes for daily commuters.

## 🏗️ Project Pipeline
1. **Phase 1: Data Engineering (Python)**
   - Engineered an automated pipeline to generate a simulated dataset (`ncr_transit_data.csv`) of 5,000 commuter trips.
2. **Phase 2: Data Analytics (MySQL)**
   - Designed a relational database structure and executed advanced SQL queries (`queries.sql`) to aggregate delays and uncover traffic patterns.
3. **Phase 3: Data Visualization (Power BI)**
   - Developed an interactive corporate dashboard featuring KPI cards, donut charts, and clustered bar charts to visually communicate data-driven insights.

## 📂 Repository Structure
- `generate_data.py`: Python script used to process and format the raw transit dataset.
- `ncr_transit_data.csv`: The core dataset containing trip origins, destinations, transport modes, and delays.
- `queries.sql`: MySQL queries used for extracting business metrics and route optimizations.
- `Dashboard.png`: High-resolution screenshot of the final Power BI dashboard.

*(Note: Please open `Dashboard.png` to view the final visualizations of the extracted data).*

---
### 👨‍💻 Author
**Pintoo Jha**  
*Data Analyst | Master of Computer Applications (MCA) Candidate*
