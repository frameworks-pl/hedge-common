import logging
import os

class Hedge:
    def __init__(self, repoRootPath):
        self.repoRootPath = repoRootPath

    def preflight(self, agent, params):
        agent.runCommand('add-apt-repository ppa:neovim-ppa/stable')
        agent.runCommand('apt-get update')

    def vim(self, agent, params):
        if not os.environ['HOME']:
            logging.error('HOME environment variable is not define, cannot continue')
            return
        home = os.environ['HOME']
        agent.ensurePackages(['neovim'])

        
        agent.ensureFile('/vim/.vimrc', f"{home}/.vimrc")

    def k8s_helper(self, agent, params):
        if not os.environ['HOME']:
            logging.error('HOME environment variable is not define, cannot continue')
            return
        home = os.environ['HOME']    
        agent.ensureFile('/k8s/fwk8s.py', f"{home}/scripts/fwk8s.py")
        
    def lazyvim(self, agent, params):
        pass
