### End to end TextSummarizer Project

Using HuggingFace

Basee model - google/pegasus-cnn_dailymail for text summarization

Dataset: Samsung/samsum
15K datapoints
    3 fields:
        (input)dialogue: text
        (output)Summary: human written summary of dialogue
        id: unique id of an example

### Workflows 

1. Config.yaml
2. Params.yaml
3. Config entity
4. Configuration Manager
5. Update the components- Data Ingestion,Data Transformation, Model Trainer
6. Create our Pipeline-- Training Pipeline,Prediction Pipeline
7. Front end-- Api's, Training APi's, Batch Prediction API's


Steps:
Training Pipeline:
    Dataingestion:
            Download the data as zip
            extract the downloaded zip
    Data transformation:
            load from disk ( convert from arrow to dataset_dict type) - ALL folders(Train,test,Validation)
            initialize tokenizer
            take input "dialogue" and apply tokenizer
            take output "summary" and apply as_target_tokenizer
            save the input, attention_mask and output_embeddings as dict
            save to disk
    Model trainer:
            Initiate tokenizer,model,transformed datasets,
            se2seqdatacollator 
            Trainer(trainable args and all prev info along with test and validation set for training,(due to  resource constraint))
            trainer.train()
            save the model and tokenizer
    Model Evaluation:
            Take few samples from the test set, load the saved tokenizer, model
            Metrics used: "rouge1", "rouge2", "rougeL", "rougeLsum"
Prediction Pipeline:
        Load the model 
        Use for prediction in FASTAPI


