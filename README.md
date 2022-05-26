# wildQA
Question-Answering in the wild. 

This project is planned as an exploration of the ability of Information Retrieval, Question-Answering methods as applied to a 'document in the wild'. 

We build a system to pass the Driving Knowledge exam by using Washington State Department of Licensing Driving Guide as the knowledge repository. 

Here are the stages we will build.

1. Parsing a PDF (just text at first) to generate a decent text corpus
2. Use classical IR methods (e.g. BM25) to fetch create a good retrieval system to fetch relevant docs/pages given a question/query.
3. Reraking paragraphs from retrieved pages using sentence/document embeddings to get the best candidate for the query. 
4. Applying a BERT-like QA model to find the answer from the paragraph. 
5. Sentence Processing to parse a multiple choice question. 
6. Handle images in documents and questions (this seems a bit difficult) 
7. See if we can stich it all together to make a QA Bot which takes in the pdf and is ready to answer questions. 

