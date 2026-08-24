        # Finance-Logistics-100-Python-Projects

        100 progressively difficult Python projects in **finance, business
        analytics, logistics, supply-chain, operations research, and network
        engineering** — built in the spirit of `Mini-Bio-Python-Projects`,
        retargeted at computational business engineering.

        The goal is not to "learn Python." The goal is to learn how to use
        Python to **understand, diagnose, model, optimize, and engineer real
        business systems** — moving from a single script to a modular
        application, to a data pipeline, to an optimization system, to an
        intelligent decision-support system.

        ## Learning Philosophy

        Each project answers a real business question. Complexity is always
        isolated inside modules — no 1,000-line `main.py`, no artificially
        inflated beginner projects. Architecture scales with difficulty:
        Phase 1 projects are `README.md` + `main.py`; Phase 8 projects have
        full `config/ data/ src/ tests/ notebooks/ models/ outputs/` trees.

        ## Project Map

        - **Phase 1** (`phase1_python_business_foundations/`) — projects 001–015
- **Phase 2** (`phase2_business_logic/`) — projects 016–030
- **Phase 3** (`phase3_data_structures_business_systems/`) — projects 031–045
- **Phase 4** (`phase4_file_handling_real_data/`) — projects 046–060
- **Phase 5** (`phase5_numpy_simulation/`) — projects 061–075
- **Phase 6** (`phase6_pandas_business_analytics/`) — projects 076–085
- **Phase 7** (`phase7_visualization_network_analysis/`) — projects 086–092
- **Phase 8** (`phase8_machine_learning_optimization/`) — projects 093–100

        ## Phase Structure

        | Phase | Focus | Projects |
        |---|---|---|
        | 1 | Python Business Foundations | 001–015 |
        | 2 | Business Logic & Decision Systems | 016–030 |
        | 3 | Data Structures & Business Systems | 031–045 |
        | 4 | File Handling & Real Business Data | 046–060 |
        | 5 | NumPy, Simulation & Quantitative Computing | 061–075 |
        | 6 | Pandas & Business Intelligence | 076–085 |
        | 7 | Visualization, Graphs & Network Analysis | 086–092 |
        | 8 | Machine Learning, Optimization & Integrated Systems | 093–100 |

        ## Technology Progression

        Python → data structures → file handling → NumPy → Pandas →
        Matplotlib/Plotly → SciPy → NetworkX → scikit-learn → OR-Tools →
        integrated systems. See `roadmap.md` for the full skill map.

        ## Domain Roadmaps

        - **Finance:** cash flow, revenue, expenses, margins, pricing, loans,
          investments, risk, portfolio analysis, working capital,
          profitability, financial forecasting.
        - **Logistics:** inventory, warehouses, procurement, suppliers,
          transportation, routing, distributors, retailers, delivery,
          lead time, capacity, stockouts, demand.
        - **Operations Research:** linear/integer programming, transportation
          optimization, assignment, facility location, routing, resource
          allocation, scheduling, network flow.
        - **Network Analysis:** graph modeling, shortest paths, bottlenecks,
          centrality, dependency, resilience, flow networks.
        - **Machine Learning:** demand forecasting, delay prediction,
          supplier risk, inventory prediction, payment risk, cost
          prediction, anomaly detection, clustering.

        ## Installation

        ```bash
        git clone <this-repo-url>
        cd Finance-Logistics-100-Python-Projects
        python -m venv .venv && source .venv/bin/activate   # or .venv\Scripts\activate on Windows
        pip install -r requirements.txt   # root dev tooling (pytest, etc.)
        ```

        Each project also has its own `requirements.txt` with only the
        dependencies it actually needs — install those inside the project
        folder before running it.

        ## Usage

        ```bash
        cd phase1_python_business_foundations/project_001_personal_cash_flow_analyzer
        pip install -r requirements.txt
        python main.py
        ```

        ## Generating / Regenerating the Repository

        The full folder structure is produced by `file_generator.py`, driven
        by the metadata in `projects_data.py`. It is idempotent and will
        never overwrite an existing file unless you pass `--force`:

        ```bash
        python file_generator.py --root .
        python file_generator.py --root . --only 45     # regenerate one project
        python file_generator.py --root . --dry-run       # preview, write nothing
        ```

        ## Contribution Guidelines

        See `CONTRIBUTING.md`.

        ## Project Difficulty Levels

        - **Beginner** — 001–030
        - **Intermediate** — 031–060
        - **Advanced** — 061–085
        - **Professional** — 086–100

        ## Full Project Index

        | Project | Domain | Difficulty | Main Technology |
| ------- | ------ | ---------- | --------------- |
| 001. Personal Cash Flow Analyzer | Finance | Beginner | Python (stdlib) |
| 002. Simple Interest Calculator | Finance | Beginner | Python (stdlib) |
| 003. Compound Interest Engine | Finance | Beginner | Python (stdlib) |
| 004. Loan EMI Calculator | Finance | Beginner | Python (stdlib) |
| 005. Profit Margin Calculator | Finance | Beginner | Python (stdlib) |
| 006. Break-Even Calculator | Finance | Beginner | Python (stdlib) |
| 007. Revenue Growth Analyzer | Finance | Beginner | Python (stdlib) |
| 008. Expense Categorizer | Finance | Beginner | Python (stdlib) |
| 009. Budget Variance Calculator | Finance | Beginner | Python (stdlib) |
| 010. Invoice Generator | Finance | Beginner | Python (stdlib) |
| 011. Product Pricing Calculator | Finance | Beginner | Python (stdlib) |
| 012. Inventory Value Calculator | Logistics | Beginner | Python (stdlib) |
| 013. Logistics Cost Calculator | Logistics | Beginner | Python (stdlib) |
| 014. Landed Cost Calculator | Logistics | Beginner | Python (stdlib) |
| 015. Small Business Financial Dashboard | Finance | Beginner | pandas |
| 016. Progressive Tax Calculator | Finance | Beginner | Python (stdlib) |
| 017. Investment Return Calculator | Finance | Beginner | Python (stdlib) |
| 018. Loan Amortization Engine | Finance | Beginner | Python (stdlib) |
| 019. Cash Reserve Simulator | Finance | Beginner | Python (stdlib) |
| 020. Supplier Payment Scheduler | Finance | Beginner | Python (stdlib) |
| 021. Customer Credit Limit Checker | Finance | Beginner | Python (stdlib) |
| 022. Stock Reorder Calculator | Logistics | Beginner | Python (stdlib) |
| 023. Safety Stock Calculator | Logistics | Beginner | Python (stdlib) |
| 024. Economic Order Quantity Calculator | Logistics | Beginner | Python (stdlib) |
| 025. Inventory Replenishment Engine | Logistics | Beginner | Python (stdlib) |
| 026. Transportation Cost Estimator | Logistics | Beginner | Python (stdlib) |
| 027. Vehicle Capacity Checker | Logistics | Beginner | Python (stdlib) |
| 028. Delivery Priority Engine | Logistics | Beginner | Python (stdlib) |
| 029. Supplier Risk Scorer | Logistics | Beginner | Python (stdlib) |
| 030. Business Decision Rule Engine | Operations Research | Beginner | Python (stdlib) |
| 031. Customer Ledger | Finance | Intermediate | Python (stdlib) |
| 032. Supplier Ledger | Finance | Intermediate | Python (stdlib) |
| 033. Product Catalog Engine | Logistics | Intermediate | Python (stdlib) |
| 034. Warehouse Inventory Manager | Logistics | Intermediate | Python (stdlib) |
| 035. Multi-Product Order System | Logistics | Intermediate | Python (stdlib) |
| 036. Shipment Tracking System | Logistics | Intermediate | Python (stdlib) |
| 037. Purchase Order Manager | Logistics | Intermediate | Python (stdlib) |
| 038. Sales Order Manager | Finance | Intermediate | Python (stdlib) |
| 039. Multi-Warehouse Stock Allocator | Logistics | Intermediate | Python (stdlib) |
| 040. Distributor Management System | Logistics | Intermediate | Python (stdlib) |
| 041. Retailer Network Manager | Logistics | Intermediate | Python (stdlib) |
| 042. Supplier Performance Database | Logistics | Intermediate | Python (stdlib) |
| 043. Customer Profitability Analyzer | Finance | Intermediate | Python (stdlib) |
| 044. Product Profitability Analyzer | Finance | Intermediate | Python (stdlib) |
| 045. End-to-End Order Lifecycle Simulator | Integrated | Intermediate | Python (stdlib) |
| 046. CSV Expense Analyzer | Finance | Intermediate | pandas |
| 047. Financial Transaction Cleaner | Finance | Intermediate | pandas |
| 048. Bank Statement Analyzer | Finance | Intermediate | pandas |
| 049. Sales CSV Analyzer | Finance | Intermediate | pandas |
| 050. Inventory CSV Analyzer | Logistics | Intermediate | pandas |
| 051. Supplier CSV Analyzer | Logistics | Intermediate | pandas |
| 052. Delivery Performance Analyzer | Logistics | Intermediate | pandas |
| 053. Transportation Cost Analyzer | Logistics | Intermediate | pandas |
| 054. Warehouse Utilization Analyzer | Logistics | Intermediate | pandas |
| 055. Stockout Analyzer | Logistics | Intermediate | pandas |
| 056. Excess Inventory Detector | Logistics | Intermediate | pandas |
| 057. Purchase Order Aging Analyzer | Logistics | Intermediate | pandas |
| 058. Customer Payment Delay Analyzer | Finance | Intermediate | pandas |
| 059. Logistics KPI Report Generator | Logistics | Intermediate | pandas |
| 060. Business Data Quality Auditor | Integrated | Intermediate | pandas |
| 061. Portfolio Return Calculator | Finance | Advanced | numpy |
| 062. Portfolio Risk Calculator | Finance | Advanced | numpy |
| 063. Monte Carlo Investment Simulator | Finance | Advanced | numpy |
| 064. Demand Distribution Simulator | Logistics | Advanced | numpy |
| 065. Inventory Uncertainty Simulator | Logistics | Advanced | numpy |
| 066. Safety Stock Simulation | Logistics | Advanced | numpy |
| 067. Warehouse Capacity Simulation | Logistics | Advanced | numpy |
| 068. Transportation Cost Simulation | Logistics | Advanced | numpy |
| 069. Lead-Time Variability Simulator | Logistics | Advanced | numpy |
| 070. Stockout Probability Simulator | Logistics | Advanced | numpy |
| 071. Multi-Product Inventory Simulation | Logistics | Advanced | numpy |
| 072. Scenario-Based Profit Simulator | Finance | Advanced | numpy |
| 073. Logistics Cost Sensitivity Analyzer | Logistics | Advanced | numpy |
| 074. Working Capital Simulator | Finance | Advanced | numpy |
| 075. Business Risk Monte Carlo Engine | Integrated | Advanced | numpy |
| 076. Financial Performance Analyzer | Finance | Advanced | pandas |
| 077. Monthly P&L Analyzer | Finance | Advanced | pandas |
| 078. Regional Sales Analyzer | Finance | Advanced | pandas |
| 079. SKU Performance Analyzer | Logistics | Advanced | pandas |
| 080. Inventory Turnover Analyzer | Logistics | Advanced | pandas |
| 081. Supplier Scorecard | Logistics | Advanced | pandas |
| 082. Logistics Cost Dashboard | Logistics | Advanced | pandas |
| 083. Customer Segmentation Analyzer | Finance | Advanced | pandas |
| 084. Cost-to-Serve Analyzer | Logistics | Advanced | pandas |
| 085. End-to-End Supply Chain Analytics System | Integrated | Advanced | pandas |
| 086. Financial KPI Dashboard | Finance | Professional | pandas |
| 087. Demand Trend Dashboard | Logistics | Professional | pandas |
| 088. Inventory Health Dashboard | Logistics | Professional | pandas |
| 089. Logistics Route Visualization | Logistics | Professional | pandas |
| 090. Supply Chain Network Graph | Network Science | Professional | networkx |
| 091. Logistics Bottleneck Detector | Network Science | Professional | networkx |
| 092. Supply Chain Dependency Analyzer | Network Science | Professional | networkx |
| 093. Demand Forecasting Model | Machine Learning | Professional | pandas |
| 094. Delivery Delay Prediction | Machine Learning | Professional | pandas |
| 095. Supplier Risk Prediction | Machine Learning | Professional | pandas |
| 096. Inventory Stockout Prediction | Machine Learning | Professional | pandas |
| 097. Customer Payment Risk Model | Machine Learning | Professional | pandas |
| 098. Logistics Cost Prediction Model | Machine Learning | Professional | pandas |
| 099. Vehicle Route Optimization System | Operations Research | Professional | pandas |
| 100. Intelligent Finance + Logistics Network Simulator | Integrated | Professional | pandas |
