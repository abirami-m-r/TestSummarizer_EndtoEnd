from src.textSummarizer import logger
from src.textSummarizer.config.configuration import ConfigurationManager
from src.textSummarizer.components.data_ingestion import DataIngestion
from src.textSummarizer.components.data_transformation import DataTransformation
from src.textSummarizer.components.model_trainer import ModelTrainer
from src.textSummarizer.components.model_evaluation import ModelEvaluation
                                            


def initiate_data_ingestion():
    try:
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion=DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()
    except Exception as e:
        logger.error(e)
        raise e
    

def initiate_data_transformation():
    try:
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation=DataTransformation(config=data_transformation_config)
        data_transformation.convert()
    except Exception as e:
        logger.error(e)
        raise e
    
def initiate_model_trainer():
    try:
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer=ModelTrainer(config=model_trainer_config)
        #model_trainer.train() ## to save cpu , trained on colab and saved artifacts
    except Exception as e:
        logger.error(e)
        raise e
    
def initiate_model_evaluation():
    try:
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation=ModelEvaluation(config=model_evaluation_config)
        model_evaluation.evaluate()
    except Exception as e:
        logger.error(e)
        raise e
    
