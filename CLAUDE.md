# Economic Analysis Model (Simple path)

Streamlit port of the Excel "Simple" analysis: scenario-weighted projections, NPVs, price heuristics.

## Run / test
- `pip install -r requirements.txt`, then `streamlit run app.py`
- `python -m pytest -q`

## Files
- `app.py` - Streamlit UI (sidebar inputs, KPIs, chart, table, JPEG download)
- `economics_model.py` - model logic; `run_simple_model(inp, horizon_years)` returns NPVs for years 1..H
- `export_image.py` - builds the results JPEG (matplotlib, no browser needed)
- `tests/test_economics_model.py` - pytest suite
- `docs/index.html` - static page; `manual/` - user manual PDF

## Decisions
- Years dropdown (1-10) sets the horizon for gross profit NPV, gross revenue NPV (target), terminal-style NPV, chart and table.
- Discount premium (continuous) and pessimistic weight (discrete) are typed number inputs.

## Gotchas
- `npv_gross_profit_10y` keeps its old name but follows the chosen horizon.
- Excel NPV semantics: first cash flow is discounted by (1+r)^1.
