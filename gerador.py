from google import genai
import os
from google.colab import userdata

# 1. Configurar a chave da API buscando direto dos Secrets salvos no Colab
api_key = userdata.get('GEMINI_API_KEY')
client = genai.Client(api_key=api_key)

# 2. Configurar o prompt focado em textura de pelos para treino de tatuagem
prompt = "close-up of realistic and detailed animal fur texture, focused on the layer of hair for tattoo practice"

print("Gerando imagem...")
result = client.models.generate_images(
    model='imagen-3.0-generate-002',
    prompt=prompt,
    config=dict(
        number_of_images=1,
        output_mime_type="image/png"
    )
)

# 3. Salvar o arquivo de imagem localmente no ambiente
for i, generated_image in enumerate(result.generated_images):
    image_path = f"animal_fur_tattoo_{i}.png"
    with open(image_path, 'wb') as f:
        f.write(generated_image.image.image_bytes)
    print(f"Imagem salva com sucesso como: {image_path}")
