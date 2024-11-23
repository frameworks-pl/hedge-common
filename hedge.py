import logging
import os

class Hedge:
    def __init__(self, repoRootPath):
        self.repoRootPath = repoRootPath

    def preflight(self, agent, params):
        agent.runCommand('apt-get update')


    def vim(self, agent, params):
        if not os.environ['USER']:
            logging.error('USER environment variable is not define, cannot continue')
            return
        user = os.environ['USER']
        agent.ensurePackages(['neovim'])
        agent.ensureFile('/vim/.vimrc', f"/home/{user}/.vimrc")