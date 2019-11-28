import pyspark.sql

spark = pyspark.sql.SparkSession.builder.getOrCreate()

spark.read.jdbc('jdbc:posgresql://localhost:5432/pagila',
                'customer',
                properties={"user":"repl", "password":"password"})



