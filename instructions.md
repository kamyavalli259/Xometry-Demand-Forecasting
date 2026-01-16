1. Go to the Repo 
cd xometry-demand-forecasting
 
2. ls
should see
data  etl  features  models  pipeline  requirements.txt  README.md


3. Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

4. install dependencies
pip install --upgrade pip
pip install -r requirements.txt


5. Generate Sample Data
python data/generate_sample_data.py

Expected output: Sample data generated at data/raw/orders.csv

6. Run Spark-ETL
verify spark: spark-submit --version
Run ETL: spark-submit etl/spark_etl.py

Expected: Files written to data/processed/

7. Run the Forecasting & Optimization Pipeline
python pipeline/run_pipeline.py

Expected output: RMSE: <some number>

8. View MLflow Experiments
Start MLFlow UI: mlflow ui
Open browser: http://localhost:5000

Expected: Should see experiment runs, logged parameters, metrics

9. In the terminal close the virtual environment
deactivate 

