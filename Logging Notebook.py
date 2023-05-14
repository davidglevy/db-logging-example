# Databricks notebook source
# MAGIC %md
# MAGIC ## Import the relative module

# COMMAND ----------

from db_logging_common import setup_logging
logger = setup_logging()

# COMMAND ----------

# MAGIC %md
# MAGIC ## Log to your hearts content

# COMMAND ----------

import time

logger.info("Hello World")
time.sleep(1)
logger.warning("An operation")
time.sleep(2.6)
logger.info("And done")
