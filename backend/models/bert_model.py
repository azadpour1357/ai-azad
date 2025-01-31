from transformers import BertTokenizer, BertForQuestionAnswering, pipeline

class TaxQuestionAnswering:
    def __init__(self):
        self.tokenizer = BertTokenizer.from_pretrained('bert-large-uncased-whole-word-masking-finetuned-squad')
        self.model = BertForQuestionAnswering.from_pretrained('bert-large-uncased-whole-word-masking-finetuned-squad')
        self.qa_pipeline = pipeline("question-answering", model=self.model, tokenizer=self.tokenizer)
    
    def get_answer(self, question, context):
        return self.qa_pipeline({'question': question, 'context': context})['answer']
