from data.cts_access import load_cts, dump_cts

cts_name = "HMM_scenario_2_4"

cts = load_cts(cts_name)
cts.convert_by_default()
dump_cts(cts, 'new_' + cts_name)
