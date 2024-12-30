from src.textSummarizer import logger
from src.textSummarizer.pipeline.training_pipeline import (
                                                            initiate_data_ingestion,
                                                            initiate_data_transformation,
                                                            initiate_model_trainer,
                                                            initiate_model_evaluation
                                                        )


def main():
    stage = "Data Ingestion"
    logger.info(f"<<<<<<< {stage} started >>>>>>>>")
    initiate_data_ingestion()
    logger.info(f"<<<<<<< {stage} Completed >>>>>>>>")

    stage = "Data Transformation"
    logger.info(f"<<<<<<< {stage} started >>>>>>>>")
    initiate_data_transformation()
    logger.info(f"<<<<<<< {stage} Completed >>>>>>>>")

    stage = "Model trainer"
    logger.info(f"<<<<<<< {stage} started >>>>>>>>")
    initiate_model_trainer()
    logger.info(f"<<<<<<< {stage} Completed >>>>>>>>")

    stage = "Model Evaluation"
    logger.info(f"<<<<<<< {stage} started >>>>>>>>")
    initiate_model_evaluation()
    logger.info(f"<<<<<<< {stage} Completed >>>>>>>>")

if __name__=="__main__":
    main()