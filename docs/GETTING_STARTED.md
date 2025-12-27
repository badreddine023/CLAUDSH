# Getting Started with CLAUDSH

Welcome to the Quranic Hyper-Analysis Framework! This guide will help you set up and start using CLAUDSH for advanced Quranic analysis.

## Prerequisites

Before you begin, ensure you have the following installed on your system:

- **Node.js**: Version 22 or higher (download from [nodejs.org](https://nodejs.org))
- **Python**: Version 3.11 or higher (download from [python.org](https://www.python.org))
- **MySQL or TiDB**: Database server for storing analysis results
- **pnpm**: Package manager for Node.js (install via `npm install -g pnpm`)

## Installation Steps

### 1. Clone the Repository

```bash
git clone https://github.com/badreddine023/CLAUDSH.git
cd CLAUDSH
```

### 2. Install Node.js Dependencies

```bash
pnpm install
```

This command installs all required Node.js packages for the frontend and backend services.

### 3. Install Python Dependencies

```bash
pip install -r requirements.txt
```

This installs all Python libraries needed for the analysis engines, including NumPy, Pandas, NLTK, and more.

### 4. Set Up Environment Variables

Create a `.env` file in the project root with the following variables:

```env
DATABASE_URL=mysql://user:password@localhost:3306/quran_analysis
VITE_APP_TITLE=Quranic Analysis System
VITE_APP_LOGO=/logo.svg
NODE_ENV=development
```

Replace the database credentials with your actual MySQL/TiDB connection details.

### 5. Initialize the Database

```bash
pnpm db:push
```

This command creates the necessary database tables and schema based on the Drizzle ORM configuration.

### 6. Start the Development Server

```bash
pnpm dev
```

The application will start on `http://localhost:5173` by default. Open this URL in your web browser to access the CLAUDSH interface.

## Project Structure

Understanding the project layout will help you navigate and contribute effectively:

| Directory | Purpose |
|-----------|---------|
| `client/` | React frontend application with UI components |
| `server/` | Backend services and API routes |
| `src/` | Python analysis modules and engines |
| `data/` | Quran datasets and analysis results |
| `docs/` | Documentation and guides |
| `notebooks/` | Jupyter notebooks for exploratory analysis |
| `tests/` | Unit tests and integration tests |

## Running Analysis

### Complete Pipeline

To run the full analysis pipeline:

```bash
python src/main_pipeline.py
```

This executes all analysis stages sequentially: preprocessing, local analysis, non-local analysis, information theory calculations, and semantic field extraction.

### Individual Analysis Modules

You can run specific analysis modules independently:

```bash
# Markov chain analysis
python -m src.local_analysis.markov_chains

# Entropy calculations
python -m src.information_theory.entropy_calculator

# Semantic field extraction
python -m src.semantic_analysis.field_extractor
```

## Using the Dashboard

The interactive dashboard provides a user-friendly interface for exploring analysis results:

1. **Navigate to the Dashboard**: Click "Explore Analysis" on the home page or visit `/dashboard`
2. **Select Analysis Type**: Use the tabs to switch between different analysis views
3. **Explore Visualizations**: Interact with charts and graphs to discover patterns
4. **Export Results**: Download analysis results in JSON, CSV, or PDF formats

## Configuration

The `config.yaml` file controls analysis parameters and settings:

```yaml
analysis:
  markov_orders: [1, 2, 3, 4, 5]      # Markov chain orders to analyze
  window_sizes: [10, 25, 50, 100]     # Window sizes for local analysis
  entropy_levels: ['word', 'root', 'letter']  # Entropy calculation levels

themes:
  clusters:                            # Semantic field clusters
    - 'توحيد/Tawhid/Monothéisme'
    - 'نبوة/Prophecy/Prophétie'
    # ... more themes
```

Modify these settings to customize the analysis behavior.

## Common Tasks

### Adding a New Analysis Feature

1. Create a new Python module in the appropriate `src/` subdirectory
2. Implement your analysis logic following the existing patterns
3. Add a corresponding API endpoint in `server/routers.ts`
4. Create a React component in `client/src/pages/` to display results
5. Write tests for your new feature
6. Update documentation with usage examples

### Viewing Analysis Results

Results are stored in the `data/outputs/` directory:

- **Visualizations**: PNG/SVG files in `data/outputs/visualizations/`
- **Reports**: PDF/HTML files in `data/outputs/reports/`
- **Raw Data**: JSON/CSV files in `data/processed/`

### Debugging

Enable debug logging by setting the environment variable:

```bash
DEBUG=claudsh:* pnpm dev
```

This provides detailed logs for troubleshooting issues.

## Troubleshooting

### Database Connection Error

If you encounter database connection errors:

1. Verify MySQL/TiDB is running: `mysql -u user -p -h localhost`
2. Check the DATABASE_URL in your `.env` file
3. Ensure the database user has proper permissions
4. Run `pnpm db:push` again to reinitialize

### Python Module Not Found

If Python modules are not found:

```bash
# Reinstall dependencies
pip install --force-reinstall -r requirements.txt

# Add project to Python path
export PYTHONPATH="${PYTHONPATH}:$(pwd)"
```

### Port Already in Use

If port 5173 is already in use:

```bash
# Use a different port
pnpm dev -- --port 3000
```

## Next Steps

After completing the installation:

1. **Explore the Dashboard**: Familiarize yourself with the analysis interface
2. **Read the Roadmap**: Understand the project's development phases
3. **Review Examples**: Check the notebooks directory for example analyses
4. **Contribute**: See the CONTRIBUTING.md file to get involved

## Support & Documentation

- **Full Documentation**: See the `docs/` directory
- **API Reference**: Available at `/api/docs` when the server is running
- **GitHub Issues**: Report bugs or request features on GitHub
- **Community**: Join discussions in the GitHub Discussions tab

## Additional Resources

- [Arabic NLP Guide](./ARABIC_GUIDE.md)
- [API Documentation](./API_DOCUMENTATION.md)
- [Development Roadmap](../ROADMAP.md)
- [Contributing Guidelines](../CONTRIBUTING.md)

Happy analyzing! 🚀
