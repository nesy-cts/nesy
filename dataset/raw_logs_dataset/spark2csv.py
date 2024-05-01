from logparser.Drain import LogParser


input_dir  = 'spark/' # The input directory of log file
output_dir = 'spark/'  # The output directory of parsing results
log_file   = 'spark_2.log'  # The input log file name
log_format = "<Date> <Time> <Level> <Component>: <Content>"  # spark log format
# Regular expression list for optional preprocessing (default: [])
regex      = [r"(\d+\.){3}\d+", r"\b[KGTM]?B\b", r"([\w-]+\.){2,}[\w-]+"]
st         = 0.5  # Similarity threshold
depth      = 4  # Depth of all leaf nodes

parser = LogParser(log_format, indir=input_dir, outdir=output_dir,  depth=depth, st=st, rex=regex)
parser.parse(log_file)
