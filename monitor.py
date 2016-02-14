import time
import clips
import sys

def msg(s):
    print "M> %s" % s

clips.RegisterPythonFunction(msg)

def load_facts(facts_file):
    clips.LoadFacts(facts_file)

def load_rules(rules_file):
    clips.Load(rules_file)

def repeat(interval, func, *args, **kwargs):
    try:
        while True:
            func(*args, **kwargs)
            time.sleep(interval)
    except KeyboardInterrupt:
        msg("exiting ...")


def run_checks(facts_file, rules_file):
    clips.Reset()
    load_rules(rules_file)
    load_facts(facts_file)
    clips.Run()



if __name__=='__main__':
    facts_file = sys.argv[1]
    rules_file = sys.argv[2]
    bindings_file = sys.argv[3]
    __import__(bindings_file)
    freq = int(sys.argv[4])
    repeat(freq, run_checks, facts_file, rules_file)
