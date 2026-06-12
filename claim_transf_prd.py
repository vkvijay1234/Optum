# Databricks notebook source
# MAGIC %run "/Workspace/optum/connectors"
# MAGIC

# COMMAND ----------

# MAGIC %run "/Workspace/optum/generic"

# COMMAND ----------

claims_df = read_bronze_json("Claims")

# COMMAND ----------

claims_df = drop_columns(claims_df,['_id'])

# COMMAND ----------

claims_df = drop_columns(claims_df,['Claim_Or_Rejected'])

# COMMAND ----------

claims_df = claims_df.replace("NaN",None)
claims_df = claims_df.withColumn("claim_amount", claims_df['claim_amount'].cast("integer"))
claims_df = claims_df.withColumn("claim_date", claims_df['claim_date'].cast("date"))

# COMMAND ----------

write2silver(claims_df,"claims_S.csv")

# COMMAND ----------

write2silver(claims_df,"claims_S_new.csv")
