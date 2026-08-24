"""
projects_data.py

Canonical metadata for all 100 projects in the
Finance-Logistics-100-Python-Projects repository.

This is the single source of truth consumed by file_generator.py.
Editing a project's tech stack, domain, or difficulty here is enough —
the generator derives folder/file layout from these fields plus the
phase rules in file_generator.py.
"""

from dataclasses import dataclass, field
from typing import List


@dataclass
class Project:
    number: int
    title: str
    domain: str          # Finance | Logistics | Operations Research | Network Science | Machine Learning | Integrated
    phase: int            # 1-8
    difficulty: str        # Beginner | Intermediate | Advanced | Professional
    technologies: List[str] = field(default_factory=list)
    needs_data: bool = False
    needs_notebook: bool = False
    needs_models: bool = False
    needs_config: bool = False

    @property
    def slug(self) -> str:
        s = self.title.lower()
        for ch in ["&", "-", "/", "(", ")", ",", ".", "+"]:
            s = s.replace(ch, " ")
        s = "_".join(s.split())
        return f"project_{self.number:03d}_{s}"


PHASE_FOLDERS = {
    1: "phase1_python_business_foundations",
    2: "phase2_business_logic",
    3: "phase3_data_structures_business_systems",
    4: "phase4_file_handling_real_data",
    5: "phase5_numpy_simulation",
    6: "phase6_pandas_business_analytics",
    7: "phase7_visualization_network_analysis",
    8: "phase8_machine_learning_optimization",
}


def _phase(n: int) -> int:
    if n <= 15: return 1
    if n <= 30: return 2
    if n <= 45: return 3
    if n <= 60: return 4
    if n <= 75: return 5
    if n <= 85: return 6
    if n <= 92: return 7
    return 8


def _difficulty(n: int) -> str:
    if n <= 30: return "Beginner"
    if n <= 60: return "Intermediate"
    if n <= 85: return "Advanced"
    return "Professional"


# (number, title, domain, technologies, extras)
# extras: needs_data, needs_notebook, needs_models, needs_config
_RAW = [
    (1, "Personal Cash Flow Analyzer", "Finance", [], {}),
    (2, "Simple Interest Calculator", "Finance", [], {}),
    (3, "Compound Interest Engine", "Finance", [], {}),
    (4, "Loan EMI Calculator", "Finance", [], {}),
    (5, "Profit Margin Calculator", "Finance", [], {}),
    (6, "Break-Even Calculator", "Finance", [], {}),
    (7, "Revenue Growth Analyzer", "Finance", [], {}),
    (8, "Expense Categorizer", "Finance", [], {}),
    (9, "Budget Variance Calculator", "Finance", [], {}),
    (10, "Invoice Generator", "Finance", [], {}),
    (11, "Product Pricing Calculator", "Finance", [], {}),
    (12, "Inventory Value Calculator", "Logistics", [], {}),
    (13, "Logistics Cost Calculator", "Logistics", [], {}),
    (14, "Landed Cost Calculator", "Logistics", [], {}),
    (15, "Small Business Financial Dashboard", "Finance", ["pandas"], {}),

    (16, "Progressive Tax Calculator", "Finance", [], {}),
    (17, "Investment Return Calculator", "Finance", [], {}),
    (18, "Loan Amortization Engine", "Finance", [], {}),
    (19, "Cash Reserve Simulator", "Finance", [], {}),
    (20, "Supplier Payment Scheduler", "Finance", [], {}),
    (21, "Customer Credit Limit Checker", "Finance", [], {}),
    (22, "Stock Reorder Calculator", "Logistics", [], {}),
    (23, "Safety Stock Calculator", "Logistics", [], {}),
    (24, "Economic Order Quantity Calculator", "Logistics", [], {}),
    (25, "Inventory Replenishment Engine", "Logistics", [], {}),
    (26, "Transportation Cost Estimator", "Logistics", [], {}),
    (27, "Vehicle Capacity Checker", "Logistics", [], {}),
    (28, "Delivery Priority Engine", "Logistics", [], {}),
    (29, "Supplier Risk Scorer", "Logistics", [], {}),
    (30, "Business Decision Rule Engine", "Operations Research", [], {}),

    (31, "Customer Ledger", "Finance", [], {}),
    (32, "Supplier Ledger", "Finance", [], {}),
    (33, "Product Catalog Engine", "Logistics", [], {}),
    (34, "Warehouse Inventory Manager", "Logistics", [], {}),
    (35, "Multi-Product Order System", "Logistics", [], {}),
    (36, "Shipment Tracking System", "Logistics", [], {}),
    (37, "Purchase Order Manager", "Logistics", [], {}),
    (38, "Sales Order Manager", "Finance", [], {}),
    (39, "Multi-Warehouse Stock Allocator", "Logistics", [], {}),
    (40, "Distributor Management System", "Logistics", [], {}),
    (41, "Retailer Network Manager", "Logistics", [], {}),
    (42, "Supplier Performance Database", "Logistics", [], {}),
    (43, "Customer Profitability Analyzer", "Finance", [], {}),
    (44, "Product Profitability Analyzer", "Finance", [], {}),
    (45, "End-to-End Order Lifecycle Simulator", "Integrated", [], {}),

    (46, "CSV Expense Analyzer", "Finance", ["pandas"], {"needs_data": True}),
    (47, "Financial Transaction Cleaner", "Finance", ["pandas"], {"needs_data": True}),
    (48, "Bank Statement Analyzer", "Finance", ["pandas"], {"needs_data": True}),
    (49, "Sales CSV Analyzer", "Finance", ["pandas"], {"needs_data": True}),
    (50, "Inventory CSV Analyzer", "Logistics", ["pandas"], {"needs_data": True}),
    (51, "Supplier CSV Analyzer", "Logistics", ["pandas"], {"needs_data": True}),
    (52, "Delivery Performance Analyzer", "Logistics", ["pandas"], {"needs_data": True}),
    (53, "Transportation Cost Analyzer", "Logistics", ["pandas"], {"needs_data": True}),
    (54, "Warehouse Utilization Analyzer", "Logistics", ["pandas"], {"needs_data": True}),
    (55, "Stockout Analyzer", "Logistics", ["pandas"], {"needs_data": True}),
    (56, "Excess Inventory Detector", "Logistics", ["pandas"], {"needs_data": True}),
    (57, "Purchase Order Aging Analyzer", "Logistics", ["pandas"], {"needs_data": True}),
    (58, "Customer Payment Delay Analyzer", "Finance", ["pandas"], {"needs_data": True}),
    (59, "Logistics KPI Report Generator", "Logistics", ["pandas"], {"needs_data": True}),
    (60, "Business Data Quality Auditor", "Integrated", ["pandas"], {"needs_data": True}),

    (61, "Portfolio Return Calculator", "Finance", ["numpy"], {}),
    (62, "Portfolio Risk Calculator", "Finance", ["numpy", "scipy"], {}),
    (63, "Monte Carlo Investment Simulator", "Finance", ["numpy", "matplotlib"], {}),
    (64, "Demand Distribution Simulator", "Logistics", ["numpy", "matplotlib"], {}),
    (65, "Inventory Uncertainty Simulator", "Logistics", ["numpy"], {}),
    (66, "Safety Stock Simulation", "Logistics", ["numpy"], {}),
    (67, "Warehouse Capacity Simulation", "Logistics", ["numpy"], {}),
    (68, "Transportation Cost Simulation", "Logistics", ["numpy"], {}),
    (69, "Lead-Time Variability Simulator", "Logistics", ["numpy"], {}),
    (70, "Stockout Probability Simulator", "Logistics", ["numpy", "scipy"], {}),
    (71, "Multi-Product Inventory Simulation", "Logistics", ["numpy", "pandas"], {}),
    (72, "Scenario-Based Profit Simulator", "Finance", ["numpy", "pandas"], {}),
    (73, "Logistics Cost Sensitivity Analyzer", "Logistics", ["numpy", "pandas", "matplotlib"], {}),
    (74, "Working Capital Simulator", "Finance", ["numpy", "pandas"], {}),
    (75, "Business Risk Monte Carlo Engine", "Integrated", ["numpy", "pandas", "matplotlib"], {}),

    (76, "Financial Performance Analyzer", "Finance", ["pandas", "matplotlib"], {"needs_data": True}),
    (77, "Monthly P&L Analyzer", "Finance", ["pandas", "matplotlib"], {"needs_data": True}),
    (78, "Regional Sales Analyzer", "Finance", ["pandas", "matplotlib"], {"needs_data": True}),
    (79, "SKU Performance Analyzer", "Logistics", ["pandas", "matplotlib"], {"needs_data": True}),
    (80, "Inventory Turnover Analyzer", "Logistics", ["pandas", "matplotlib"], {"needs_data": True}),
    (81, "Supplier Scorecard", "Logistics", ["pandas", "matplotlib"], {"needs_data": True}),
    (82, "Logistics Cost Dashboard", "Logistics", ["pandas", "plotly"], {"needs_data": True}),
    (83, "Customer Segmentation Analyzer", "Finance", ["pandas", "scikit-learn"], {"needs_data": True}),
    (84, "Cost-to-Serve Analyzer", "Logistics", ["pandas", "matplotlib"], {"needs_data": True}),
    (85, "End-to-End Supply Chain Analytics System", "Integrated", ["pandas", "numpy", "matplotlib"], {"needs_data": True}),

    (86, "Financial KPI Dashboard", "Finance", ["pandas", "plotly"], {"needs_data": True}),
    (87, "Demand Trend Dashboard", "Logistics", ["pandas", "plotly"], {"needs_data": True}),
    (88, "Inventory Health Dashboard", "Logistics", ["pandas", "plotly"], {"needs_data": True}),
    (89, "Logistics Route Visualization", "Logistics", ["pandas", "plotly", "networkx"], {"needs_data": True}),
    (90, "Supply Chain Network Graph", "Network Science", ["networkx", "matplotlib"], {"needs_data": True}),
    (91, "Logistics Bottleneck Detector", "Network Science", ["networkx", "pandas"], {"needs_data": True}),
    (92, "Supply Chain Dependency Analyzer", "Network Science", ["networkx", "pandas"], {"needs_data": True}),

    (93, "Demand Forecasting Model", "Machine Learning", ["pandas", "numpy", "scikit-learn", "matplotlib"],
     {"needs_data": True, "needs_notebook": True, "needs_models": True}),
    (94, "Delivery Delay Prediction", "Machine Learning", ["pandas", "numpy", "scikit-learn"],
     {"needs_data": True, "needs_notebook": True, "needs_models": True}),
    (95, "Supplier Risk Prediction", "Machine Learning", ["pandas", "numpy", "scikit-learn"],
     {"needs_data": True, "needs_notebook": True, "needs_models": True}),
    (96, "Inventory Stockout Prediction", "Machine Learning", ["pandas", "numpy", "scikit-learn"],
     {"needs_data": True, "needs_notebook": True, "needs_models": True}),
    (97, "Customer Payment Risk Model", "Machine Learning", ["pandas", "numpy", "scikit-learn"],
     {"needs_data": True, "needs_notebook": True, "needs_models": True}),
    (98, "Logistics Cost Prediction Model", "Machine Learning", ["pandas", "numpy", "scikit-learn"],
     {"needs_data": True, "needs_notebook": True, "needs_models": True}),
    (99, "Vehicle Route Optimization System", "Operations Research",
     ["pandas", "numpy", "networkx", "ortools"],
     {"needs_data": True, "needs_config": True}),
    (100, "Intelligent Finance + Logistics Network Simulator", "Integrated",
     ["pandas", "numpy", "scikit-learn", "networkx", "matplotlib", "plotly"],
     {"needs_data": True, "needs_notebook": True, "needs_models": True, "needs_config": True}),
]


def load_projects() -> List[Project]:
    projects = []
    for number, title, domain, tech, extras in _RAW:
        projects.append(
            Project(
                number=number,
                title=title,
                domain=domain,
                phase=_phase(number),
                difficulty=_difficulty(number),
                technologies=tech,
                needs_data=extras.get("needs_data", False),
                needs_notebook=extras.get("needs_notebook", False),
                needs_models=extras.get("needs_models", False),
                needs_config=extras.get("needs_config", False),
            )
        )
    assert len(projects) == 100, f"expected 100 projects, got {len(projects)}"
    numbers = [p.number for p in projects]
    assert numbers == list(range(1, 101)), "project numbering must be continuous 1-100 with no duplicates"
    return projects


if __name__ == "__main__":
    ps = load_projects()
    print(f"Loaded {len(ps)} projects across {len(PHASE_FOLDERS)} phases.")
