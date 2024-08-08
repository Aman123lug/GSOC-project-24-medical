
from dataclasses import dataclass, field

from lightrag.core import Component, Generator, DataClass
from lightrag.components.model_client import GroqAPIClient
from lightrag.components.output_parsers import JsonOutputParser

@dataclass
class QAOutput(DataClass):
    explanation: str = field(
        metadata={"desc": "A brief explanation of the concept in one sentence."}
    )
    example: str = field(metadata={"desc": "An example of the concept in a sentence."})


qa_template = r"""<SYS>
Your are MedSathi a helpful pharmacist. Use the given context to get the knowledge of the medicine and provide the asked information about the medicine using the context, explain in details what is inside the context their result  answer only using the context don't add any other information over it. 
context: {context}.
    
   
    
<OUTPUT_FORMAT>
{{output_format_str}}
</OUTPUT_FORMAT>
</SYS>
User: {{input_str}}

You:"""


class QA(Component):
    def __init__(self):
        super().__init__()

        parser = JsonOutputParser(data_class=QAOutput, return_data_class=True)
        self.generator = Generator(
            model_client=GroqAPIClient(),
            model_kwargs={"model": "llama3-8b-8192"},
            template=qa_template,
            prompt_kwargs={"output_format_str": parser.format_instructions()},
            output_processors=parser,
        )

    def call(self, query: str):
        return self.generator.call({"input_str": query})

    async def acall(self, query: str):
        return await self.generator.acall({"input_str": query})
    
