from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained("instruction-pretrain/medicine-Llama3-8B")
tokenizer = AutoTokenizer.from_pretrained("instruction-pretrain/medicine-Llama3-8B")

# Put your input here, NO prompt template is required
user_input = '''what is the main cause of cancer

'''

inputs = tokenizer(user_input, return_tensors="pt", add_special_tokens=True).input_ids.to(model.device)
outputs = model.generate(input_ids=inputs, max_new_tokens=400)[0]

answer_start = int(inputs.shape[-1])
pred = tokenizer.decode(outputs[answer_start:], skip_special_tokens=True)

print(pred)
