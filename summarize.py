from langchain_openai import ChatOpenAI
from langchain.chains import MapReduceDocumentsChain, StuffDocumentsChain, LLMChain
from langchain.prompts import PromptTemplate
from langchain.schema import Document
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

# Connect to DB
client = MongoClient(os.getenv("MONGO_URI"))
db = client.news_db
raw_collection = db.raw_articles
summary_collection = db.summaries

def generate_summaries():
    llm = ChatOpenAI(
        model="gpt-4o",
        temperature=0.7,
        api_key=os.getenv("OPENAI_API_KEY")
    )
    articles = raw_collection.find({"summary": {"$exists": False}})
    
    # Define prompts
    map_template = """The following is a section of a news article. Provide a concise summary of the key points:
    "{text}"
    Concise summary:"""
    map_prompt = PromptTemplate(template=map_template, input_variables=["text"])
    
    combine_template = """The following are summaries of different sections of a news article. Combine them into a final, coherent summary:
    "{text}"
    Final summary:"""
    combine_prompt = PromptTemplate(template=combine_template, input_variables=["text"])
    
    # Create chains
    map_chain = LLMChain(llm=llm, prompt=map_prompt)
    reduce_chain = LLMChain(llm=llm, prompt=combine_prompt)
    
    # Create the final chain
    chain = MapReduceDocumentsChain(
        llm_chain=map_chain,
        reduce_documents_chain=StuffDocumentsChain(
            llm_chain=reduce_chain,
            document_variable_name="text"
        ),
        document_variable_name="text"
    )
    
    for article in articles:
        content = f"{article['title']}\n\n{article['content']}"
        docs = [Document(page_content=content)]
        summary = chain.run(docs)
        
        # Save summary
        summary_collection.insert_one({
            "url": article["url"],
            "title": article["title"],
            "summary": summary,
            "source": article["source"]["name"],
            "publishedAt": article["publishedAt"]
        })
        # Mark as processed
        raw_collection.update_one(
            {"_id": article["_id"]},
            {"$set": {"summary": True}}
        )
    print("Summaries generated.")

if __name__ == "__main__":
    generate_summaries()