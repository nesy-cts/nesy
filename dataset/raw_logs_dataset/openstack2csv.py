from logparser.Drain import LogParser

input_dir = 'open_stack/'  # The input directory of log file
output_dir = 'open_stack/'  # The output directory of parsing results
log_file = 'open_stack_2.log'  # The input log file name
log_format = "<Logrecord> <Date> <Time> <Pid> <Level> <Component> \[<ADDR>\] <Content>"  # spark log format
# Regular expression list for optional preprocessing (default: [])
regex = [r"((\d+\.){3}\d+,?)+", r"/.+?\s", r"\d+"]
st = 0.5  # Similarity threshold
depth = 4  # Depth of all leaf nodes

parser = LogParser(log_format, indir=input_dir, outdir=output_dir, depth=depth, st=st, rex=regex)
parser.parse(log_file)