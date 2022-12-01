import pyspark

data = []
for x in range(5):
    data.append((random.randint(0,9), random.randint(0,9)))
df = spark.createDataFrame(data, ("label", "data"))

df.show()

'''print('Lectura Archivo Parquet')
data = spark.read.parquet('https://wus1staadt1s.blob.core.windows.net/landing/cua_sap_isq_prototipos/Tables/NCIRQuery.parquet')
display(data)'''