from transformers import GPT2LMHeadModel, GPT2Tokenizer

def generate_description(attributes):
    model_name = 'gpt2'
    tokenizer = GPT2Tokenizer.from_pretrained(model_name)
    model = GPT2LMHeadModel.from_pretrained(model_name)

    input_text = f"Generate a product description for: {attributes}"
    inputs = tokenizer.encode(input_text, return_tensors='pt')
    outputs = model.generate(inputs, max_length=150, num_return_sequences=1)

    description = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return description.strip()

if __name__ == "__main__":
    attributes = "Color: Red, Size: Medium, Material: Cotton, Brand: XYZ"
    print(generate_description(attributes))
