
import argparse
from comp_graph import eval_graph

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Compute graphs.')
    parser.add_argument('path', type=str, help='path to graph definition')
    args = parser.parse_args()

    output = eval_graph(args.path)
    
    print(output)