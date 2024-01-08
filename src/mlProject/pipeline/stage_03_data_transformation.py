from mlProject.config.configuration import ConfigurationManager
from mlProject.components.data_transformation import DataTransformation
from mlProject import logger
from pathlib import Path


STAGE_NAME = 'Data Transformation stage'

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            with open(Path('artifacts/data_validation/status.txt'), 'r') as f:
                status = f.read().split(' ')[-1]

            if status == 'True':
                config = ConfigurationManager()
                data_transformation_config = config.get_data_transformation_config()
                data_transformation = DataTransformation(config=data_transformation_config)
                data_transformation.train_test_splitting()
            else:
                raise Exception("Your data schema is not valid")
        except Exception as e:
            raise e
        
if __name__=="__main__":
    try:
        logger.info(f'>>>>>>>> stage {STAGE_NAME} started <<<<<<<')
        data_transformation = DataTransformationTrainingPipeline()
        data_transformation.main()
        logger.info(f'>>>>>>> stage {STAGE_NAME} completed <<<<<<<<')
    except Exception as e:
        raise e