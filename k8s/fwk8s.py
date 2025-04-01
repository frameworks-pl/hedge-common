import argparse

def startPodSession():
    pass

def main():

    
    parser = argparse.ArgumentParser(prog="k8s helper",
        description='Script to speed up operations on k8s')
    #parser.add_argument('-it', "--interactive", type=str, help='Enter interactive session of a pod')
    # parser.add_argument('-m', "--module", type=str, help='Execute target from the provided module rather than from default one (hedge)', default='hedge')
    # parser.add_argument('-p', "--port", type=str, help='Port of the repository with server configuration', default=None)
    # parser.add_argument('-w', "--workdir", type=str, help='Location of work directory', default=None)
    # parser.add_argument('-t', "--target", type=str, help='Target to execute', default='build')
    # parser.add_argument('-lt', "--list-targets", help="List available arguments", nargs='?', const=True, default=None)
    # parser.add_argument('-s', "--skip", type=bool, help='Skip cloning repository', default=False)
    # parser.add_argument('-v', "--verbose", type=bool, help='Verbose mode', default=False)
    # parser.add_argument('-o', "--sshoptions", type=str, help='SSH options', default="")
    
    args = parser.parse_args()

    #TODO:
    # - add target param, read it here
    # - use value of targetr param to call appropriate target
    # - inside target use -n param to get name of pod to run
    # - write function that can figure out which 'real' pod to execute based on the name
    targetMethod = getattr(hedgeInstance, target);


if __name__ == '__main__':
    exitCode = main()
    exit(exitCode)
