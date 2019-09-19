# Databricks notebook source
# MAGIC %sh cat /dbfs/databricks-datasets/adult/README.md

# COMMAND ----------

teste = spark.read.csv("/databricks-datasets/adult/adult.data")

# COMMAND ----------

display(teste)

# COMMAND ----------

teste.registerTempTable('teste')

# COMMAND ----------

# MAGIC %sql select _c14, count(1) from teste group by 1 order by 2 desc;

# COMMAND ----------

# MAGIC %scala
# MAGIC 
# MAGIC print("teste")

# COMMAND ----------

# MAGIC %r
# MAGIC 
# MAGIC print("teste")

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC ## teste de markdown do databricks
# MAGIC 
# MAGIC * bullet
# MAGIC 
# MAGIC > ref
# MAGIC 
# MAGIC `código intenso`

# COMMAND ----------


