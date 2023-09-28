from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier import logger



STAGE_NAME = 'Data Ingestion stage'
try:
    logger.info(f">>>>>> {STAGE_NAME} started <<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> {STAGE_NAME} completed <<<<<")

except Exception as e:
    logger.exception(e)
    raise e