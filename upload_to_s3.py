import boto3
import json
import random
import faker

# Generador de datos ficticios
fake = faker.Faker()
customer_types = ["Masivo", "Preferente", "Premium"]

def generate_credit_card_campaign_data(num_records=200):
    data = []
    for _ in range(num_records):
        record = {
            "nombre_cliente": fake.name(),
            "monto_tarjeta": round(random.uniform(500000, 15000000), 0),
            "tasa_interes": round(random.uniform(5, 15), 0),
            "tipo_cliente": random.choice(customer_types),
        }
        data.append(record)
    return data

# Nombre del bucket S3
BUCKET_NAME = "datos-campanas"
FILE_NAME = "campaign_data.json"

print("🟡 Generando datos ficticios...")
data = generate_credit_card_campaign_data()

print("🟡 Conectándose a AWS S3...")
s3 = boto3.client('s3')

s3.put_object(Bucket=BUCKET_NAME, Key=FILE_NAME, Body=json.dumps(data))

print(f"✅ Datos subidos exitosamente a S3 en el bucket {BUCKET_NAME}.")
