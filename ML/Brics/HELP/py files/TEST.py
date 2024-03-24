def crest_pulse(x):
    return ((x.abs().max()/x.abs().mean())/(x.abs().max()/(( x ** 2).mean() ** 0.5))).round(6)

form_factor = data_spark_clean.groupby('time').agg(
    crest_pulse(data_spark_clean.bear1).alias("bear1_form"),
    crest_pulse(data_spark_clean.bear2).alias("bear2_form"),
    crest_pulse(data_spark_clean.bear3).alias("bear3_form"),
    crest_pulse(data_spark_clean.bear4).alias("bear4_form")
    )