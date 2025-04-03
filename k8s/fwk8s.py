import argparse
import logging
import sys
import inspect

def podSessionTarget():
    print("podSessionTarget")

def deploymentApplyTarget():
    print("deploymentApplyTarget")


def listTargets(current_module):
    functions = inspect.getmembers(current_module, inspect.isfunction)
    target_functions = [name[:-6] for name, func in functions if name.endswith("Target")]
    return target_functions

def main():   
    parser = argparse.ArgumentParser(prog="k8s helper",
        description='Script to speed up operations on k8s')
    #parser.add_argument('-it', "--interactive", type=str, help='Enter interactive session of a pod')
    # parser.add_argument('-m', "--module", type=str, help='Execute target from the provided module rather than from default one (hedge)', default='hedge')
    # parser.add_argument('-p', "--port", type=str, help='Port of the repository with server configuration', default=None)
    # parser.add_argument('-w', "--workdir", type=str, help='Location of work directory', default=None)
    parser.add_argument('-t', "--target", type=str, help='Target to execute')
    parser.add_argument('-lt', "--list-targets", help="List available arguments", nargs='?', const=True, default=None)
    # parser.add_argument('-s', "--skip", type=bool, help='Skip cloning repository', default=False)
    # parser.add_argument('-v', "--verbose", type=bool, help='Verbose mode', default=False)
    # parser.add_argument('-o', "--sshoptions", type=str, help='SSH options', default="")
    
    args = parser.parse_args()
    current_module = sys.modules[__name__]

    if args.list_targets:
        print("\nList of available targets (if you do not see one you are looking for, check if signature is correct):")
        targets = listTargets(current_module)
        for key in targets:
            print(key) 
        return 0

    #TODO:
    # - add target param, read it here
    # - use value of targetr param to call appropriate target
    # - inside target use -n param to get name of pod to run
    # - write function that can figure out which 'real' pod to execute based on the name
    if not args.target:
        logging.error("Missing target")
        return 1

    #append "Target" to target
    target = args.target + "Target"

    target_func = None
    if hasattr(current_module, target):
        target_func = getattr(current_module, target)

    if not target_func:
        logging.error(f"There is no such target: '{args.target}'")
        return 1;

    target_func()


if __name__ == '__main__':
    exitCode = main()
    exit(exitCode)
