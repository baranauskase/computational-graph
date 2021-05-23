
import argparse
from comp_graph import eval_graph

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Compute graphs.')
    parser.add_argument('path', type=str, help='path to graph definition')
    parser.add_argument('--conf', nargs=2, action='append')
    args = parser.parse_args()

    palceholder_vals = {conf[0]: int(conf[1]) for conf in args.conf}

    output = eval_graph(args.path, palceholder_vals)
    
    print(output)